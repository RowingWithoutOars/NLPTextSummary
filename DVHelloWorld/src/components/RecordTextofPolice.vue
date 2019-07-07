<template>
  <section>
    <el-col :span="24" class="toolbar" style="padding-bottom: 0;">
      <h1>笔录文本信息摘要演示系统<br>Record Text of Police Information Summary Demonstration System
      </h1>
    <el-form :inline="true">
      <el-header>
        <el-form-item>
          <el-select v-model="values" placeholder="请选择" style="width: 150px">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
        <el-input type="textarea" autosize v-model="nonAddress" placeholder="请输入笔录文本"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="getAddress()">查询</el-button>
        </el-form-item >
      </el-header>
      <el-main>
        <el-form-item>
          <el-table :data="matchAddress" align="left" v-if="this.matchAddress.length>0" v-loading="loading" highlight-current-row style="width: 100%;">
          <el-table-column type="index" width="60">
          </el-table-column>
          <el-table-column prop="label" label="子类别" width="300" sortable='custom'>
          </el-table-column>
          <el-table-column prop="p" label="可信度" width="200" sortable='custom'>
          </el-table-column>
          </el-table>
        </el-form-item>
      </el-main>
      <el-footer>
      <el-form-item>
        <label>Copyright© 2018 苏州科技大学-昆山市公安局 大数据应用联合实验室</label>
      </el-form-item>
      </el-footer>
    </el-form>
    </el-col>
    <el-container>
    </el-container>
  </section>
</template>
<script>
import { getInfo } from '../../api/api'
export default {
  data () {
    return {
      nonAddress: '',
      options: [{
        label: '作案手段',
        value: 0
      }, {
        label: '一级物品',
        value: 1
      }, {
        label: '一级案由',
        value: 2
      }, {
        label: '一级案发区域',
        value: 3
      }, {
        label: '二级物品',
        value: 4
      },
      {
        label: '二级案由',
        value: 5
      }, {
        label: '二级案发区域',
        value: 6
      }],
      values: 0,
      matchAddress: [],
      loading: false
    }
  },
  methods: {
    getAddress () {
      console.log(this.nonAddress)
      let para = {
        nonAddress: this.nonAddress.trim()
      }
      this.loading = true
      getInfo(para).then((result) => {
        console.log(result)
        this.loading = false
        if (result.data.length === 0) {
          this.$alert('没有合适的匹配结果', '提示', {
            confirmButtonText: '确定'
          }
          )
        }
        this.matchAddress = result.data
        if (this.matchAddress.length > this.values) {
          this.matchAddress = this.matchAddress.slice(0, this.values)
        }
      })
    }
  }
}

</script>
<style>
  .el-header, .el-footer {
    text-align: center;
    line-height: 100px;
  }

  .el-aside {
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    text-align: center;
    line-height: 500px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
