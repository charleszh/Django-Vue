<template>
  <div>
    <user-edit-form @onSubmit="loadUsers()" ref="edit"></user-edit-form>
  <el-table
    ref="multipleTable"
    :data="userInfo"
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
      prop="username"
      label="用户名"
      width="120">
    </el-table-column>
    <el-table-column
      prop="name"
      label="真实姓名">
    </el-table-column>
    <el-table-column
      prop="phone"
      label="手机号">
    </el-table-column>
    <el-table-column
      prop="email"
      label="邮箱">
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
          @click="editUser(scope.row)"
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
import UserEditForm from './UserEditForm'
export default {
  name: 'UserProfile',
  components: { UserEditForm },
  data () {
    return {
      userInfo: [],
      selectedRolesIds: [],
      dialogFormVisible: false,
      roles: []
    }
  },
  mounted: function () {
    this.loadUsers()
    this.loadRoles()
  },
  methods: {
    loadUsers () {
      var _this = this
      this.$axios.get('/admin/user').then(resp => {
        if (resp && resp.status === 200) {
          _this.users = resp.data
          _this.userInfo = _this.users.data
        }
      })
    },
    loadRoles () {
      var _this = this
      this.$axios.get('/admin/role').then(resp => {
        if (resp && resp.status === 200) {
          _this.roles = resp.data.data
        }
      })
    },
    editUser: function (row) {
      this.$refs.edit.dialogFormVisible = true
      this.$refs.edit.form = {
        id: row.id,
        username: row.username,
        name: row.name,
        phone: row.phone,
        email: row.email,
        enabled: row.enabled,
        roles: this.roles
      }
      let roleIds = []
      for (let i = 0; i < row.roles.length; i++) {
        roleIds.push(row.roles[i].id)
      }
      this.$refs.edit.selectedRolesIds = roleIds
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
