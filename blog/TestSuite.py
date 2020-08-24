import os

testCaseFlag = "*** Test Cases ***"
settingsFlag = "*** Settings ***"
variablesFlag = "*** Variables ***"
keywordsFlag = "*** Keywords ***"

class TestSuite():
    def __init__(self, path):
        self.suitePath = path
        self.suiteFileContent = self.readSuite(path)
        self.settings = []
        self.testCases = []
        self.variables = []
        self.keywords = []
        self.suiteContentFlag = {"testcases": {"fileSepFlag": "*** Test Cases ***", "fileObjFlag": "test_cases"},
                                 "settings": {"fileSepFlag": "*** Settings ***", "fileObjFlag": "settings"},
                                 "variables": {"fileSepFlag": "*** Variables ***", "fileObjFlag": "variables"},
                                 "keywords": {"fileSepFlag": "*** Keywords ***", "fileObjFlag": "keywords"}}
        self.parseSuiteFile()

    def __str__(self):
        return os.path.basename(self.suitePath)

    def getSuiteAttributes(self):
        return {'settings': self.settings, 'testcases': self.testCases, 'variables': self.variables,
                'keywords': self.keywords}

    def readSuite(self, path):
        fileObj = open(path, "r", encoding='UTF-8')
        # fileContent = []
        fileContent = [line.rstrip() for line in fileObj]
        fileObj.close()
        return fileContent

    def getTypeContent(self, type, content):
        typeContent = []
        for item in content:
            if item.type == type:
                typeContent.append(map(lambda x: '    '+x, item))
        return typeContent

    def saveSuite(self, content):
        fileObj = open(self.suitePath, "w", encoding='UTF-8')
        if 'settings' in content:
            self.writeContentPart('settings', fileObj, content['settings'])
        if 'variables' in content:
            self.writeContentPart('variables', fileObj, content['variables'])
        if 'testcases' in content:
            self.writeContentPart('testcases', fileObj, content['testcases'])
        if 'keywords' in content:
            self.writeContentPart('keywords', fileObj, content['keywords'])
        fileObj.close()

    def writeContentPart(self, type, fileObj, contentPart):
        fileObj.writelines([self.suiteContentFlag[type]["fileSepFlag"]+"\n"])
        if type == 'variables' or type == 'settings':
            fileObj.writelines(map(lambda x: x+'\n', contentPart))
            fileObj.writelines(['\n'])
        else:
            for item in contentPart:
                fileObj.writelines(item['title']+'\n')
                fileObj.writelines(map(lambda x: x+'\n', item['content']))
                fileObj.writelines(['\n'])

    def parseSuiteFile(self):
        self.testCases = self.getSuitePart('testcases')
        self.settings = self.getSuitePart('settings')
        self.variables = self.getSuitePart('variables')
        self.keywords = self.getSuitePart('keywords')

    def getSuitePart(self, type):
        partContent = self.suiteFileContent
        partContentFlag = self.suiteContentFlag[type]['fileSepFlag']
        if partContentFlag not in partContent:
            return
        index = partContent.index(partContentFlag)
        if index >= 0 and len(partContent) > index+1:
            items = partContent[index+1:]
            if type == 'testcases' and self.suiteContentFlag['keywords']['fileSepFlag'] in partContent:
                endIndex = partContent.index(self.suiteContentFlag['keywords']['fileSepFlag'])
                items = partContent[index+1:endIndex]
            results = []
            if type == 'settings' or type == 'variables':
                for item in items:
                    if len(item) == 0:
                        break
                    results.append(item)
                return results
            itemNum = 0
            results.append({'title': items[0], 'content': []})
            for item in items[1:]:
                if item.startswith('    '):
                    results[itemNum]['content'].append(item)
                elif len(item) == 0:
                    continue
                else:
                    itemNum += 1
                    results.append({'title': item, 'content': []})
            return results
        else:
            return []

    def getAllTestCases(self):
        testCaseContent = self.suiteFileContent
        if testCaseFlag not in testCaseContent:
            return
        index = testCaseContent.index(testCaseFlag)
        if index >= 0:
            testCases = testCaseContent[index+1:]
            if keywordsFlag in testCaseContent:
                endIndex = testCaseContent.index(keywordsFlag)
                testCases = testCaseContent[index+1:endIndex]
            caseNum = 0
            self.testCases.append({'title': testCases[0], 'content': []})
            for item in testCases[1:]:
                if item.startswith('    '):
                    self.testCases[caseNum]['content'].append(item)
                elif len(item) == 0:
                    continue
                else:
                    caseNum += 1
                    self.testCases.append({'title': item, 'content': []})

    def getSettings(self):
        settingsContent = self.suiteFileContent
        if settingsFlag in settingsContent:
            index = settingsContent.index(settingsFlag)
            settings = settingsContent[index+1:]
            for item in settings:
                if len(item) == 0:
                    break
                else:
                    self.settings.append(item)
        else:
            self.settings = []



