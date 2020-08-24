<template>
  <el-container style="border: 1px solid #eee">
    <el-main>
      <el-button style="float:right;margin: 10px 20px" icon="el-icon-plus" size=medium type="primary" round @click="createNewTest">创建测试集</el-button>
      <el-table
        :data="testSuites"
        style="width: 100%; align-content: center">
        <el-table-column
          prop="id"
          label="ID"
          width="90">
        </el-table-column>
        <el-table-column
          prop="name"
          label="用例集名称"
          width="180">
        </el-table-column>
        <el-table-column
          prop="abstract"
          label="用例集摘要"
          width="280">
        </el-table-column>
        <el-table-column
          prop="execute_status"
          label="当前状态"
          width="90">
        </el-table-column>
        <el-table-column  label="操作" header-align="center" align="center">
          <template slot-scope="scope">
            <el-button
              @click.native.prevent="viewTestCase(scope.row)"
              size="small">
              查看
            </el-button>
            <el-button
              @click.native.prevent="executeSuite(scope.row)"
              size="small">
              执行
            </el-button>
            <el-button
              @click.native.prevent="executeSuite(scope.row)"
              size="small">
              日志
            </el-button>
            <el-button
              size="mini"
              @click="editTestCase(scope.row)"
            >
              编辑
            </el-button>
            <el-button
              size="mini"
              type="danger"
              @click="deleteTestCase(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <br>
      <el-pagination
        background
        layout="total, prev, pager, next, jumper"
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="pageSize"
        :total="total">
      </el-pagination>
      <div>
        <el-container style="border: 1px solid #eee"
                      title="展示执行日志"
                      @close="clear">
          <el-main>
            <el-row justify="center">
              <el-col align="left"><span style="font-weight: bold">脚本执行日志：</span>
                <el-button  style="float:right" size="small" icon="el-icon-delete-solid" type="success" @click="clearLog">清空</el-button>
                <el-button  style="float:right; margin-right: 10px" size="small" icon="el-icon-switch-button" type="warning" @click="closeSocket">停止</el-button>
              </el-col>
            </el-row>
            <div class="logBlock">
              <ul class="scrollBottom" style="text-align: left; font-size: small; background-color: black; color: lawngreen" v-for="(item, index) in msgDetails" :key="index">{{ msgDetails[index] }}</ul>
            </div>
          </el-main>
        </el-container>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import Console from './Console'
export default {
  name: 'ExecutePage',
  components: {Console},
  data () {
    return {
      testSuites: [{'id': 1, 'name': 'zhq', 'abstract': 'Demo for execution', 'path': 'D:\\Setup\\Python27\\Scripts\\LearnRF.robot', 'created_time': '2020-07-09', 'execute_status': 'pass'},
        {'id': 2, 'name': 'zhq', 'abstract': 'Demo2 for execution', 'path': 'D:\\Setup\\Python27\\Scripts\\LearnRF.robot', 'created_time': '2020-07-09', 'execute_status': 'pass'}],
      currentPage: 1,
      total: 1,
      pageSize: 5,
      logPath: '',
      consoleVisible: false,
      path: 'ws://127.0.0.1:8000/api/show_log/',
      socket: '',
      msgDetails: [],
      wsHeartFlag: false,
      wsRestart: false
    }
  },
  mounted: function () {
    // this.loadTestCases()
    // this.init()
  },
  methods: {
    executeSuite (row) {
      this.init()
      this.$axios.post('/execute_suite/', {
        suite_path: 'D:\\Setup\\Python27\\Scripts\\\\robot.bat'
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$message({
            type: 'info',
            message: '开始执行'
          })
          this.send(resp.data)
        }
      })
    },
    loadTestCases () {
    },
    createNewTest: function () {
    },
    getTestCaseTagsName: function (tags) {
    },
    editTestCase: function (testCase) {
    },
    viewTestCase: function (testCase) {
    },
    deleteTestCase: function (id) {
    },
    searchResult () {
    },
    handleFilterUrl ({name = '', ftime = '', ttime = '', tags = ['']} = {}) {
    },
    handleCurrentChange (page) {
    },
    init () {
      console.log('enter into init')
      if (typeof (WebSocket) === 'undefined') {
        alert('您的浏览器不支持socket')
      } else {
        this.socket = new WebSocket(this.path)
        this.socket.onopen = this.open
        this.socket.onerror = this.error
        this.socket.onmessage = this.getMessage
        this.socket.onclose = this.close
      }
    },
    open () {
      console.log('socket is opened')
      this.msgDetails.push('Socket is connected!')
      this.scrollToBottom()
      this.wsHeartFlag = true
    },
    displayLog (logPath) {
      //  this.init()
      this.send(logPath)
    },
    reopen () {
      if (this.socket) {
        console.log('socket connected!')
        // this.socket.close()
        // this.init()
      } else {
        console.log('socket 需要重新连接')
        this.init()
      }
      this.scrollToBottom()
      this.wsRestart = false
    },
    error () {
      console.log('连接错误')
      // this.init()
    },
    getMessage (msg) {
      console.log(msg.data)
      this.msgDetails.push(msg.data)
      this.scrollToBottom()
      if (msg.data === 'END') {
        console.log('enter into end')
      }
    },
    send (logPath) {
      /* if (!this.wsRestart) {
        this.socket.send('#backup_all:' + logPath)
        console.log('send message: ' + '#backup_all')
        this.msgDetails.push('socket连接成功,正在执行......')
      } else {
        this.msgDetails.push('请先连接socket！！！')
        this.init()
        this.socket.send('#backup_all:' + logPath)
      } */
      this.socket.send('#backup_all:' + logPath)
      this.scrollToBottom()
    },
    close: function (e) {
      console.log('socket已经关闭', e)
      this.scrollToBottom()
    },
    closeSocket: function (e) {
      console.log('enter into close')
      this.msgDetails.push('The connection is closed......')
      this.scrollToBottom()
      this.socket.send('END')
      this.socket.onclose()
      this.socket.close()
      this.wsRestart = true
    },
    clearLog () {
      this.msgDetails = ['']
    },
    handleReload () {
      this.reload()
    },
    scrollToBottom () {
      this.$nextTick(() => {
        let container = this.$el.querySelector('.logBlock')
        container.scrollTop = container.scrollHeight
      })
    }
  },
  destroyed () {
    this.socket.onclose = this.close
  }
}
</script>
<style>
  .logBlock {
    height: 400px;
    width: 100%;
    float: left;
    background-color: black;
    overflow:scroll;
    margin-left: 10px;
  }
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  .el-aside {
    color: #333;
  }
</style>
