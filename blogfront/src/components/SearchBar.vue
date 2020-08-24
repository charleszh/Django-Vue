<template>
  <div style="margin-left: 10px; margin-bottom: 30px;display: flex;justify-content: left;align-items: center;">
    测试用例名称：
    <el-input
      placeholder="请输入内容"
      size="medium"
      style="width: 300px;margin-right: 10px"
      v-model="testCaseName">
    </el-input>
    用例标签：
    <el-select
        v-model="searchTags"
        multiple
        filterable
        allow-create
        style="width: 300px"
        placeholder="请选择测试用例标签">
        <el-option
          v-for="item in tags"
          :key="item.id"
          :label="item.name"
          :value="item.id">
        </el-option>
      </el-select>
    <el-button style="margin-left: 10px" size="medium" type="primary" icon="el-icon-search" @click="searchClick">搜索</el-button>
    <el-button size="medium" type="primary" icon="el-icon-delete" @click="clearSearch">清空</el-button>
  </div>
</template>
<script>
export default {
  name: 'SearchBar',
  data () {
    return {
      testCaseName: '',
      searchTags: '',
      testCases: [],
      cardLoading: [],
      tags: []
    }
  },
  mounted () {
    this.loadTags()
  },
  methods: {
    loadTags () {
      var _this = this
      this.$axios.get('/show_tags/').then(resp => {
        if (resp && resp.status === 200) {
          _this.tags = resp.data.results
        }
      })
    },
    searchClick () {
      this.$emit('onSearch')
    },
    clearSearch () {
      this.testCaseName = ''
      this.searchTags = []
    }
  }
}
</script>
<style></style>
