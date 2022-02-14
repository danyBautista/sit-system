// register form component
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

new Vue({
    el: '#profile',
    delimiters: ['{$','$}'],
    data: {
        form: false,
        id_frm: 0,
        st_frm: false,
        tl_frm: '',
        name: '',
        first_name:'',
        last_name:''
    },
    watch:{
        form_id: function(val){
            this.viewForms(val)
            this.update(val)
        }
    },
    methods: {
        viewForms: function(content, id, title, dni){
            var self = this;
            axios.get('/people/api/select/' + dni + '/')
            .then(function(response){
                self.id_frm = id;
                self.tl_frm = title;
                self.form = content;
                self.name = response.data[0].name
                self.first_name = response.data[0].first_name
                self.last_name = response.data[0].last_name
            })
            .catch(function(error){
                console.log(error)
            })
        },
        update: function(dni)
        {
            var csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
            let headers = {
                "X-CSRFToken": csrftoken,
                "Content-Type": "application/x-www-form-urlencoded"
            };
            const people = {
                'name' : this.name,
                'first_name' : this.first_name,
                'last_name' : this.last_name
            }
            axios.put('/people/api/update/' + dni, people, headers)
            .then(res => console.log(res.data))
            .catch(function(error){
                console.log(error)
            })
        }
    },
})