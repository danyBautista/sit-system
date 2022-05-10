new Vue({
    el: '#vehicles',
    delimiters: ['{$', '$}'],
    data: {
        Search : '',
        ListUser: [],
        SelectUser : []
    },
    watch:{
        Search: function(val){
            this.SearchUserByDNI(val)
        }
    },
    methods: {
        SearchUserByDNI : function(Search){
            var self = this
            var url = document.getElementById('url_search_dni').innerHTML
            axios.get(url + '/people/api/search/dni/?kword=' + Search)
            .then(function(response){
                self.ListUser = response.data
            })
            .catch(function(error){
                console.log(error)
            })
        },
        AddUserByDNI : function(DNI)
        {
            var chekbox = '<input type="checkbox" name="owners" value="' + DNI.dni + '" id="' + DNI.dni + '">'
            var content = document.getElementsByClassName("chk-result")
            console.log(DNI.dni)
            this.Search = ''
            this.SelectUser.push(DNI)
        }
    },
})