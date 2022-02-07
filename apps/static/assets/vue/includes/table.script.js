// register modal component
Vue.component("views", {
    template: "#modal-template"
});

  // start app
new Vue({
    el: "#table",
    delimiters: ['{$','$}'],
    data: {
        showList: false,
        showIcon: true
    }
});
