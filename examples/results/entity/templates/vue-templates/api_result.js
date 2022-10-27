// 槽位数据管理管理
import request from '@/utils/request'

//新增槽位数据管理
export function add_entity(data){
  return request({
    url: '/entity',
    method: 'post',
    data
  })
}
//批量导入槽位数据管理
export function import_entity(data){
  return request({
    url: '/entity/import',
    method: 'post',
    data
  })
}
//删除槽位数据管理
export function delete_entity(entity_id){
  return request({
    url: '/entity/' + entity_id,
    method: 'delete',
  })
}
//更新槽位数据管理
export function update_entity(data){
  return request({
    url: '/entity/' + data["entity_id"] ,
    method: 'put',
    data
  })
}
//查询槽位数据管理
export function query_entity(data){
  return request({
    url: '/entity/query' ,
    method: 'post',
    data
  })
}

export let list = [
  
]