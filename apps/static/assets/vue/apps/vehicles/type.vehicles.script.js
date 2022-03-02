new Vue({
    el: '#type-vehicle',
    delimiters: ['{$', '$}'],
    data: {
        name: '',
        status: true
    },
    watch:{
        form_id: function(val){
            this.register(val)
        }
    },
    methods: {
        register: function(){
            var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };
            var data_type = {
                'name' : this.name,
                'status' : this.status
            }
            axios({
                method: 'POST',
                url: '/vehicles/api/type/register/',
                headers: headers,
                data: data_type
            })
            .then(function (response){
                var select = document.getElementById('#id_type')
                for (value in response)
                {
                    var option = document.createElement("option");
                    option.text = array[value.data.name]
                    select.add(option)
                }
                console.log(response.data)
            })
            .catch( function(error){
                console.log(error)
            })
        }
    }
})