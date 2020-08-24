<template>
  <div>
    <role-edit-form @onSubmit="loadRoles()" ref="edit" :qqq="qqq"></role-edit-form>
    <el-table
      ref="multipleTable"
      :data="roles"
      tooltip-effect="dark"
      header-align="center"
      style="width: 100%"
      @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="55">
      </el-table-column>
      <el-table-column
        prop="id"
        label="id"
        width="120">
      </el-table-column>
      <el-table-column
        prop="name"
        label="角色名"
        width="150">
      </el-table-column>
      <el-table-column
        prop="nameZh"
        label="角色描述">
      </el-table-column>
      <el-table-column
        prop="enabled"
        label="状态">
        <template slot-scope="scope">
          <el-switch active-color="#13ce66" inactive-color="#ff4949" v-model="scope.row.enabled" @change=change(scope.$index,scope.row)>
          </el-switch>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="editRole(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            size="mini"
            type="danger"
            @click="deleteUser(scope.row)">删除</el-button>
        </template>
      </el-table-column>

    </el-table>
    <div style="margin-top: 20px">
      <el-button @click="toggleSelection([userInfo[1], userInfo[2]])">批量删除</el-button>
      <el-button @click="toggleSelection()">取消选择</el-button>
    </div>
  </div>
</template>

<script>
import RoleEditForm from './RoleEditorForm'
export default {
  name: 'UserRole',
  components: { RoleEditForm },
  data () {
    return {
      selectedPermissionsIds: [],
      selectedMenusIds: [],
      dialogFormVisible: false,
      roles: [],
      qqq: 'zxj'
    }
  },
  mounted: function () {
    this.loadRoles()
  },
  methods: {
    loadRoles () {
      var _this = this
      this.$axios.get('/admin/role').then(resp => {
        if (resp && resp.status === 200) {
          _this.roles = resp.data.data
        }
      })
    },
    editRole: function (row) {
      this.$refs.edit.dialogFormVisible = true
      this.$refs.edit.form = {
        id: row.id,
        name: row.name,
        name_zh: row.nameZh,
        enabled: row.enabled
      }
      let permissionIds = []
      for (let i = 0; i < row.permissions.length; i++) {
        permissionIds.push(row.permissions[i].id)
      }
      this.$refs.edit.selectedPermissionsIds = permissionIds
      console.log(row.menus)
      let menuIds = []
      for (let i = 0; i < row.menus.length; i++) {
        menuIds.push(row.menus[i].id)
        for (let j = 0; j < row.menus[i].children.length; j++) {
          menuIds.push(row.menus[i].children[j].id)
        }
      }
      // 判断树是否已经加载
      // 第一次打开对话框前树不存在，无法调用方法，需要通过设置 default-checked 正确选中菜单项
      this.$refs.edit.selectedMenusIds = menuIds
      console.log(menuIds)
    },
    deleteUser: function (user) {
      this.$confirm('此操作将永久删除该用户，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios
          .post('/admin/deleteUser', {
            id: user.id,
            username: user.username,
            name: user.name,
            phone: user.phone,
            email: user.email,
            enabled: user.enabled
          }).then(resp => {
            if (resp && resp.status === 200) {
              this.loadUsers()
            }
          })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
    }
  }
}
</script>
<style>
  .el-table td, .el-table th {
    text-align: center;
  }
</style>
