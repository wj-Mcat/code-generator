<template>
  <el-dialog title="编辑用户管理管理" :visible.sync="show" v-loading="loading">
    <el-form :model="form" label-width="120px" :rules="rules" ref="form">
      <el-form-item label="昵称" prop="nick">
          <el-input v-model="form.nick" placeholder="请输入昵称" />
      </el-form-item><el-form-item label="用户名" prop="username">
          <el-input v-model="form.username" placeholder="请输入用户名" />
      </el-form-item><el-form-item label="用户密码" prop="password">
          <el-input v-model="form.password" placeholder="请输入用户密码" />
      </el-form-item><el-form-item label="备注" prop="remark">
          <el-input v-model="form.remark" placeholder="请输入备注" />
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
    update_User
  } from "./api_result";
    export default {
      name: "add",
      data(){
        return {
          loading:false,
          show:false,
          form:{},
          
          rules:{
              nick:[{required:true, message:"请输入昵称", trigger:['blur']}],
              username:[{required:true, message:"请输入用户名", trigger:['blur']}],
              password:[{required:true, message:"请输入用户密码", trigger:['blur']}],
              remark:[{required:true, message:"请输入备注", trigger:['blur']}],
              
          }
        }
      },
      methods:{
      show_dialog(data) {
          this.show = true;
          this.form = Object.assign({}, data);
          this.source_data = Object.assign({}, data);
          this.form.modify_user_id = this.$store.state.user.user_id;
        },
        reset_form(){
          this.form={}
        },
        submit(){
          this.$refs["form"].validate((valid) => {
            if (valid) {
              this.loading = true;
              let $this = this;
              update_User(this.form).then(function (res) {
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