<template>
  <div id="hot-preview">
    <!--<span>{{ content }}</span>-->
    <div style="">
    <el-row>
      <el-button type="success" size="small" @click="viewRaw">raw</el-button>
    <el-button type="primary" size="small" @click="testFunc">保存</el-button>
    <el-button type="success" size="small">执行</el-button>
    </el-row>
    </div>
    <HotTable :root="root" ref="testHot" :settings="hotSettings" style="text-align: left"></HotTable>
  </div>
</template>

<script>
import { HotTable } from '@handsontable/vue'
import '../../node_modules/handsontable/dist/handsontable.full.css'
// import Handsontable from 'handsontable-pro'

export default {
  name: 'ShowTestCaseContent',
  props: ['content'],
  data: function () {
    return {
      root: 'test-hot',
      hotSettings: {
        data: this.content, // this.content,
        // colHeaders: true, */
        startRows: 11, // 行列范围
        startCols: 6,
        minRows: 5, // 最小行列
        minCols: 5,
        maxRows: 20, // 最大行列
        maxCols: 20,
        colWidths: '10px',
        rowHeaders: true, // 行表头，可以使布尔值（行序号），可以使字符串（左侧行表头相同显示内容，可以解析html），也可以是数组（左侧行表头单独显示内容）。
        // colHeaders: [ '选择', '题目', 'A选项', 'B选项', 'C选项', 'D选项', '答案' ], // 自定义列表头or 布尔值
        colHeaders: true,
        minSpareCols: 1, // 列留白
        minSpareRows: 1, // 行留白
        // currentRowClassName: 'currentRow', //为选中行添加类名，可以更改样式
        // currentColClassName: 'currentCol',//为选中列添加类名
        autoWrapRow: true, // 自动换行
        // hiddenColumns: { columns: [0] },
        contextMenu: {
          items: {
            'row_above': {
              name: '上方插入一行'
            },
            'row_below': {
              name: '下方插入一行'
            },
            'col_left': {
              name: '左方插入列'
            },
            'col_right': {
              name: '右方插入列'
            },
            'hsep1': '---------', // 提供分隔线
            'remove_row': {
              name: '删除行'
            },
            'remove_col': {
              name: '删除列'
            },
            'make_read_only': {
              name: '只读'
            },
            'borders': {
              name: '表格线'
            },
            'copy': {
              name: '复制'
            },
            'cut': {
              name: '剪切'
            },
            'commentsAddEdit': {
              name: '添加备注'
            },
            'commentsRemove': {
              name: '取消备注'
            },
            'freeze_column': {
              name: '固定列'
            },
            'unfreeze_column': {
              name: '取消列固定'
            },
            'hsep2': '---------'
          }
        },
        manualColumnFreeze: true, // 手动固定列  ?
        manualColumnMove: true, // 手动移动列
        manualRowMove: true, // 手动移动行
        manualColumnResize: true, // 手工更改列距
        manualRowResize: true, // 手动更改行距
        comments: true, // 添加注释  ?
        customBorders: [], // 添加边框
        columnSorting: false, // 排序
        stretchH: 'all', // 根据宽度横向扩展，last:只扩展最后一列，none：默认不扩展
        fillHandle: true, // 选中拖拽复制 possible values: true, false, "horizontal", "vertical"
        fixedColumnsLeft: 2, // 固定左边列数
        fixedRowsTop: 2, // 固定上边列数
        mergeCells: [ // 合并
          // {row: 1, col: 1, rowspan: 3, colspan: 3},  //指定合并，从（1,1）开始行3列3合并成一格
          // {row: 3, col: 4, rowspan: 2, colspan: 2}
        ],
        className: 'htLeft',
        licenseKey: 'non-commercial-and-evaluation'
        /* afterChange: () => {
          if (this.hotRef) {
            this.$store.commit('updateData', this.hotRef.getSourceData())
          }
        } */
      }
    }
  },
  watch: {
    content: function (val) {
      this.hotSettings.data = val
    }
  },
  methods: {
    testFunc: function () {
      // this.$refs.hotTable.table就是当前的表格的对象
      const hotInstance = this.$refs.testHot.hotInstance
      console.log(hotInstance.getData())
      const modifiedData = hotInstance.getData()
      this.$emit('submit', modifiedData)
    },

    viewRaw: function () {
      const hotInstance = this.$refs.testHot.hotInstance
      console.log(hotInstance.getData())
      const modifiedData = hotInstance.getData()
      this.$emit('viewUpdatedRaw', modifiedData)
    }
  },
  components: {
    HotTable
  }
}
</script>
