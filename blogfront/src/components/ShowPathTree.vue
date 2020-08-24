<template>
<div>
  <el-container>
    <el-aside>
      <el-scrollbar style="height:100%">
  <el-tree
    :data="folderTree"
     v-loading="loading"
    :default-expand-all="false"
    @node-click="handleSelect"
    :render-content="renderTree">
  </el-tree>
        </el-scrollbar>
    </el-aside>
  <el-container>
    <el-main>
      <div v-if="viewFileRaw === true">
        <el-scrollbar style="height:100%">
        <el-button style="float: left" type="primary" size="mini" @click="saveRawFile">save</el-button>
        <el-input
          v-model="currentFileContent"
          type="textarea"
          autosize
          placeholder="文件内容">
        </el-input>
          </el-scrollbar>
      </div>
      <div :hidden="hiddenFlag">
      <span v-if="currentObjType === 'testcases'" style="float: left; color: green">Test Case:{{currentTestCaseTitle}}</span>
        <span v-if="currentObjType === 'settings'" style="float: left; color: goldenrod">Settings:</span>
        <span v-if="currentObjType === 'variables'" style="float: left; color: darkseagreen" >Variable:</span>
        <span v-if="currentObjType === 'keywords'" style="float: left; color: green" >Keyword:{{currentTestCaseTitle}}</span>
        <show-test-case-content :content="testCaseContent" ref="testcaseTable" @viewUpdatedRaw="viewUpdatedRaw" @submit="saveTestCase"></show-test-case-content>
      </div>
    </el-main>
  </el-container>
  </el-container>

</div>
</template>

<script>
import ShowTestCaseContent from './ShowTestCaseContent'
import { putTestCaseIntoSuite, putFileInFolder, transferFolderToTree, transferListToFormatedRFCase, transferListToFormatedRFSettings, generateSuiteFile } from '../../lib/utils'
export default {
  name: 'ShowPathTree',
  components: { ShowTestCaseContent },
  data () {
    return {
      folderList: [],
      fileList: [],
      folderTree: [],
      fileContent: [],
      settings: [],
      testCases: [],
      testCaseContent: [[]],
      currentFileContent: '',
      currentTestCase: {},
      currentTestCaseTitle: '',
      currentObjType: '',
      currentNode: '',
      hiddenFlag: true,
      viewFileRaw: false
    }
  },
  mounted () {
    this.getPathTree()
  },
  methods: {
    saveRawFile () {
      let modifiedContent = ''
      this.$axios.post('/saveRawFile/', {
        rawData: this.currentFileContent,
        filePath: this.currentTestSuite.file_path
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$message({
            type: 'info',
            message: '已保存成功'
          })
          modifiedContent = resp.data.fileContent
          this.currentTestSuite.file_content = modifiedContent
          this.currentNode.parent.data.file_content = modifiedContent
          let children = putTestCaseIntoSuite(this.currentTestSuite)
          this.currentTestSuite.children = children
          this.currentNode.parent.data.children = children
        }
      })
    },
    saveTestCase (data) {
      this.updateCurrentData(data)
      this.$axios.post('/saveSuiteFile/', {
        suiteInfo: this.currentTestSuite
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$message({
            type: 'info',
            message: '已保存成功'
          })
        }
      }
      )
    },
    handleSelect (data, node, obj) {
      this.currentNode = node
      this.viewFileRaw = false
      this.hiddenFlag = true
      this.currentNode = node
      this.currentTestSuite = node.parent.data
      this.currentObjType = node.data.type
      if (this.currentObjType === 'file') {
        this.currentTestSuite = node.data
      }
      if (this.currentObjType === 'testcases' || this.currentObjType === 'keywords') {
        this.hiddenFlag = false
        this.currentTestCaseTitle = node.data.title
        this.testCaseContent = node.data.content
      } else if (this.currentObjType === 'settings') {
        this.hiddenFlag = false
        this.currentTestCaseTitle = 'settings'
        this.testCaseContent = node.data.content
      } else if (this.currentObjType === 'variables') {
        this.hiddenFlag = false
        this.currentTestCaseTitle = 'variables'
        this.testCaseContent = node.data.content
      } else {
        this.testCaseContent = [[]]
      }
      /* if (this.currentObjType === 'file') {
        this.showRaw()
      } */
    },
    viewUpdatedRaw (data) {
      this.updateCurrentData(data)
      this.hiddenFlag = true
      this.viewFileRaw = true
      this.currentFileContent = generateSuiteFile(this.currentTestSuite)
    },
    updateCurrentData (data) {
      if (this.currentObjType === 'testcases') {
        var testCases = this.currentTestSuite.file_content.testcases
        for (let index in testCases) {
          if (testCases[index].title === this.currentTestCaseTitle) {
            testCases[index].content = transferListToFormatedRFCase(data)
            this.currentTestSuite.children[index].content = data
            break
          }
        }
        this.currentTestSuite.file_content.testcases = testCases
      }
      if (this.currentObjType === 'keywords') {
        var keywords = this.currentTestSuite.file_content.keywords
        for (let index in keywords) {
          if (keywords[index].title === this.currentTestCaseTitle) {
            keywords[index].content = transferListToFormatedRFCase(data)
            this.currentTestSuite.children[index].content = data
            break
          }
        }
        this.currentTestSuite.file_content.keywords = keywords
      }
      if (this.currentObjType === 'settings') {
        var updateSettings = transferListToFormatedRFSettings(data)
        for (let item in this.currentTestSuite.children) {
          if (this.currentTestSuite.children[item].type === 'settings') {
            this.currentTestSuite.children[item].content = data
            break
          }
        }
        this.currentTestSuite.file_content.settings = updateSettings
      }
      if (this.currentObjType === 'variables') {
        var updateVariables = transferListToFormatedRFSettings(data)
        for (let item in this.currentTestSuite.children) {
          if (this.currentTestSuite.children[item].type === 'variables') {
            this.currentTestSuite.children[item].content = data
            break
          }
        }
        this.currentTestSuite.file_content.variables = updateVariables
      }
    },
    showRaw () {
      this.hiddenFlag = true
      this.viewFileRaw = true
      this.currentFileContent = generateSuiteFile(this.currentTestSuite)
    },
    getPathTree () {
      this.$axios.get('/getFileTreeList/').then(resp => {
        if (resp && resp.status === 200) {
          const resps = JSON.parse(JSON.stringify(resp))
          this.fileList = resps.data.files
          this.folderList = resps.data.folders
          this.folderTree = transferFolderToTree(putFileInFolder(this.folderList, this.fileList))
        }
      })
    },
    renderTree (h, {node, data, store}) {
      return (
        <div class="treeItem">
          <i class={data.icon} style="margin-right:5px; color: yellowgreen; font-weight: bold"></i>
          {data.label}
        </div>
      )
    }
  }
}
</script>

<style>
.treeItem {
  display: inline-block;
  width: ~"calc(100% - 50px)";
  color: black;
  height: 60px;
  line-height: 60px;
}
.el-icon-folder {
  }
.el-scrollbar__wrap {
  overflow-x: hidden;
  height: 800px;
}
</style>
