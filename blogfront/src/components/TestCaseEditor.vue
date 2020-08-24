<template>
  <div>
    <el-dialog
      title="添加/修改测试用例"
      :visible.sync="dialogVisible"
      :append-to-body="true">
      <el-form v-model="form" style="text-align: left" ref="dataForm">
        <el-form-item label="id" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.id" :disabled="true" autocomplete="off" placeholder="不加《》"></el-input>
        </el-form-item>
      <el-form-item label="用例名称" :label-width="formLabelWidth" prop="name">
        <el-input v-model="form.name" autocomplete="off" placeholder="不加《》"></el-input>
      </el-form-item>
        <el-form-item label="用例摘要" :label-width="formLabelWidth" prop="abstract">
          <el-input v-model="form.abstract" autocomplete="off" placeholder="不加《》"></el-input>
        </el-form-item>
      <el-form-item label="创建时间" :label-width="formLabelWidth" prop="createdTime">
        <el-date-picker type="datetime" placeholder="选择日期" v-model="form.createdTime" style="width: 100%;"></el-date-picker>
      </el-form-item>
      <el-form-item label="当前状态" :label-width="formLabelWidth" prop="cid">
        <el-select v-model="form.execteStatus.name" placeholder="请选择分类">
          <el-option label="Pass" value="Pass"></el-option>
          <el-option label="Fail" value="Fail"></el-option>
          <el-option label="NA" value="NA"></el-option>
        </el-select>
      </el-form-item>
        <el-form-item label="标签" :label-width="formLabelWidth" prop="cid">
          <el-select
            v-model="form.tags"
            multiple
            filterable
            allow-create
            placeholder="请选择测试用例标签">
            <el-option
              v-for="item in tags"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveTestCase">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'TestCaseEditor',
  data () {
    return {
      tags: [],
      dialogVisible: false,
      form: {
        id: '',
        name: '',
        author: '',
        createdTime: '',
        abstract: '',
        executeStatus: {
          id: '',
          name: ''
        }
      },
      formLabelWidth: '120px'
    }
  },
  mounted () {
    this.loadTags()
  },
  methods: {
    init: function (test) {
      this.form.id = test.id
    },
    loadTags () {
      var _this = this
      this.$axios.get('/show_tags/').then(resp => {
        if (resp && resp.status === 200) {
          _this.tags = resp.data.results
        }
      })
    },
    saveTestCase () {
      this.$confirm('是否保存并提交用例?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        if (this.form.id) {
          this.$axios
            .put('/show_testcases/' + this.form.id + '/', {
              id: this.form.id,
              name: this.form.name,
              author: 1,
              created_time: this.form.createdTime,
              modified_time: this.form.createdTime,
              abstract: this.form.abstract,
              tags: this.form.tags,
              execute_status: {
                name: this.form.execteStatus.name
              }
            }).then(resp => {
              if (resp && resp.status === 200) {
                this.$message({
                  type: 'info',
                  message: '已保存成功'
                })
                alert(resp)
                this.dialogVisible = false
              }
            })
        } else {
          this.$axios
            .post('/show_testcases/', {
              name: this.form.name,
              author: 1,
              created_time: this.form.createdTime,
              modified_time: this.form.createdTime,
              abstract: this.form.abstract,
              tags: this.form.tags,
              execute_status: {
                name: this.form.execteStatus.name
              }
            }).then(resp => {
              if (resp && resp.status === 201) {
                this.$message({
                  type: 'info',
                  message: '已保存成功'
                })
                this.dialogVisible = false
              }
            })
        }
      }
      ).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消创建'
        })
      })
    },
    uploadImg () {
      this.article.articleCover = this.$refs.imgUpload.url
    }
  }
}
</script>
