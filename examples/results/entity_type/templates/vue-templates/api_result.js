// 槽位类别管理管理
import request from '@/utils/request'

//新增槽位类别管理
export function add_entity_type(data){
  return request({
    url: '/entity_type',
    method: 'post',
    data
  })
}
//批量导入槽位类别管理
export function import_entity_type(data){
  return request({
    url: '/entity_type/import',
    method: 'post',
    data
  })
}
//删除槽位类别管理
export function delete_entity_type(entity_type_id){
  return request({
    url: '/entity_type/' + entity_type_id,
    method: 'delete',
  })
}
//更新槽位类别管理
export function update_entity_type(data){
  return request({
    url: '/entity_type/' + data["entity_type_id"] ,
    method: 'put',
    data
  })
}
//查询槽位类别管理
export function query_entity_type(data){
  return request({
    url: '/entity_type/query' ,
    method: 'post',
    data
  })
}

export let list = [
  
]