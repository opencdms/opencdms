// store.js
import { createStore } from 'vuex'

export const store = createStore({
  state() {
    return {
      csvData: null,
      selected: []
    }
  },
  mutations: {
    setCSVData(state, data) {
      state.csvData = data
    },
    setSelected(state, selected){
      console.log(selected);
      state.selected = selected;
    }
  },
  actions: {
    async fetchCSVData({ commit }, filename) {
      const csvData = await d3.csv(filename);
      commit('setCSVData', csvData);
    }
  },
  getters: {
    getCSVData(state) {
      return state.csvData;
    },
    getSelected(state){
      console.log( "state.selected" );
      if (state.selected === null || state.selected === undefined){
        return [];
      } else {
        return state.selected;
      }
    }
  }
})
