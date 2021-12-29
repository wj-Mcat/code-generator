<el-autocomplete
  class="inline-input"
  v-model="form.stocktaking_name"
  :fetch-suggestions="stocktaking_name_query_search"
  :trigger-on-focus="true"
  value-key="stocktaking_name"
  placeholder="请输入内容"
></el-autocomplete>

stocktaking_name_query_search(queryString, cb) {
this.$remote_autocomplete('Stocktaking', 'stocktaking_name', queryString).then(function(res){
  if ('data' in res){
    cb(res['data'])
  }
})
},