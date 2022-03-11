new Vue({
    el :'#procedure',
    delimiters: ['{$','$}'],
    data:{
        title : 'Nuevo registro',
        score_icon: true,
        score_load: false,
        scolor: 'text-dark',
        score_text: 'Observado',
    },
    methods: {
        validateOptions : function(){
            this.score_icon = false
            this.score_load = true
            this.scolor = 'text-info',
            this.score_text = 'Procesando...'

            var license_plate = $('#id_license_plate')
            var date_check = $('#id_check_date')
            var message = $('#message')
            if(license_plate.val() != '' && date_check.val() != '')
            {
                axios.get('/certificate/api/select/soat/' + license_plate.val())
                .then( function(response){
                    reslg = Object.keys(response.data).length
                    if(reslf > 1 )
                    {
                        alert('mayor a uno')
                    }
                    else{
                        alert('igual a uno')
                    }
                })
                .catch(function(error){
                    console.log(error)
                })
            }
            else{
                message.modal('show')
                $('#icon').html('warning')
                $('#title-mesage').html('Advertencia')

                if(license_plate.val() != '')
                    $('#content').html('No se registro ninguna fecha de control, no se puede continuar.')
                else if(date_check.val() != '')
                    $('#content').html('No encuentra la placa del vehiculo para su validacion, no se puede continuar.')

                $('#bg-message, #bg-btn-message').addClass('bg-gradient-warning').removeClass('bg-message')
            }
        }
    },
})