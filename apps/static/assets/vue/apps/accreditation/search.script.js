
new Vue({
    el: '#operations',
    delimiters: ['{$','$}'],
    data: {
        title: 'Buscar placa',
        search: true,
        validate: false,
        footer: false,
        vehicle_content: false,
        vehicles: [],
        plate: '',
        message: '',
        bg : 'bg-warning'
    },
    methods : {
        searchPlate : function(){
            var self = this;
            if(this.plate != '')
            {
                axios.get('../../vehicles/api/search/?kword=' + this.plate)
                .then(function(response){
                    result = Object.keys(response.data).length
                    if(result == 1){
                        var data = response.data
                        axios.get('../../validations/api/list/vehicle/?kword=' + data[0]['plate'])
                        .then(function(response){
                            var result = Object.keys(response.data).length
                            if (result != 0){
                                var data = Object(response.data)
                                if(result > 1){
                                    self.footer = true;
                                    self.bg = 'bg-info';
                                    self.message = 'Vehiculos con validacion encontrados seleccione uno para continuar'
                                    self.vehicle_content = true;
                                    self.vehicles = data
                                }
                                else{
                                    window.location.href = "../form/" + data[0]['id']
                                }
                            }else{
                                window.location.href = "../../validations/select/" + self.id
                            }
                        })
                    }else{
                        window.location.href = "../../vehicles/create/"
                    }
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
        getVehicleProcedure :function(){

        }
    }
})