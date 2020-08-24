<template>
    <div>
      <el-button style="margin-left: 10px" size="medium" icon="el-icon-caret-right" type="primary" @click="send">执行</el-button>
      <el-button style="margin-left: 10px" size="medium" icon="el-icon-delete-solid" type="success" @click="clearLog">清空</el-button>
      <p style="text-align: left; margin-left:20px; font-weight: bold">脚本执行结果：</p>
      <div class="logBlock">
        <ul class="scrollBottom" style="text-align: left; font-size: small; background-color: black; color: lawngreen" v-for="(item, index) in msgDetails" :key="index">{{ msgDetails[index] }}</ul>
      </div>
    </div>
</template>

<script>
export default {
  name: 'ExecuteTestCase',
  data () {
    return {
      path: 'ws://127.0.0.1:8000/api/show_log/',
      socket: '',
      msgDetails: []
    }
  },
  mounted: function () {
    // 初始化
    this.init()
    // this.messages()
  },
  methods: {
    init () {
      if (typeof (WebSocket) === 'undefined') {
        alert('您的浏览器不支持socket')
      } else {
        this.socket = new WebSocket(this.path)
        this.socket.onopen = this.open
        this.socket.onerror = this.error
        this.socket.onmessage = this.getMessage
      }
    },
    open () {
      console.log('socket连接成功')
    },
    error () {
      console.log('连接错误')
    },
    getMessage (msg) {
      console.log(msg.data)
      this.msgDetails.push(msg.data)
    },
    send () {
      this.socket.send('#backup_all')
      console.log('send message: ' + '#backup_all')
    },
    close: function () {
      console.log('socket已经关闭')
    },
    destroyed () {
      this.socket.onclose = this.close
    },
    clearLog () {
      this.msgDetails = ['']
    },
    scrollToBottom () {
      this.$nextTick(() => {
        let container = this.$el.querySelector('.logBlock')
        // container.scrollIntoView()
        container.scrollTop = container.scrollHeight
      }, 1000)
    }
  }
}
</script>
<style>
  .logBlock {
    height: 600px;
    width: 1000px;
    float: left;
    background-color: black;
    overflow:scroll;
    margin-left: 30px;
  }
</style>
