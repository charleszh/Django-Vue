<template>
  <div>
    <el-dialog
      title="修改角色信息"
      :visible.sync="dialogFormVisible"
      @close="clear">
      <el-form v-model="form" style="text-align: left" ref="dataForm">
        <el-form-item label="ID" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.id" autocomplete="off" placeholder="不加《》" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="角色名" :label-width="formLabelWidth" prop="username">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="角色描述" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name_zh" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="状态" :label-width="formLabelWidth"  prop="enabled">
          <el-switch v-model="form.enabled" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
        </el-form-item>
        <el-form-item label="功能配置" label-width="120px" prop="roles">
          <el-checkbox-group v-model="selectedPermissionsIds">
            <el-checkbox v-for="(permission,i) in permissions" :key="i" :label="permission.id">{{permission.desc_}}</el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="菜单配置" label-width="120px" prop="menus">
          <el-tree
            :data="menus"
            :props="props"
            show-checkbox
            :default-checked-keys="selectedMenusIds"
            node-key="id"
            ref="tree"></el-tree>
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
  inject: ['reload'],
  name: 'RoleEditForm',
  data () {
    return {
      dialogFormVisible: false,
      selectedPermissionsIds: [],
      selectedMenusIds: [],
      menus: [],
      permissions: [],
      form: {
        id: '',
        name: '',
        name_zh: '',
        enabled: true
      },
      props: {
        id: 'id',
        label: 'nameZh',
        children: 'children'
      },
      formLabelWidth: '120px'
    }
  },
  mounted: function () {
    this.permissions = this.loadPermissions()
    this.menus = this.loadMenus()
  },
  methods: {
    clear () {
      this.reload()
      this.form = {
        id: '',
        username: '',
        name: '',
        name_zh: '',
        enabled: false,
        selectedPermissionsIds: [],
        selectedMenusIds: []
      }
    },
    loadPermissions () {
      var _this = this
      this.$axios.get('/admin/permissions').then(resp => {
        if (resp && resp.status === 200) {
          _this.permissions = resp.data.data
        }
      })
    },
    loadMenus () {
      var _this = this
      this.$axios.get('/admin/role/menu').then(resp => {
        if (resp && resp.status === 200) {
          _this.menus = resp.data
        }
      })
    },
    checkMenus (menuIds) {
      alert(this.$refs.tree)
      if (this.$refs.tree) {
        alert('enter into refs')
        this.$refs.tree.setCheckedKeys(menuIds)
      }
    },
    onSubmit () {
      console.log(this.$refs.tree.getCheckedKeys())
      let _this = this
      let permissions = []
      for (let i = 0; i < _this.selectedPermissionsIds.length; i++) {
        for (let j = 0; j < _this.permissions.length; j++) {
          if (_this.selectedPermissionsIds[i] === _this.permissions[j].id) {
            permissions.push(_this.permissions[j])
          }
        }
      }
      this.$axios
        .post('/admin/role', {
          id: this.form.id,
          name: this.form.name,
          nameZh: this.form.name_zh,
          enabled: this.form.enabled,
          permissions: permissions
        }).then(resp => {
          if (resp && resp.status === 200) {
            this.dialogFormVisible = false
          }
        })
      console.log(this.$refs.tree.getCheckedKeys())
      this.$axios.put('/admin/role/menu?rid=' + this.form.id, {
        menusIds: this.$refs.tree.getCheckedKeys()
      }).then(resp => {
        if (resp && resp.status === 200) {
          this.$emit('onSubmit')
        }
      })
    }
  }
}
</script>

<style scoped>
</style>
