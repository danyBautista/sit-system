
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
                            if (result > 1){
                                self.sfooter = true;
                                self.bg = 'bg-info';
                                self.message = 'Vehiculos con validacion encontrados seleccione uno para continuar'
                                self.vehicle_content = true;
                                self.vehicles = data
                            }else{
                                if(result == 1)
                                {
                                    var dt = Object(response.data)
                                    console.log(dt)
                                    window.location.href = "../form/" + dt[0]['id']
                                }
                                else{
                                    axios.get('../api/search/?kword=' + self.plate)
                                    .then(function(response){
                                        var data = Object(response.data)
                                        window.location.href = "../update/" + data[0]['id']
                                    })
                                }
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