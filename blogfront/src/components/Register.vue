<template>
  <body id="paper">
  <el-form class="register-container" label-position="labelPosition" label-width="90px" v-loading="loading">
    <h3 class="register_title">用户注册</h3>
    <el-form-item label="账号">
      <el-input type="text" v-model="registerForm.username" auto-complete="off" placeholder="账号" clearable="true"></el-input>
    </el-form-item>
    <el-form-item label="请输入密码">
      <el-input type="password" v-model="registerForm.password" auto-complete="off" placeholder="密码" clearable="true" show-password></el-input>
    </el-form-item>
    <el-form-item label="请确认密码">
      <el-input type="password" v-model="registerForm.rePassword" auto-complete="off" placeholder="确认密码" clearable="true" show-password></el-input>
    </el-form-item>
    <el-form-item style="width: 100%">
      <el-button type="primary" style="width:100%;background: #505458;border: none" v-on:click="register">注册</el-button>
    </el-form-item>
    <el-form-item style="width: 100%">
      <router-link type="primary" style="font-style: oblique" to="login">登录试试吧</router-link>
    </el-form-item>
  </el-form>
  </body>
</template>
<script>
export default {
  name: 'register',
  data () {
    return {
      checked: true,
      registerForm: {
        username: '',
        password: '',
        rePassword: ''
      },
      loading: false
    }
  },
  methods: {
    register () {
      // eslint-disable-next-line no-unused-vars
      var _this = this
      console.log(this.$store.state)
      this.$axios
        .post('/register', {
          username: this.registerForm.username,
          password: this.registerForm.password
        })
        .then(resp => {
          if (resp.data.code === 200) {
            this.$alert('注册成功 ' + resp.data.data.username, '提示', {
              confirmButtonText: '确定'
            })
            _this.$router.replace('/login')
          } else {
            this.$alert(resp.data.message, '提示', {
              confirmButtonText: '确定'
            })
          }
        })
        .catch(failResponse => {
        })
    }
  }

}
</script>
<style>
  #paper {
    background:url("../assets/login_background.jpg") no-repeat;
    background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position: fixed;
  }
  body{
    margin: -5px 0px;
  }
  .register-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }
  .register_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }
</style>
