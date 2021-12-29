<template>
  <el-dialog title="新增正则化抽取器管理" :visible.sync="show" v-loading="loading">
    <el-form :model="form" label-width="120px" :rules="rules" ref="form">
      <el-form-item label="别名" prop="name">
          <el-input v-model="form.name" placeholder="请输入别名" />
      </el-form-item><el-form-item label="Module Path" prop="module">
          <el-input v-model="form.module" placeholder="请输入Module Path" />
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
    add_regex_extractor
  } from "./api_result";
    export default {
      name: "add",
      data(){
        return {
          loading:false,
          show:false,
          form:{},
          
          rules:{
              name:[{required:true, message:"请输入别名", trigger:['blur']}],
              module:[{required:true, message:"请输入Module Path", trigger:['blur']}],
              
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
              add_regex_extractor(this.form).then(function (res) {
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