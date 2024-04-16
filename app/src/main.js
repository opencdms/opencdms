import "vuetify/styles";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import 'material-design-icons-iconfont/dist/material-design-icons.css';

import {createPinia} from 'pinia';

const pinia = createPinia();

const app = createApp(App)
  .use(router)
//  .use(pinia)
  .use(createPinia())
  .use(vuetify)

app.mount("#app")
