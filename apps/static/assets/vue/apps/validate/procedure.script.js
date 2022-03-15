new Vue({
    el :'#procedure',
    delimiters: ['{$','$}'],
    data:{
        title : 'Nuevo registro',
        score_icon: true,
        score_load: false,
        scolor: 'text-dark',
        score_text: 'Observado',

        soaticon: 'fa-question',
        soatcolor: 'text-dark',
        soat_text: 'Indeterminado',

        citvcolor: 'text-dark',
        citvicon: 'fa-question',
        citv_text: 'Vigente',

        srccolor: 'text-dark',
        srcicon: 'fa-question',
        src_text: 'Vigente'
    },
    methods: {
        validateOptions : function(){
            this.score_icon = false
            this.score_load = true
            this.scolor = 'text-info',
            this.score_text = 'Procesando...'

            var license_plate = $('#id_license_plate')
            var date_check = $('#id_check_date')

            var self = this;
            if(license_plate.val() != '' && date_check.val() != '')
            {
                axios.get('/certificate/api/select/soat/?vehicles=' + license_plate.val())
                .then( function(response){
                    self.soaticon = 'fa-sync fa-spin'
                    self.soatcolor = 'text-info'
                    self.soat_text = 'procesando...'

                    var _count = Object.keys(response.data).length
                    if(_count == 1)
                    {
                        if(response.data[0].date_expiry > date_check.val())
                        {
                            self.soatcolor = 'text-success'
                            self.soat_text = 'Vigente'
                            self.soaticon = 'fa-check'
                            $('#id_soat_status').val(self.soat_text)
                            $('#id_soat').val(response.data[0].policy)
                            axios.get('/certificate/api/select/citv/?vehicle=' + license_plate.val())
                            .then(function(response){
                                self.citvcolor = 'text-info'
                                self.citvicon = 'fa-sync fa-spin'
                                self.citv_text = 'Procesando...'
                                var _count = Object.keys(response.data).length
                                if(_count == 1)
                                {
                                    if(response.data[0].expiration_date > date_check.val())
                                    {
                                        self.citvcolor = 'text-success'
                                        self.citv_text = 'Vigente'
                                        self.citvicon = 'fa-check'
                                        $('#id_citv_status').val(self.citv_text)
                                        $('#id_citv').val(response.data[0].id)
                                        axios.get('/certificate/api/select/src/?vehicles=' + license_plate.val())
                                        .then(function(response){
                                            self.srccolor = 'text-info',
                                            self.srcicon = 'fa-sync fa-spin',
                                            self.src_text = 'Procesando...'
                                            var _count = Object.keys(response.data).length
                                            if(_count == 1)
                                            {
                                                self.srccolor = 'text-success'
                                                self.srcicon = 'fa-check'
                                                self.src_text = 'Vigente'
                                            }
                                            else{
                                                self.srccolor = 'text-warning'
                                                self.src_text = 'No vigente'
                                                self.srcicon = 'fa-exclamation'

                                                message =   [
                                                    'Existe mas de un SRC',
                                                    'Actualmente encontramos ' + _count + ' registros para esta placa',
                                                    ''
                                                ]
                                                self.ViewMessage('info', message);
                                            }
                                        })
                                        .catch(function(error){
                                            console.log(error)
                                        })
                                    }
                                    else{
                                        self.citvcolor = 'text-warning'
                                        self.citv_text = 'No vigente'
                                        self.citvicon = 'fa-exclamation'

                                        message =   [
                                            'Observaciones de CITV',
                                            'La fecha de control es superior a la fecha de expiracion de CITV',
                                            '<small>Es necesario seleccionar el registro adecuado apara la placa</small>'
                                        ]
                                        self.ViewMessage('warning', message);
                                    }
                                }
                                else{
                                    message =   [
                                        'Existe mas de un CITV',
                                        'Actualmente encontramos mas de un regitro para esta placa',
                                        ''
                                    ]
                                    this.ViewMessage('info', message);
                                }
                            })
                            .catch(function(error){
                                console.log(error)
                            })
                        }
                        else{
                            self.soatcolor = 'text-warning'
                            self.soat_text = 'No vigente'
                            self.soat_mark = 'fa-exclamation'

                            message =   [
                                'Observaciones de SOAT',
                                'La fecha de control es superior a la fecha de expiracion de soat',
                                ''
                            ]
                            self.ViewMessage('warning', message);
                        }
                    }
                    else{
                        message =   [
                            'Existe mas de un soat',
                            'Actualmente encontramos mas de un regitro para esta placa',
                            ''
                        ]
                        this.ViewMessage('info', message);
                    }
                })
                .catch(function(error){
                    console.log(error)
                })
            }
            else{
                message =   [
                                'Verificacion de datos',
                                'No se ingreso la fecha de control no se puede continuar sin este dato',
                                ''
                            ]
                this.ViewMessage('warning', message);
            }
        },
        ViewMessage: function(t='quest', c = ['title', 'msg', 'body']){
            $('#bg-message, #bg-btn-message')
                .removeClass('bg-message')
                .removeClass('bg-gradient-info')
                .removeClass('bg-gradient-warning')
                .removeClass('bg-gradient-success')
                .removeClass('bg-gradient-danger')
                .removeClass('bg-gradient-secondary')
            $('#message').modal('show')
            switch (t) {
                case 'info':
                    icon = 'info'
                    bg = 'bg-gradient-info'
                    break;
                case 'warning':
                    icon = 'warning'
                    bg = 'bg-gradient-warning'
                    break;
                case 'success':
                    icon = 'done'
                    bg = 'bg-gradient-sucsess'
                    break;
                case 'danger':
                    icon = 'error'
                    bg = 'bg-gradient-danger'
                    break;
                case 'quest':
                    icon = 'question_mark'
                    bg = 'bg-gradient-secondary'
                    break;
            }
            $('#icon').html(icon)
            $('#bg-message, #bg-btn-message').addClass(bg).removeClass('bg-message')
            $('#title-mesage').html(c[0])
            $('#content').html(c[1])
            $('#content-body').html(c[2])

        }
    },
})