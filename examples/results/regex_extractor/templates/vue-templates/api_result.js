// 正则化抽取器管理管理
import request from '@/utils/request'

//新增正则化抽取器管理
export function add_regex_extractor(data){
  return request({
    url: '/regex_extractor',
    method: 'post',
    data
  })
}
//批量导入正则化抽取器管理
export function import_regex_extractor(data){
  return request({
    url: '/regex_extractor/import',
    method: 'post',
    data
  })
}
//删除正则化抽取器管理
export function delete_regex_extractor(regex_extractor_id){
  return request({
    url: '/regex_extractor/' + regex_extractor_id,
    method: 'delete',
  })
}
//更新正则化抽取器管理
export function update_regex_extractor(data){
  return request({
    url: '/regex_extractor/' + data["regex_extractor_id"] ,
    method: 'put',
    data
  })
}
//查询正则化抽取器管理
export function query_regex_extractor(data){
  return request({
    url: '/regex_extractor/query' ,
    method: 'post',
    data
  })
}

export let list = [
  
]