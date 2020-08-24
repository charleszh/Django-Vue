<template>
  <el-container>
    <el-header style="text-align: right; font-size: 15px">
      <el-dropdown>
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>个人信息</el-dropdown-item>
          <el-dropdown-item @click.native="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>Charles</span>
    </el-header>
    <el-container>
    <el-aside style="height: 100%;width: 250px;">
      <nav-menu></nav-menu>
    </el-aside>
    <el-main>
      <router-view/>
    </el-main>
      </el-container>
  </el-container>
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
import TestCaseEditor from './TestCaseEditor'
import TestCaseDetail from './TestCaseDetail'
import SearchBar from './SearchBar'
import NavMenu from './NavMenu'
export default {
  name: 'AtmsIndex',
  components: {NavMenu, TestCaseEditor, TestCaseDetail, SearchBar},
  data () {
    return {
    }
  },
  mounted: function () {
  },
  methods: {
    logout: function () {
      var _this = this
      console.log('enter into logout')
      this.$axios.get('/accounts/logout/').then(resp => {
        console.log(resp)
        if (resp.status === 200) {
          this.$message({
            message: resp.data,
            type: 'success'
          })
          // _this.$store.commit('logout')
          _this.$router.replace('/login')
        }
      })
    }
  }
}
</script>
