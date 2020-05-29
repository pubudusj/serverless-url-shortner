import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    short_urls: null,
    loader: null
  },
  mutations: {
    fetchShortUrls(state, data) {
      state.short_urls = data;
    },
    addShortUrl(state, shortUrl) {
      state.short_urls.unshift(shortUrl);
    },
    updateLoader(state, value) {
      state.loader = value;
    }
  },
  actions: {
    async addShortUrl({ commit, dispatch }, short_url) {
      dispatch('setLoader', 'Creating...')
      const result = await api.addShortUrl(short_url)
      if (result) commit('addShortUrl', result)
      else(console.error('Failed adding short url'))
      dispatch('setLoader', null)
    },
    async fetchShortUrls({ commit, dispatch }) {
      dispatch('setLoader', 'Fetching...')
      const result = await api.fetchShortUrls()
      if (result) commit('fetchShortUrls', result)
      else(console.error('Failed fetching urls'))
      dispatch('setLoader', null)
    },
    setLoader({ commit }, value) {
      commit('updateLoader', value)
    }
  },
  modules: {
  },
  getters: {
    getShortUrls(state){
      return state.short_urls;
    }
  }
})
