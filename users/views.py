from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import LoginForm
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

@require_http_methods(['POST'])
def login(request):
    form = LoginForm(request.POST)
    print(request.POST)
    if form.is_valid():
        print("valid request")
    username = form.cleaned_data['username']
    print('the username is : ', username)
    # password = form.cleaned_data['password']
    # content = json.loads(request.body.decode('utf-8'))
    # username = content['username']
    # password = content['password']
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse(JsonResponse({'message': 'success'}))
    else:
        return HttpResponse(JsonResponse({'message': 'fail'}))

@require_http_methods(['GET'])
def logout(request):
    auth.logout(request)
    return HttpResponse("退出登录成功")
