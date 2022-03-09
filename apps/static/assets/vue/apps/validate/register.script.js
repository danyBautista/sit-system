new Vue({
    el: '#routes',
    delimiters: ['{$','$}'],
    data:{
        id : '',
        route : 'hola',
        limit : '',
        status : false
    },
    methods : {
        RetisterRoute : function(){
            route = document.getElementById('id_route')
            concession = document.getElementById('id_concession')
            stt  = document.getElementById('id_status')
            limit  = document.getElementById('id_limit')
            var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };

            data_create = {
                'route' : route.value,
                'concession' : concession.value,
                'status' : stt.value,
                'limit' : limit.value
            }
            axios({
                method: 'POST',
                url: '/validations/procedure/create/',
                headers: headers,
                data: data_create
            })
            .then( function(response){
                $("#routes").modal('hide');
                console.log(response)
            })
            .catch(function(error){
                console.log(error)
            })
        }
    }
})