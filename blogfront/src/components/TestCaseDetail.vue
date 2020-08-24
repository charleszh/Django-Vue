<template>
  <div>
    <el-dialog
      title="查看测试用例"
      :visible.sync="dialogVisible"
      :append-to-body="true">
      <el-form v-model="form" style="text-align: left" ref="dataForm">
        <el-form-item label="id" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.id" autocomplete="off" :disabled="true" placeholder="不加《》"></el-input>
        </el-form-item>
        <el-form-item label="用例名称" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name" autocomplete="off" :disabled="true" placeholder="不加《》"></el-input>
        </el-form-item>
        <el-form-item label="用例摘要" :label-width="formLabelWidth" prop="abstract">
          <el-input v-model="form.abstract" autocomplete="off" :disabled="true" placeholder="不加《》"></el-input>
        </el-form-item>
        <el-form-item label="创建时间" :label-width="formLabelWidth" prop="createdTime">
          <el-date-picker type="datetime" placeholder="选择日期" :disabled="true" v-model="form.createdTime" style="width: 100%;"></el-date-picker>
        </el-form-item>
        <el-form-item label="当前状态" :label-width="formLabelWidth" prop="cid">
          <el-input  v-model="form.execteStatus.name" autocomplete="off" :disabled="true" placeholder="不加《》"></el-input>
        </el-form-item>
        <el-form-item label="标签" :label-width="formLabelWidth" prop="cid">
          <el-select
            v-model="form.tags"
            multiple
            filterable
            disabled="true"
            allow-create
            placeholder="">
          </el-select>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'TestCaseDetail',
  data () {
    return {
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
  }
}
</script>
