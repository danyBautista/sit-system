function inspections(options){
    let _this = this;
    let DefaultOptions = {
        id_user : '',
        route:''
    }
    options = {...DefaultOptions, ...options};

    this.init = function(){
        alert(options.route)
        this.viewCardsearch();
    }
    this.viewCardsearch = function(){
        const panelsearch = document.getElementById('key_word');
        panelsearch.addEventListener('keypress', function(event){
            if(event.key === "Enter"){
                event.preventDefault();
                _this.searchKey(this.value.toUpperCase())
            }
        })
    }
    this.searchKey = function(kword){
        axios.get("/tablero/query/api/select/" + kword)
            .then(function(response){
                var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };
            data_create= {
                'key_register': response.data[0].plate,
                'user' : options.id_user,
                'status_query' : true,
            }
            axios({
                method: 'POST',
                url: '../tablero/query/api/create/',
                headers: headers,
                data: data_create
                })
                .then( function(response){
                    console.log(response.data['key_register'])
                    window.location.href = "search/" + response.data['key_register']
                })
                .catch(function(error){
                    console.log(error)
                })
            })
    }
    this.init();
}