<template>
  <el-dialog title="新增槽位数据管理" :visible.sync="show" v-loading="loading">
    <el-form :model="form" label-width="120px" :rules="rules" ref="form">
      <el-form-item label="关键字" prop="key">
          <el-input v-model="form.key" placeholder="请输入关键字" />
      </el-form-item><el-form-item label="别名" prop="alias">
          <el-input v-model="form.alias" placeholder="请输入别名" />
      </el-form-item><el-form-item label="实体类型" prop="entity_type_id">
          <el-input v-model="form.entity_type_id" placeholder="请输入实体类型" />
      </el-form-item><el-form-item label="实体数据类型" prop="entity_value_type">
          <el-input v-model="form.entity_value_type" placeholder="请输入实体数据类型" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit">提 交</el-button>
        <el-button @click="reset_form">重 置</el-button>
        <el-button @click="show=false">取 消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
  import {
    add_entity
  } from "./api_result";
    export default {
      name: "add",
      data(){
        return {
          loading:false,
          show:false,
          form:{},
          
          rules:{
              key:[{required:true, message:"请输入关键字", trigger:['blur']}],
              alias:[{required:true, message:"请输入别名", trigger:['blur']}],
              entity_type_id:[{required:true, message:"请输入实体类型", trigger:['blur']}],
              entity_value_type:[{required:true, message:"请输入实体数据类型", trigger:['blur']}],
              
          }
        }
      },
      methods:{
        show_dialog(){
          this.show=true;
          this.loading = false;
          this.form = {
            create_user_id:this.$store.state.user.user_id
          };
        },
        reset_form(){
          this.form={}
        },
        submit(){
          this.$refs["form"].validate((valid) => {
            if (valid) {
              this.loading = true;
              let $this = this;
              add_entity(this.form).then(function (res) {
                $this.loading=false;
                if (res.code === 200){
                  $this.show=false;
                  $this.$emit("fresh");
                }else{
                  alert(res.message);
                }
              })
            } else {
              return false;
            }
          });
        }
      }
    }
</script>