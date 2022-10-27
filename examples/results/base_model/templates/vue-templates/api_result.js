// 用户管理管理管理
import request from '@/utils/request'

//新增用户管理管理
export function add_user(data){
  return request({
    url: '/user',
    method: 'post',
    data
  })
}
//批量导入用户管理管理
export function import_user(data){
  return request({
    url: '/user/import',
    method: 'post',
    data
  })
}
//删除用户管理管理
export function delete_user(user_id){
  return request({
    url: '/user/' + user_id,
    method: 'delete',
  })
}
//更新用户管理管理
export function update_user(data){
  return request({
    url: '/user/' + data["user_id"] ,
    method: 'put',
    data
  })
}
//查询用户管理管理
export function query_user(data){
  return request({
    url: '/user/query' ,
    method: 'post',
    data
  })
}

export let list = [
  
]