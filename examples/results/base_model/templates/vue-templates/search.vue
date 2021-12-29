<template>
  <el-card class="box-card margin-space">
    <div slot="header">
      <span>高级筛选</span>
    </div>
    <!--      筛选表单-->
    <el-form :inline="true" :model="form" ref="form" class="demo-form-inline" label-width="120px">
    <el-form-item label="姓名" prop="name">
          <el-input v-model="form.name" placeholder="请输入姓名" />
      </el-form-item><el-form-item label="性别" prop="sex">
          <el-input v-model="form.sex" placeholder="请输入性别" />
      </el-form-item><el-form-item label="角色" prop="role_id">
          <el-input v-model="form.role_id" placeholder="请输入角色" />
      </el-form-item>
      <div style="margin-left:50px">
        <el-form-item>
          <el-button type="primary" @click="search">查询</el-button>
        </el-form-item>
        <el-form-item>
          <el-button @click="reset_search()">重置</el-button>
        </el-form-item>
      </div>
    </el-form>
  </el-card>
</template>

<script>
    export default {
      name: "search",
      data(){
        return{
        
          form:{}
        }
      },
      methods:{
        get_search_params(){
          // 此函数也提供给父组件调用
          let query = Object.assign({},this.form);
          delete query["time"];
          return query;
        },
        search(){
          this.$emit("fresh");
        },
        
        
        
        
        
        
        
        reset_search(){
          this.form={};
          this.search();
        }
      }
    }
</script>

<style scoped>

</style>