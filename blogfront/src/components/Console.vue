<template>
  <div>
  <el-container style="border: 1px solid #eee"
                title="展示执行日志"
                :visible.sync="consoleVisible"
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
</template>
<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  .el-aside {
    color: #333;
  }
</style>

<script>
export default {
  name: 'Console',
  inject: ['reload'],
  data () {
    return {
      consoleVisible: false,
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
        this.init()
        this.socket.send('#backup_all:' + logPath)
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
    height: 500px;
    width: 100%;
    float: left;
    background-color: black;
    overflow:scroll;
    margin-left: 10px;
  }
</style>
