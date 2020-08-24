<template>
  <body id="poster">
  <el-form class="login_container" :model="loginForm" label-position="left" xml:lang="0px" @submit.native.prevent>
    <h3 class="login_title">系统登录</h3>
    <el-form-item>
      <el-input type="text" v-model="loginForm.username" auto-complete="off" placeholder="账号" clearable></el-input>
    </el-form-item>
    <el-form-item>
      <el-input type="password" v-model="loginForm.password" auto-complete="off" placeholder="密码" clearable show-password></el-input>
    </el-form-item>
    <el-form-item style="width: 100%">
      <el-button type="primary" native-type="submit" style="width:100%;background: #505458;border: none" v-on:click="login">登录</el-button>
    </el-form-item>
    <el-form-item style="width: 100%">
      <router-link type="primary"  style="font-style: oblique" to="register">还没有账号吗? 注册一个吧</router-link>
    </el-form-item>
  </el-form>
  </body>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      responseResult: []
    }
  },
  methods: {
    login () {
      // var _this = this
      var ret = ''
      for (let it in this.loginForm) { ret += encodeURIComponent(it) + '=' + encodeURIComponent(this.loginForm[it]) + '&' }
      ret = ret.slice(0, -1)
      this.$axios
        .post('/accounts/login/', ret, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        .then(successResponse => {
          console.log('133', successResponse)
          if (successResponse.status === 200) {
            // _this.$store.commit('login', _this.loginForm)
            var path = this.$route.query.redirect
            this.$router.replace({path: path === '/' || path === undefined ? '/index' : path})
          } else {
            this.$alert(successResponse.data.message)
          }
        })
        .catch(failResponse => {
        })
    }
  }
}
</script>
<style>
  .login_container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }

  .login_title {
    margin: 10px auto 40px auto;
    text-align: center;
    color: #505458;
  }

  #poster {
    background: url("../assets/login_background.jpg") no-repeat;
    background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position: fixed;
  }

  body{
    margin: 0px;
  }
</style>
