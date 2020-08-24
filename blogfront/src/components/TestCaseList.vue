<template>
  <el-container style="border: 1px solid #eee">
          <el-main>
        <search-bar @onSearch="searchResult" ref="searchBar"></search-bar>
        <el-button style="float:right;margin: 10px 20px" icon="el-icon-plus" size=medium type="primary" round @click="createNewTest">创建测试用例</el-button>
        <el-table
          :data="testCases"
          style="width: 100%">
          <el-table-column
            prop="id"
            label="ID"
            width="180">
          </el-table-column>
          <el-table-column
            prop="name"
            label="用例名称"
            width="180">
          </el-table-column>
          <el-table-column
            prop="abstract"
            label="用例摘要"
            width="180">
          </el-table-column>
          <el-table-column
            prop="created_time"
            label="创建时间">
          </el-table-column>
          <el-table-column
            prop="execute_status.name"
            label="当前状态">
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="viewTestCase(scope.row)"
                size="small">
                查看
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
            <test-case-editor ref="testCaseEditor" @onSubmit="loadTestCases"></test-case-editor>
            <test-case-detail ref="testCaseDetail" @onSubmit="loadTestCases"></test-case-detail>
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
      </el-main>
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
export default {
  name: 'TestCaseList',
  components: {TestCaseEditor, TestCaseDetail, SearchBar},
  data () {
    return {
      testCases: [],
      currentPage: 1,
      total: 0,
      pageSize: 5
    }
  },
  mounted: function () {
    this.loadTestCases()
  },
  methods: {
    loadTestCases () {
      var _this = this
      this.$axios.get('/show_testcases/?page=1&page_size=' + _this.pageSize).then(resp => {
        if (resp && resp.status === 200) {
          _this.testCases = resp.data.results
          _this.total = resp.data.count
        }
      })
    },
    createNewTest: function () {
      this.$refs.testCaseEditor.dialogVisible = true
      this.$refs.testCaseEditor.form = {
        name: '',
        createdTime: '',
        abstract: '',
        execteStatus: {
          id: '',
          name: ''
        }
      }
    },
    getTestCaseTagsName: function (tags) {
      var tagsName = []
      var _this = this
      for (let tag of tags) {
        this.$axios.get('/show_tags/' + tag + '/').then(resp => {
          if (resp && resp.status === 200) {
            _this.tagName = resp.data.name
            tagsName.push(_this.tagName)
          }
        })
      }
      return tagsName
    },
    editTestCase: function (testCase) {
      // alert(testCase.tags)
      this.$refs.testCaseEditor.dialogVisible = true
      this.$refs.testCaseEditor.form = {
        id: testCase.id,
        name: testCase.name,
        createdTime: testCase.created_time,
        abstract: testCase.abstract,
        execteStatus: {
          id: testCase.execute_status.id,
          name: testCase.execute_status.name
        },
        tags: testCase.tags
      }
    },
    viewTestCase: function (testCase) {
      this.$refs.testCaseDetail.dialogVisible = true
      this.$refs.testCaseDetail.form = {
        id: testCase.id,
        name: testCase.name,
        createdTime: testCase.created_time,
        abstract: testCase.abstract,
        execteStatus: {
          id: testCase.execute_status.id,
          name: testCase.execute_status.name
        },
        tags: this.getTestCaseTagsName(testCase.tags)
      }
    },
    deleteTestCase: function (id) {
      this.$confirm('此操作将永久删除该测试用例, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios.delete('/show_testcases/' + id + '/').then(resp => {
          if (resp && resp.status === 200) {
            this.loadTestCases()
          }
        })
      }
      ).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    searchResult () {
      var _this = this
      this.$axios
        .get('/show_testcases/?page_size=' + this.pageSize + '&' + this.handleFilterUrl({name: this.$refs.searchBar.testCaseName,
          tags: this.$refs.searchBar.searchTags
        })
        ).then(resp => {
          if (resp && resp.status === 200) {
            _this.testCases = resp.data.results
            _this.total = resp.data.count
          }
        })
    },
    handleFilterUrl ({name = '', ftime = '', ttime = '', tags = ['']} = {}) {
      var url = ''
      url = 'testcase_name=' + name + '&dtime_before=' + ftime + '&dtime_after=' + ttime
      if (tags.length === 0) {
        url += '&testcase_tag='
      } else {
        for (let tag of tags) {
          url += '&testcase_tag' + '=' + tag
        }
      }
      return url
    },
    handleCurrentChange (page) {
      var _this = this
      this.$axios.get('/show_testcases/', {
        params: {
          page: page,
          page_size: _this.pageSize
        }
      }).then(resp => {
        if (resp && resp.status === 200) {
          _this.testCases = resp.data.results
        }
      })
    }
  }
}
</script>
