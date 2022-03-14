new Vue({
    el :'#procedure',
    delimiters: ['{$','$}'],
    data:{
        title : 'Nuevo registro',
        score_icon: true,
        score_load: false,
        scolor: 'text-dark',
        score_text: 'Observado',
        soat_icon: true,
        soat_load: false,
        soatcolor: 'text-dark',
        soat_text: 'Indeterminado',
        soat_mark: 'question_mark'
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

            var self = this;

            if(license_plate.val() != '' && date_check.val() != '')
            {
                axios.get('/certificate/api/select/soat/' + license_plate.val())
                .then( function(response){
                    reslg = Object.keys(response.data).length
                    if(reslg > 1 )
                    {
                        self.soat_icon = false
                        self.soat_load = true
                        self.soatcolor = 'text-info'
                        self.soat_text = 'procesando...'

                        message.modal('show')
                        $('#icon').html('settings')
                        $('#content').html('Se necesita su aprobacion para continuar con la habilitacion')
                        $('#bg-message, #bg-btn-message').addClass('bg-gradient-secondary').removeClass('bg-message')
                        $('#title-mesage').html('Verificacion de SOAT')
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
        },
        ViewMessage : function(t, m, cl = 1, ct=''){
            var color = ''
            switch (type) {
                case 1:
                    color = text-dark
                    break;
                case 2:
                    color = text-info
                    break;
                case 3:
                    color = text-success
                    break;
                case 4:
                    color = text-warning
                    break;
                default:
                    break;
            }
            $('#icon').html(i)
            $('#content').html(m)
            $('#bg-message, #bg-btn-message').addClass('bg-gradient-secondary').removeClass('bg-message')
            $('#title-mesage').html(t)
        }
    },
})