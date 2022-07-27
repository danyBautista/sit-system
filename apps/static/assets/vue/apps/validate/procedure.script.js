new Vue({
    el :'#procedure',
    delimiters: ['{$','$}'],
    data:{
        title : 'Nuevo registro',
        scoreicon: 'fa-question',
        scorecolor: 'text-dark',
        score_text: 'Observado',

        pericon : 'fa-question',
        percolor: 'text-dark',
        per_text: 'Observado',

        enbicon : 'fa-question',
        enbcolor: 'text-dark',
        enb_text: 'Observado',

        soaticon: 'fa-question',
        soatcolor: 'text-dark',
        soat_text: 'Indeterminado',

        citvcolor: 'text-dark',
        citvicon: 'fa-question',
        citv_text: 'Indeterminado',

        srccolor: 'text-dark',
        srcicon: 'fa-question',
        src_text: 'Indeterminado',

        svctcolor: 'text-dark',
        svcticon: 'fa-question',
        svct_text: 'Indeterminado'
    },
    methods: {
        validateOptions : function(){
            this.scoreicon = 'fa-sync fa-spin'
            this.scorecolor = 'text-info',
            this.score_text = 'Procesando...'

            var license_plate = $('#id_license_plate')
            var date_check = $('#id_check_date')
            var year = $('#id_year_of_production')

            this.pericon = 'fa-sync fa-spin'
            this.percolor = 'text-info'
            this.per_text = 'Procesando...'

            this.enbicon = 'fa-sync fa-spin'
            this.enbcolor= 'text-info'
            this.enb_text= 'Procesando...'

            var self = this;

            var date = new Date(date_check.val())
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
                            self.soat_text = 'VIGENTE'
                            self.soaticon = 'fa-check'
                            $('#id_soat_status').val(self.soat_text)
                            $('#id_soat').val(response.data[0].id)
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
                                        self.citv_text = 'VIGENTE'
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
                                                self.src_text = 'VIGENTE'
                                                $('#id_src_status').val(self.src_text)
                                                $('#id_src').val(response.data[0].id)
                                                axios.get('/certificate/api/select/svct/?vehicles=' + license_plate.val())
                                                .then(function(response){
                                                    self.svctcolor = 'text-info'
                                                    self.svcticon = 'fa-sync fa-spin'
                                                    self.svct_text = 'Procesando...'
                                                    var _count = Object.keys(response.data).length
                                                    if(_count == 1){
                                                        self.svctcolor = 'text-success'
                                                        self.svcticon = 'fa-check'
                                                        self.svct_text = 'VIGENTE'
                                                        $('#id_svct_status').val(self.src_text)
                                                        $('#id_svct').val(response.data[0].id)

                                                        self.scoreicon = 'fa-check'
                                                        self.scorecolor = 'text-success'
                                                        self.score_text = 'ACEPTADO'
                                                        $('#id_score').val(self.score_text)

                                                        axios.get('../api/control/year/')
                                                        .then(function(response){
                                                            if(date.getFullYear() - year.val() <= response.data[0].years_antiquity)
                                                            {
                                                                self.pericon = 'fa-check'
                                                                self.percolor = 'text-success'
                                                                self.per_text = 'ACEPTADO'
                                                                $('#id_seniority_period').val(self.per_text)

                                                                var authorization = $("#icon-authorization").children('i').html()
                                                                var comment = $('#comment').children('i').hasClass('text-secondary')
                                                                if((authorization == 'privacy_tip' && comment == true) ||
                                                                    ($('#year_prod').html() >= 2017 ) ||
                                                                    $('#id_check_sistran').prop('checked') == true)
                                                                {
                                                                    self.enbicon = 'fa-check'
                                                                    self.enbcolor= 'text-success'
                                                                    self.enb_text= 'ACEPTADO'
                                                                    $('#id_enabled').val(self.enb_text)
                                                                }
                                                                else{
                                                                    alert('falta documento de autorizacion' + comment)
                                                                }
                                                            }
                                                            else{
                                                                self.percolor = 'text-warning'
                                                                self.per_text = 'NO VIGENTE'
                                                                self.pericon = 'fa-exclamation'

                                                                message =   [
                                                                    'Periodo de antiguedad',
                                                                    'Actualemte el vehiculo excede el periodo de antiguedad inppuesto por ' + response.data[0].years_antiquity,
                                                                    ''
                                                                ]
                                                                self.ViewMessage('warning', message);
                                                            }
                                                        })
                                                        .catch(function(error){

                                                        })
                                                    }else{
                                                        self.svctcolor = 'text-warning'
                                                        self.svct_text = 'NO VIGENTE'
                                                        self.svcticon = 'fa-exclamation'

                                                        message =   [
                                                            'Existe mas de un SVCT',
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
                                                self.srccolor = 'text-warning'
                                                self.src_text = 'NO VIGENTE'
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
                                        self.citv_text = 'NO VIGENTE'
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
                            self.soat_text = 'NO VIGENTE'
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

        },
        RegisterProcedure : function(){
            var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;
            const fd = new FormData()
            alert($('#frm_validations').serialize())
            var list_id_activity = []

            fd.append('proceedings', $('#id_proceedings').val())
            fd.append('check_date', $('#id_check_date').val())
            fd.append('year_proceeding',$('#id_year_proceeding').val())
            fd.append('route',$('#id_route').val())
            fd.append('due_date',$('#id_due_date').val())
            fd.append('contract',$('#id_contract').val())
            fd.append('authorization',$('#id_authorization').val())
            fd.append('substitution',$('#id_substitution').val())
            fd.append('vehicles',$('#id_vehicles').val())
            fd.append('year',$('#id_year').val())
            fd.append('lisense_plate',$('#id_license_plate').val())
            fd.append('year_of_production',$('#id_year_of_production').val())
            fd.append('score',$('#id_score').val())
            fd.append('seniority_period',$('#id_seniority_period').val())
            fd.append('enabled',$('#id_enabled').val())
            fd.append('soat',$('#id_soat').val())
            fd.append('soat_status',$('#id_soat_status').val())
            fd.append('citv',$('#id_citv').val())
            fd.append('citv_status',$('#id_citv_status').val())
            fd.append('src',$('#id_src').val())
            fd.append('src_status',$('#id_src_status').val())
            fd.append('svct',$('#id_svct').val())
            fd.append('svct_status',$('#id_svct_status').val())
            fd.append('status', $('#id_status').val())

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };
            axios({
                method: 'POST',
                url: '../create/',
                headers: headers,
                data: fd
            })
            .then( function(response){
                console.log(response)
            })
            .catch(function(error){
                console.log(error)
            })
        }
    },
})