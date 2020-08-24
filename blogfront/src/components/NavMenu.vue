<template>
  <div>
  <el-menu
    :default-active="'/index'"
    class="el-navmenu"
    router
    mode="vertical"
    background-color="white"
    text-color="#222"
    active-text-color="red"
    :default-openeds="['0']">
    <template v-for="(item, i) in navList" :index="item.i">
      <template v-if="item.hasOwnProperty('children')">
      <el-submenu :key="i" :index="item.path" style="text-align: left">
        <span slot="title" style="font-size: 15px;">
          <i :class="item.icon"></i>
          {{item.navItem}}
        </span>
        <el-menu-item v-for="child in item.children" :key="child.path" :index="child.path">
          <i :class="child.icon"></i>
          {{child.navItem}}
        </el-menu-item>
      </el-submenu>
      </template>
      <template v-else>
        <el-menu-item :key="i" :index="item.path" style="text-align: left">
          <i :class="item.icon"></i>
          {{item.navItem}}
        </el-menu-item>
    </template>
    </template>
  </el-menu>
  </div>
</template>
<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      navList: [
        { path: '/index', navItem: '首页', icon: 'el-icon-s-home' },
        {path: '1',
          navItem: '测试用例',
          icon: 'el-icon-document',
          children: [
            {path: '/show_testcases', navItem: '搜索', icon: 'el-icon-search'},
            {path: '/show_pathtree', navItem: '新建', icon: 'el-icon-document-add'}
          ]
        },
        {path: '/execute_testcase', navItem: '执行用例', icon: 'el-icon-video-play'},
        {path: '/index', navItem: '个人中心', icon: 'el-icon-s-custom'}
      ]
    }
  },
  methods: {
  }
}
</script>

<style scoped>
  a{
    text-decoration: none;
  }

  span {
    pointer-events: none;
  }
  .el-icon-switch-button {
    cursor: pointer;
    outline:0;
  }
</style>
