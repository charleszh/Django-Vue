<template>
  <div>
    <session-list ref="sessionList" @onDisplay="displayLog"></session-list>
    <el-button style="margin-left: 10px" size="medium" icon="el-icon-caret-right" type="primary" @click="send">执行</el-button>
    <el-button style="margin-left: 10px" size="medium" icon="el-icon-delete-solid" type="success" @click="clearLog">清空</el-button>
    <el-button style="margin-left: 10px" size="medium" icon="el-icon-switch-button" type="warning" @click="closeSocket">停止</el-button>
    <el-button style="margin-left: 10px" size="medium" icon="el-icon-refresh-left" type="primary" @click="reopen">重新连接</el-button>
    <p style="text-align: left; margin-left:20px; font-weight: bold">脚本执行结果：</p>
    <div class="logBlock">
      <ul class="scrollBottom" style="text-align: left; font-size: small; background-color: black; color: lawngreen" v-for="(item, index) in msgDetails" :key="index">{{ msgDetails[index] }}</ul>
    </div>
  </div>
</template>

<script>
import SessionList from './SessionList'
export default {
  name: 'TestCaseExecution',
  components: {SessionList},
  data () {
    return {
      path: 'ws://127.0.0.1:8000/api/show_log/',
      socket: '',
      msgDetails: [],
      wsHeartFlag: false,
      wsRestart: false
    }
  },
  mounted: function () {
    // 初始化
    this.init()
  },
  methods: {
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
      this.send(logPath)
    },
    reopen () {
      if (this.socket) {
        console.log('socket connected!')
        this.socket.close()
        this.init()
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
        // this.socket.close()
        // this.wsHeartFlag = false
      }
    },
    send (logPath) {
      if (!this.wsRestart) {
        this.socket.send('#backup_all:' + logPath)
        console.log('send message: ' + '#backup_all')
        this.msgDetails.push('socket连接成功,正在执行......')
      } else {
        this.msgDetails.push('请先连接socket！！！')
      }
      this.scrollToBottom()
    },
    /* timeingHeart () {
      if (this.wsHeartFlag) {
        this.socket.send('121')
      }
      this.wsHeart = setTimeout(() => {
        this.timeingHeart()
      }, 100 * 1000)
    }, */
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
    height: 500px;
    width: 1000px;
    float: left;
    background-color: black;
    overflow:scroll;
    margin-left: 30px;
  }
</style>
