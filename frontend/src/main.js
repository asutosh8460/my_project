import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
// import router from './router'

Vue.use(VueRouter);

Vue.config.productionTip = false;

// Define your routes array here
const Routes = [
  // Example routes:
  { path: "/", component: Home },
  { path: "/about", component: About },
  // ... other routes
];

const router = new VueRouter({
  routes: Routes,
});

new Vue({
  el: "#app",
  render: (h) => h(App),
  router,
});

// import Vue from "vue";
// import App from "./App.vue";
// import VueRouter from "vue-router";

// Vue.use(VueRouter);

// Vue.config.productionTip = false;

// const router = new VueRouter({
//   routes: Routes,
// });

// new Vue({
//   el: "#app",
//   render: (h) => h(App),
//   router,
// });

// new Vue({
//   render: function (h) {
//     return h(App);
//   },
// }).$mount("#app");
