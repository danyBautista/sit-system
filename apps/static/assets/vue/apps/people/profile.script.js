// register form component
new Vue({
    el: '#profile',
    delimiters: ['{$','$}'],
    data: {
        form: false,
        id_frm: 0,
        st_frm: false,
        tl_frm: ''
    },
    watch:{
        form_id: function(val){
            this.viewForms(val)
        }
    },
    methods: {
        viewForms: function(content, id, title){
            var self = this;
            self.id_frm = id;
            self.tl_frm = title;
            self.form = content;
        }
    },
})