
new Vue({
    el: '#operations',
    delimiters: ['{$','$}'],
    data: {
        title: 'Buscar placa',
        search: true,
        validate: false,
        footer: false,
        plate: ''
    },
    methods : {
        searchPlate : function(){
            var self = this;
            if(this.plate != '')
            {
                axios.get('../../vehicles/api/search/?kword=' + this.plate)
                .then(function(response){
                    self.title = 'Placa N°: ' + response.data[0].plate
                    self.search = false
                    self.validate= true
                })
                .catch(function(error){
                    console.log(error)
                })
            }
            else{
                this.plate = 'Ingrese una placa para continuar'
            }
        },
        CreateSOAT : function(){

        }
    }
})