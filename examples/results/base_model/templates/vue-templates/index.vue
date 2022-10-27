<template>

  <div class="container">
    <!--    高级筛选-->
    <search ref="search" v-on:fresh="fresh"></search>
    <!--    查询结果-->
    <el-card class="box-card margin-space">
      <div slot="header">
        <span>查询结果</span>
      </div>
      <!--      筛选表单-->
      <el-table
        :data="table_data"
        style="width: 100%; margin:0px 0px 20px 0px"
        :default-sort="{prop: 'create_time', order: 'descending'}"
      >
        <el-table-column
          type="index"
          label="序号"
          fixed="left"
          align="center"
          width="50"
        />
        <el-table-column
              label="姓名"
              align="center"
              prop="name">
            </el-table-column>
        <el-table-column
              label="性别"
              align="center"
              prop="sex">
            </el-table-column>
        <el-table-column
              label="角色"
              align="center"
              prop="role_id">
            </el-table-column>
        
        <el-table-column label="操作" fixed="right" width="150">
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="primary"
              @click="handle_update(scope.row)"
            >编辑</el-button>
            <el-button
              size="mini"
              type="danger"
              @click="handle_delete(scope.row)"
            >删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        style="float:left;margin-bottom:20px"
        :current-page="page_index"
        :page-sizes="page_sizes"
        :page-size="page_size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handle_size_change"
        @current-change="fresh"
      />
      <div style="float: right;margin-bottom:20px;margin-right:40px">
        <el-button
          type="primary"
          @click="handle_add"
        >新增用户管理管理</el-button>
      </div>
    </el-card>

    <add ref="add" v-on:fresh="fresh"></add>
    <update ref="update" v-on:fresh="fresh"></update>

  </div>
</template>

<script>
  import {
    query_user,delete_user
  } from "./api_result";
  import search from "./search";
  import add from "./add";
  import update from "./update";
  export default {
    name: 'user',
    components: {search,add,update},
    data() {
      return {
        page_index:1,
        page_sizes:[10, 15, 20, 25],
        page_size:10,
        total:0,
        table_data: [],
      }
    },
    computed: {
      my_headers(){
        return {"X-Token":this.$store.state.user.token}
      },
    },
    // 当组件被创建便获取初始化数据
    created(){
      this.fresh()
    },
    methods: {
      // 查询数据
      get_query_params(){
        let query = {};
        if (this.$refs.search){
          query = this.$refs.search.get_search_params();
        }
        return Object.assign(query,{"page_size":this.page_size,"page_index":this.page_index});
      },
      fresh(page_index=1){
        this.page_index = page_index;
        let query = this.get_query_params();
        let $this = this;
        query_user({"list_query":query}).then(function (res) {
          if (res.data && res.data.list){
            $this.table_data = res.data.list;
            $this.total = res.data.total;
          }
        })
      },
      // 删除
      handle_delete(row) {
        this.$confirm('此操作将永久删除该用户管理管理信息, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          let $this = this;
          delete_user(row.user_id).then(function(){
            $this.$message({
              type: 'success',
              message: '删除成功!'
            });
            // 分页逻辑判断
            if ($this.page_index===1){
              $this.fresh();
            }else if(($this.total - $this.page_size * ($this.page_index-1))>1){
              $this.fresh($this.page_index);
            }else{
              $this.fresh($this.page_index-1)
            }
            $this.fresh($this.page_index);
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      // 添加数据
      handle_add(){
        this.$refs.add.show_dialog();
      },
      // 更新数据
      handle_update(data){
        this.$refs.update.show_dialog(data)
      },
      //点击分页按钮
      handle_size_change(val) {
        this.page_size = val;
        this.fresh();
      }
    }
  }
</script>

<style lang="scss" scoped>

  .container{

  }
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
  .margin-space{
    margin:20px
  }

</style>