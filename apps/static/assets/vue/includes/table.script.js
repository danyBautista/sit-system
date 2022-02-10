

new Vue({
    el: '#table',
    delimiters: ['{$','$}'],
    data: {
        list_view: false,
        search_content: true,
        kword: '',
        list_user: []
    },
    watch:{
        kword: function(val){
            this.searchUser(val)
        }
    },
    methods: {
        searchUser: function(kword){
            var self = this;
            axios.get('/people/api/search/?kword=' + kword)
            .then(function(response){
                self.list_view = true
                self.search_content = false
                self.list_user = response.data
            })
            .catch(function(error){
                console.log(error);
            })
        },
        redirec_user: function(param)
        {
            window.location.href = '/people/view/' + param +'/'
        }
    },
});

(function(){
    var o = document.getElementById("btn-search");
    var f = document.getElementById("submit-search");

    var content = document.getElementById("content-icons");
    var search = document.getElementById("form-search");
    o.addEventListener("click", function(event){
        content.classList.add('d-none')
        search.classList.remove('d-none');
    }, false);

    f.addEventListener("click", function(event){
        content.classList.remove('d-none')
        search.classList.add('d-none');
    },false)
})();