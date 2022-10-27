// 用户管理管理管理
import request from '@/utils/request'

//新增用户管理管理
export function add_User(data){
  return request({
    url: '/general/User',
    method: 'post',
    data
  })
}
//批量导入用户管理管理
export function import_User(data){
  return request({
    url: '/general/User/import',
    method: 'post',
    data
  })
}
//删除用户管理管理
export function delete_User(User_id){
  return request({
    url: '/general/User/' + User_id,
    method: 'delete',
  })
}
//更新用户管理管理
export function update_User(data){
  return request({
    url: '/general/User/' + data["User_id"] ,
    method: 'put',
    data
  })
}
//查询用户管理管理
export function query_User(data){
  return request({
    url: '/general/User/query' ,
    method: 'post',
    data
  })
}

export let list = [
  
]