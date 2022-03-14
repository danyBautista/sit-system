
new Vue({
    el: '#operations',
    delimiters: ['{$','$}'],
    data: {
        title: 'Buscar placa',
        search: true,
        validate: false,
        footer: false,
        plate: '',
        message: ''
    },
    methods : {
        searchPlate : function(){
            var self = this;
            if(this.plate != '')
            {
                axios.get('../../vehicles/api/search/?kword=' + this.plate)
                .then(function(response){
                    reslg = Object.keys(response.data).length
                    console.log(response)
                    if(reslg == 1)
                        window.location.href = "../../validations/select/" + self.plate
                    else
                        window.location.href = "../../vehicles/create/"
                })
                .catch(function(error){
                    console.log(error)
                })
            }
            else{
                this.message = 'No registro ninguna placa vehicular.'
                this.footer = true
            }
        },
        CreateSOAT : function(){

        }
    }
})