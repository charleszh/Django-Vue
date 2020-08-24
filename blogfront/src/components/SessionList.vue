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
      <console v-if="consoleVisible" ref="consoleWindow"></console>
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
import Console from './Console'
export default {
  name: 'TestCaseList',
  components: {Console},
  provide: function () {
    return {
      reload: this.reload
    }
  },
  data () {
    return {
      testSuites: [{'id': 1, 'name': 'zhq', 'abstract': 'Demo for execution', 'path': 'D:\\Setup\\Python27\\Scripts\\LearnRF.robot', 'created_time': '2020-07-09', 'execute_status': 'pass'},
        {'id': 2, 'name': 'zhq', 'abstract': 'Demo2 for execution', 'path': 'D:\\Setup\\Python27\\Scripts\\LearnRF.robot', 'created_time': '2020-07-09', 'execute_status': 'pass'}],
      currentPage: 1,
      total: 1,
      pageSize: 5,
      logPath: '',
      consoleVisible: false
    }
  },
  mounted: function () {
    // this.loadTestCases()
  },
  methods: {
    reload () {
      this.consoleVisible = false
      this.$nextTick(function () {
        this.consoleVisible = true
      })
    },
    executeSuite (row) {
      if (this.consoleVisible) {
        console.log('enter into reload')
        this.$refs.consoleWindow.handleReload()
      }
      this.consoleVisible = true
      // this.$refs.consoleWindow.reopen()
      this.$axios.post('/execute_suite/', {
        suite_path: 'D:\\Setup\\Python27\\Scripts\\\\robot.bat'
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$message({
            type: 'info',
            message: '开始执行'
          })
          // this.$refs.consoleWindow.init()
          this.$refs.consoleWindow.displayLog(resp.data)
          // this.$emit('onDisplay', resp.data)
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
    }
  }
}
</script>
