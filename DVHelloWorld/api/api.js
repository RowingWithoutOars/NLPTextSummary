import axios from 'axios'
axios.defaults.baseURL = 'http://localhost:8000//'

export const getInfo = params => {
  return axios.post('rest/nonAddress', params).then(
    res => res.data
  )
}
