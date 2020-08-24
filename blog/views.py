from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.http import require_http_methods
from blog.filters import PostFilter, TestCaseFilter
from blog.models import Post, TestCase, Tag
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, TestCaseSerializer, TagSerializer
from dwebsocket import accept_websocket
from .utils import getPathList, saveFile
from django.http import JsonResponse
from .TestSuite import TestSuite

class StandardPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
def index(httpRequest):
    return render(httpRequest, 'blog/index.html', context={
        'title': 'My first',
        'my': 'Charles\''
    })
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    # 设置filter的类为我们自定义的类
    filter_class = PostFilter

class TestCaseViewSet(ModelViewSet):
    queryset = TestCase.objects.all().order_by("id")
    serializer_class = TestCaseSerializer
    filter_backends = (DjangoFilterBackend,)
    # 设置filter的类为我们自定义的类
    filter_class = TestCaseFilter
    pagination_class = StandardPageNumberPagination

class TestSuiteViewSet(ModelViewSet):
    queryset = TestCase.objects.all().order_by("id")
    serializer_class = TestCaseSerializer
    filter_backends = (DjangoFilterBackend,)
    # 设置filter的类为我们自定义的类
    filter_class = TestCaseFilter
    pagination_class = StandardPageNumberPagination

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all().order_by("id")
    serializer_class = TagSerializer

@require_http_methods(['POST'])
def saveSuiteFile(request):
    content = json.loads(request.body.decode('utf-8'))
    content = content['suiteInfo']
    TestSuite(content['file_path']).saveSuite(content['file_content'])
    return HttpResponse('success')

@require_http_methods(['GET'])
def getFileTreeList(request):
    # filePath = request.get("filePath")
    (fileList, folderList) = getPathList()
    response = JsonResponse({'files': fileList, 'folders': folderList})
    return HttpResponse(response)

@require_http_methods(['POST'])
def saveRawFile(request):
    content = json.loads(request.body.decode('utf-8'))
    saveFile(content["filePath"], content["rawData"])
    response = JsonResponse({'fileContent': TestSuite(content["filePath"]).getSuiteAttributes()})
    return HttpResponse(response)

@require_http_methods(['GET'])
def getFileContent(request):
    filePath = request.GET.get("filePath")
    response = JsonResponse({'fileContent': TestSuite(filePath).getSuiteAttributes()})
    return HttpResponse(response)


def executeSuite(request):
    # suitePath = request.GET['suite_path']
    import subprocess, tempfile
    out_fd, out_path = \
        tempfile.mkstemp(prefix='webrfproc_', suffix='.txt',
                         text=True)
    out_file = open(out_path)
    command = ["D:\Setup\Python27\Scripts\\robot.bat", "D:\Setup\Python27\Scripts\LearnRF.robot"] #, ">", "S2020070901.log"]
    child1 = subprocess.Popen(command, shell=True, stdout=out_fd, stderr=subprocess.STDOUT)
    # 循环发送消息给前端页面
    print(out_path)
    respMsg = out_path
    return HttpResponse(out_path)

@accept_websocket
def showLog(request):
    print("enter into request")
    if not request.is_websocket():  # 判断是不是websocket连接
            message = request.GET['message']
            return HttpResponse(message)
    else:

            for message in request.websocket:
                print(message)
                message = message.decode('utf-8')  # 接收前端发来的数据
                if '#backup_all' in message:#这里根据web页面获取的值进行对应的操作
                    # import subprocess
                    # child1 = subprocess.Popen(["D:\Setup\Python27\Scripts\\robot.bat", "D:\Setup\Python27\Scripts\LearnRF.robot"], shell=True, stdout=subprocess.PIPE)
                    # # 循环发送消息给前端页面
                    # while True:
                    #      nextline = child1.stdout.readline().strip()  # 读取脚本输出内容
                    #      # print(nextline.strip())
                    #      request.websocket.send(nextline) # 发送消息到客户端
                    #      print(nextline)
                    #      # 判断消息为空时,退出循环
                    #      if not nextline:
                    #          request.websocket.send("END")
                    #          break
                    logPath = message.split('#backup_all:')[1]
                    logFile = open(logPath, "r")
                    while True:
                        where = logFile.tell()
                        line = logFile.readline()
                        if line:
                            request.websocket.send(line)
                        else:
                            import time
                            time.sleep(1)
                            logFile.seek(where)

                    # while True:
                    #     line = logFile.readline()
                    #     print(line)
                    #     request.websocket.send(line)
                    #     if not line:
                    #         # time.sleep(0.1)
                    #         # continue
                    #         break
                    #     yield line
                elif message == 'END':
                    request.websocket.close()
                else:
                    request.websocket.send('请检查配置!!!'.encode('utf-8'))

