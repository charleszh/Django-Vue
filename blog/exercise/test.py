import os, time
import threading

class A():
    def a(self):
        print("in class a")

class B():
    def b(self):
        print("in class B")
        A().a()


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(arg, obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()



# def getCurrentTime():
#     return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# path = "E:\WorkSpace\Products\\auto\RFAutoAPI\AutoTestCase"
# folderIds = {}
# folderList = []
# fileList = []
# key = "AutoTestCase"
# folderId = 0
# fileId = 10000
# folderIds[path] = folderId
# for root, dirs, files in os.walk(path):
#     for name in files:
#         fileList.append({'name': name, 'create_time': getCurrentTime(), 'folder_id': folderIds[root], 'id': fileId})
#         fileId += 1
#
#     for name in dirs:
#         folderId += 1
#         folderList.append({'name': os.path.basename(name), 'create_time': getCurrentTime(), 'folder_id': folderIds[root], 'id': folderId})
#         pathName = os.path.join(root, name)
#         folderIds[pathName] = folderId
#
# print(folderList)
# print(fileList)
