import clonedeep from 'clonedeep'

export const generateSuiteFile = (suiteFileObj) => {
  var suiteContent = ''
  if (suiteFileObj.file_content.settings) {
    suiteContent += '*** Settings ***\n'
    suiteContent += suiteFileObj.file_content.settings.join('\n') + '\n'
  }
  if (suiteFileObj.file_content.variables) {
    suiteContent += '\n*** Variables ***\n'
    suiteContent += suiteFileObj.file_content.variables.join('\n') + '\n'
  }
  if (suiteFileObj.file_content.testcases) {
    suiteContent += '\n*** Test Cases ***\n'
    for (let index in suiteFileObj.file_content.testcases) {
      suiteContent += suiteFileObj.file_content.testcases[index].title + '\n'
      suiteContent += suiteFileObj.file_content.testcases[index].content.join('\n')
      suiteContent += '\n'
    }
  }
  if (suiteFileObj.file_content.keywords) {
    suiteContent += '\n*** Keywords ***\n'
    for (let index in suiteFileObj.file_content.keywords) {
      suiteContent += suiteFileObj.file_content.keywords[index].title + '\n'
      suiteContent += suiteFileObj.file_content.keywords[index].content.join('\n')
      suiteContent += '\n'
    }
  }
  return suiteContent
}
export const transferListToTableList = (testCases) => {
  const testCasesCloned = clonedeep(testCases)
  var testcase = {}
  var testcaseIndex
  for (testcaseIndex in testCasesCloned) {
    var contentDict = {}
    var contentDictList = []
    var itemIndex, item
    testcase = testCasesCloned[testcaseIndex]
    for (itemIndex in testcase.content) {
      item = testcase.content[itemIndex]
      let index = 1
      let itemList = item.split('    ')
      while (index < itemList.length) {
        contentDict[index] = itemList[index]
        index++
      }
      contentDictList.push(contentDict)
    }
    testcase.content = contentDictList
  }
  return testCasesCloned
}

export const transTestCaseList2TreeFormat = (testCases) => {
  const testCasesCloned = clonedeep(testCases)
  var testcase = {}
  var testcaseIndex
  for (testcaseIndex in testCasesCloned) {
    var contentDict = {}
    var contentDictList = []
    var itemIndex, item
    testcase = testCasesCloned[testcaseIndex]
    for (itemIndex in testcase.content) {
      item = testcase.content[itemIndex]
      let index = 1
      let itemList = item.split('    ')
      while (index < itemList.length) {
        contentDict[index] = itemList[index]
        index++
      }
      contentDictList.push(contentDict)
    }
    testcase.content = contentDictList
  }
  return testCasesCloned
}

export const handleTestCaseContent = (content) => {
  let itemIndex
  let parsedContent = []
  var item = ''
  for (itemIndex in content) {
    item = content[itemIndex]
    let itemList = item.split('    ')
    itemList.splice(0, 1)
    parsedContent.push(itemList)
  }
  if (parsedContent.length === 0) { parsedContent = [[]] }
  return parsedContent
}

export const putTestCase2Children = (type, content, parentObj) => {
  for (let index in content) {
    let item = {}
    item.name = content[index].title
    item.title = content[index].title
    item.label = content[index].title
    item.type = type
    if (type === 'testcases') {
      item.icon = 'el-icon-reading'
    } else if (type === 'keywords') {
      item.icon = 'el-icon-setting'
    }
    item.content = handleTestCaseContent(content[index].content)
    parentObj.children.push(item)
  }
}

export const handleSettings = (settings) => {
  var formatedSettings = []
  for (let index in settings) {
    formatedSettings.push(settings[index].split('    '))
  }
  if (formatedSettings.length === 0) { formatedSettings = [[]] }
  return formatedSettings
}

export const handleVariables = (variables) => {
  var formatedSettings = []
  for (let index in variables) {
    formatedSettings.push(variables[index].split('    '))
  }
  if (formatedSettings.length === 0) { formatedSettings = [[]] }
  return formatedSettings
}

export const putTestCaseIntoSuite = (fileObj) => {
  var extIndex = fileObj.file_path.lastIndexOf('.')
  var ext = fileObj.file_path.substring(extIndex, fileObj.file_path.length)
  if (ext === '.har') {
    return []
  }
  var fileObjCloned = clonedeep(fileObj)
  var fileContent = fileObjCloned.file_content
  fileObjCloned.children = []
  if (fileContent.settings) {
    fileObjCloned.children.push({
      'name': 'settings', 'label': 'settings', 'icon': 'el-icon-setting', 'type': 'settings', 'content': handleSettings(fileContent['settings'])})
  }
  if (fileContent.variables) {
    fileObjCloned.children.push({
      'name': 'variables',
      'label': 'variables',
      'icon': 'el-icon-key',
      'type': 'variables',
      'content': handleVariables(fileContent['variables'])
    })
  }
  putTestCase2Children('testcases', fileContent['testcases'], fileObjCloned)
  putTestCase2Children('keywords', fileContent['keywords'], fileObjCloned)
  return fileObjCloned.children
}
export const putFileInFolder = (folderList, fileList) => {
  const folderListCloned = clonedeep(folderList)
  const fileListCloned = clonedeep(fileList)
  return folderListCloned.map(folderItem => {
    const folderId = folderItem.id
    let index = fileListCloned.length
    while (--index >= 0) {
      const fileItem = fileListCloned[index]
      if (fileItem.folder_id === folderId) {
        const file = fileListCloned.splice(index, 1)[0]
        file.title = file.name
        file.label = file.name
        file.type = 'file'
        fileItem.icon = 'el-icon-notebook-2'
        file.children = putTestCaseIntoSuite(file)
        if (folderItem.children) folderItem.children.push(file)
        else folderItem.children = [file]
      }
    }
    folderItem.type = 'folder'
    folderItem.icon = 'el-icon-folder'
    return folderItem
  })
}

export const transferFolderToTree = folderList => {
  if (!folderList.length) return []
  const folderListCloned = clonedeep(folderList)
  const handle = id => {
    let arr = []
    folderListCloned.forEach(folder => {
      if (folder.folder_id === id) {
        const children = handle(folder.id)
        if (folder.children) folder.children = [].concat(folder.children, children)
        else folder.children = children
        folder.title = folder.name
        folder.label = folder.name
        arr.push(folder)
      }
    })
    return arr
  }
  return handle(0)
}

export const transferListToFormatedRFCase = data => {
  const content = []
  for (let index in data) {
    content.push('    ' + data[index].join('    '))
  }
  return content
}

export const transferListToFormatedRFSettings = data => {
  const content = []
  for (let index in data) {
    content.push(data[index].join('    '))
  }
  return content
}
