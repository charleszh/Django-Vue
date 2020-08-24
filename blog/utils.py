import os, time
from .TestSuite import TestSuite
path1 = "E:\WorkSpace\Test\\folderexa0"
path2="E:\WorkSpace\Products\\auto\RFAutoAPI\AutoTestCase"
def getCurrentTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def saveFile(path, data):
    fileObj = open(path, "w", encoding='UTF-8')
    fileObj.write(data)
    fileObj.close()


def getPathList(path=path2):
    folderIds = {}
    folderList = []
    fileList = []
    folderId = 0
    fileId = 10000
    folderIds[path] = folderId
    for root, dirs, files in os.walk(path):
        for name in files:
            if (os.path.splitext(name)[1] in ['.txt', '.robot', '.har']):
                filePath = root+'/'+name
                fileContent = TestSuite(filePath).getSuiteAttributes()
                fileList.append({'name': name, 'create_time': getCurrentTime(), 'folder_id': folderIds[root],
                                 'id': fileId, 'file_content': fileContent, 'file_path': filePath})
                fileId += 1
        for name in dirs:
            folderId += 1
            folderList.append({'name': os.path.basename(name), 'create_time': getCurrentTime(), 'folder_id': folderIds[root], 'id': folderId, 'file_path': root + '/' +name})
            pathName = os.path.join(root, name)
            folderIds[pathName] = folderId
    return (fileList, folderList)
