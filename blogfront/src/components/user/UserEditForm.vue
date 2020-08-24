<template>
  <div>
  <el-dialog
      title="修改用户信息"
      :visible.sync="dialogFormVisible"
      @close="clear">
      <el-form v-model="form" style="text-align: left" ref="dataForm">
        <el-form-item label="ID" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.id" autocomplete="off" placeholder="不加《》" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
          <el-input v-model="form.username" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="真实姓名" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="手机号" :label-width="formLabelWidth" prop="phone">
          <el-input v-model="form.phone" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" :label-width="formLabelWidth" prop="email">
          <el-input v-model="form.email" autocomplete="off" placeholder="图片 URL"></el-input>
        </el-form-item>
        <el-form-item label="状态" :label-width="formLabelWidth"  prop="enabled">
          <el-switch v-model="form.enabled" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
        </el-form-item>
        <el-form-item label="角色分配" label-width="120px" prop="roles">
          <el-checkbox-group v-model="selectedRolesIds">
            <el-checkbox v-for="(role,i) in form.roles" :key="i" :label="role.id">{{role.nameZh}}</el-checkbox>
          </el-checkbox-group>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit">确 定</el-button>
      </div>
 </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'UserEditForm',
  data () {
    return {
      dialogFormVisible: false,
      selectedRolesIds: [],
      form: {
        id: '',
        username: '',
        name: '',
        phone: '',
        email: '',
        enabled: true,
        roles: []
      },
      formLabelWidth: '120px'
    }
  },
  methods: {
    clear () {
      this.form = {
        id: '',
        title: '',
        author: '',
        date: '',
        press: '',
        cover: '',
        abs: '',
        category: {
          id: '',
          name: ''
        }
      }
    },
    onSubmit () {
      let _this = this
      let roles = []
      for (let i = 0; i < _this.selectedRolesIds.length; i++) {
        for (let j = 0; j < _this.form.roles.length; j++) {
          if (_this.selectedRolesIds[i] === _this.form.roles[j].id) {
            roles.push(_this.form.roles[j])
          }
        }
      }
      this.$axios
        .post('/admin/user', {
          id: this.form.id,
          username: this.form.username,
          name: this.form.name,
          phone: this.form.phone,
          email: this.form.email,
          enabled: this.form.enabled,
          roles: roles
        }).then(resp => {
          if (resp && resp.status === 200) {
            this.dialogFormVisible = false
            this.$emit('onSubmit')
          }
        })
    }
  }
}
</script>

<style scoped>
</style>
