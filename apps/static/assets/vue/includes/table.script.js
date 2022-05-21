new Vue({
    el: '#table',
    delimiters: ['{$','$}'],
    data: {
        icon_content : true,
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
            var route = document.getElementById("route_search").value;
            var self = this;
            axios.get(route + kword)
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
            var redir = document.getElementById("route_view").value;
            window.location.href = redir + param
        }
    },
});

(function(){
    var o = document.getElementById("btn-search");
    var f = document.getElementById("submit-search");

    var iprocess = document.getElementById("icon-process");
    var iviews = document.getElementById("icon-views");
    var search = document.getElementById("form-search");

    o.addEventListener("click", function(event){
        iprocess.classList.add('d-none');
        iviews.classList.add('d-none');
        search.classList.remove('d-none');
    }, false);

    f.addEventListener("click", function(event){
        iprocess.classList.remove('d-none');
        iviews.classList.remove('d-none');
        search.classList.add('d-none');
    },false)
})();