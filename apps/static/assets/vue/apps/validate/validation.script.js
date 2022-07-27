$(function(){
    Validations = (function(){
        var array_id = ['soat_id', 'citv_id', 'src_id', 'svct_id']
        var current_date = $('#current_date').data('current-date')
        var init = function(){
            selectComboValidation();
            get_antiquity_period();
            get_calification();
            get_CalificationVehicle();
            get_authorizationVehicle();
            get_substitutionVehicle();
        },
        selectComboValidation = function(e){
            $('select').change(function(){
                var select = $(this).attr('id');
                var id_element = array_id.includes(select)
                var name = $(this).attr('name')
                if(id_element == true){
                    axios.get('/certificate/api/select/' + $(this).attr('name') + '/?id=' + $(this).val())
                    .then( function(response){
                        data = response.data
                        date_expiry = data['date_expiry']
                        console.log(date_operator(date_expiry, -20))
                        if(current_date < date_operator(date_expiry, -20))
                        {
                            $('#color_' + name).addClass('text-success').children('span').html('verified_user')
                            $('input:hidden[name=' + name + '_status]').val('VIGENTE')
                        }
                        else{
                            if (current_date > date_expiry){
                                $('#color_' + name).addClass('text-danger').children('span').html('gpp_bad')
                                $('input:hidden[name=' + name + '_status]').val('NO VIGENTE')
                            }
                            else{
                                $('#color_' + name).addClass('text-warning').children('span').html('gpp_maybe')
                                $('input:hidden[name=' + name + '_status]').val('OBSERVADO')
                            }
                        }
                    })
                }
            })
        },
        date_operator = function(date, day, type){
            date = new Date(date)
            date.setDate(date.getDate() + day)
            return date.getFullYear()+ '-' + date.getMonth() + '-' + date.getDate()
        },
        get_calification = function(){
            $('#id_RRPP_Newsletter').bind('click', function(e){
                if($(this).prop('checked')){
                    var vehicle = $('#id_license_plate').val()
                    var citv = $('input:hidden[name=citv_status]')
                    var soat = $('input:hidden[name=soat_status]')
                    var src = $('input:hidden[name=src_status]')
                    if(vehicle != ''){
                        messageValidation({
                            title: 'Informacion de vehiculo',
                            status_save: 'info',
                            content: 'No se encontro ninguno vehiculo registrado, no se puede continuar',
                            accept_event: 'get'
                        })
                    }
                    else{
                        if(citv.val() == 'ACEPTADO' && soat.val() == 'ACEPTADO' && src.val() == 'ACEPTADO' ){

                        }
                    }
                }
                else{
                    alert('deseleccionado')
                }
            })
        },
        get_antiquity_period = function(){
            $('#id_check_date').focusout(function(e){
                date = new Date($(this).val());
                var year_producction = $('input:hidden[name=year_of_production]').val();
                var years_validity = $('select[name=years]')
                var year_checking = date.getFullYear()
                var year = year_checking - year_producction;

                if(years_validity.val() == '')
                {
                    messageValidation({
                        title: 'Periodo de antiguedad',
                        status_save: 'info',
                        content: 'No selecciono los años de vigencia, el periodo de antiguedad no podra ser calculado. sera marcado como observado',
                        accept_event: 'get'
                    })
                    years_validity.focus();
                    $(this).val('')
                }
                else{
                    if (year > years_validity.children('option:selected').html()){
                        messageValidation({
                            title: 'Periodo de antiguedad',
                            status_save: 'info',
                            content: 'El periodo de antiguedad es inferior a los años establecidos, el vehiculo estara observado',
                            accept_event: 'get'
                        })
                        $('input:text[name=seniority_period]').val('RECHAZADO')
                        $('#seniority_period_icon').html('gpp_bad').addClass('text-danger')
                    }
                    else{
                        $('input:text[name=seniority_period]').val('ACEPTADO')
                        $('#seniority_period_icon').html('verified_user').addClass('text-success')
                        if($(this).val() == ''){
                            $('input:text[name=seniority_period]').val('OBSERVADO')
                            $('#seniority_period_icon').html('gpp_bad').addClass('text-warning')
                        }
                    }
                }
            })
        },
        get_CalificationVehicle = function(){
            var array_comment = ['', 'ninguno'];
            var soat_status = $('#soat_status_id')
            var citv_status = $('#citv_status_id')
            var src_status = $('#src_status_id')
            var svct_status = $('#svct_status_id')
            var snty_period = $('#seniority_period')
            var html = ''
            var vehicle_comment = $('input:hidden[name=comment]')

            $('input, select').change(function(e){
                var modify = true
                if (modify == true){
                    if($('#id_proceedings').val() != '' && $('#id_year_proceeding').val() != '' && $('#id_route').val() != '' && $('#id_years').val() != ''){
                        $('#id_submit').attr('disabled', false)
                        html = ''
                        habilitation(html)
                        Calification()
                    }
                }
            })
            function getRemoveClass(cls, id){
                var array_bg = ['danger', 'success', 'info', 'warning', 'transparent']
                var id_cls = $('#'+ id)
                for (let index = 0; index < array_bg.length; index++) {
                    if(id_cls.hasClass('bg-'+array_bg[index]) == true)
                    {
                        id_cls.removeClass('bg-' + array_bg[index]).addClass('bg-' + cls)
                    }
                }
            }
            function habilitation(){
                console.log(array_comment.includes(vehicle_comment.val()))
                if(($('input:checkbox[name=vehicle_authorization]').is(':checked') == true &&
                    array_comment.includes(vehicle_comment.val()) == true) &&
                    $('input:checkbox[name=check_sistran]').is(':checked') == true &&
                    $('select[name=substitution]').val() == '')
                {
                    $('#enabled_icon').removeClass('text-warning').addClass('text-success').html('verified_user')
                    $('input:hidden[name=enabled]').val('ACEPTADO')
                }
                else{
                    $('#enabled_icon').removeClass('text-success').addClass('text-warning').html('gpp_maybe')
                    $('input:hidden[name=enabled]').val('OBSERVADO')
                }
            }
            function Calification(){
                if(
                    soat_status.val() == 'VIGENTE' &&
                    citv_status.val() == 'VIGENTE' &&
                    src_status.val() == 'VIGENTE' &&
                    svct_status.val() == 'VIGENTE' &&
                    $('input:hidden[name=enabled]').val() == 'ACEPTADO' &&
                    $('input:checkbox[name=RRPP_Newsletter]').is(':checked') == true){
                    getRemoveClass('success', 'title_var')
                    $('input:hidden[name=score]').val('ACEPTADO')
                    $('#score_msg').html('ACEPTADO')
                }
                else{
                    getRemoveClass('warning', 'title_var')
                    $('input:hidden[name=score]').val('OBSERVADO')
                    $('#score_msg').html('OBSERVADO')
                }
            }
        },
        get_authorizationVehicle = function(){
            $('#form_authorization').submit(function(e){
                e.preventDefault();
                var parameters = new FormData(this);
                $.ajax({
                    url : $(this).attr('action'),
                    type: $(this).attr('method'),
                    data: parameters,
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                }).
                done(function(data){
                    let $option = $('<option/>', {text: data['code'], value: data['id']}).attr('selected', true)
                    $('select[name=authorization]').append($option)
                    $('#authorization_form').modal('hide')
                    $('#icon_authorization').html('verified_user').addClass('text-success')
                }).
                fail(function(jqXHR, textStatus, errorThrown){
                    this.messageValidation({
                        title: 'Error de guardado',
                        status_save: 'error',
                        content: 'error',
                        accept_event: 'get'
                    })
                    console.log(textStatus + ': ' + errorThrown)
                })
            })
        },
        get_substitutionVehicle = function(){
            $('#form_substitution').submit(function(e){
                e.preventDefault();
                var parameters = new FormData(this);
                $.ajax({
                    url : $(this).attr('action'),
                    type: $(this).attr('method'),
                    data: parameters,
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                }).
                done(function(data){
                    let $option = $('<option/>', {text: data['plate'], value: data['id']}).attr('selected', true)
                    $('select[name=substitution]').append($option)
                    $('#substitution_form').modal('hide')
                    $('#icon_substitution').html('verified_user').addClass('text-success')
                }).
                fail(function(jqXHR, textStatus, errorThrown){
                    messageValidation({
                        title: 'Error de guardado',
                        status_save: 'error',
                        content: 'error',
                        accept_event: 'get'
                    })
                    console.log(textStatus + ': ' + errorThrown)
                })
            })
        },
        messageValidation = function(options){
            defaults = {
                show_header: true,
                lock_escape_key: false,
                title: 'Mensaje de bienvenida',
                status_save: '',
                content: 'El registro se guardo correctamente, en la base de datos.',
                accept_event: 'post',
                url_acept: $('a.btn-link').attr('href'),
                modal_size: ''
            }

            var option = $.extend({}, defaults, options);

            var modal = '';
            $(this).each(function(){
                if(option.lock_escape_key == true){
                    lock_key = {'data-bs-backdrop': 'static'}
                }
                else{
                    lock_key = {}
                }
                modal = $('<div>').prop({id:'modalAlert', className: 'modal fade'}).attr(lock_key)

                modal_dialog = $('<div>').prop({className: 'modal-dialog modal-dialog-centered ' + option.modal_size}).appendTo(modal)
                modal_content = $('<div>').prop({className: 'modal-content'}).appendTo(modal_dialog)

                if(option.show_header == true){
                    modal_header = $('<div>').prop({className: 'modal-header py-1 pt-2'}).appendTo(modal_content)
                    modal_title = $('<h5>').prop({className: 'modal-title font-weight-normal text-sm', innerHTML: option.title}).appendTo(modal_header)
                    modal_close = $('<button>')
                        .prop({className: 'btn-close text-dark pt-0', innerHTML: '<i class="fa fa-times text-danger"></i>'})
                        .attr({'data-bs-dismiss':'modal', 'aria-label':'Close'})
                        .appendTo(modal_header)
                }
                modal_body = $('<div>').prop({className: 'modal-body'}).appendTo(modal_content)
                modal_footer = $('<div>').prop({className: 'modal-footer border-top-0 pt-0'}).appendTo(modal_content)

                status_content = $('<div>').prop({className: 'text-sm d-flex', 'id': 'content_id'}).appendTo(modal_body)

                switch (option.status_save) {
                    case 'success':
                        var icon = 'done';
                        var color = option.status_save
                        break;
                    case 'warning':
                        var icon = 'warning'
                        var color = 'warning'
                        break;
                    case 'error':
                        var icon = 'error'
                        var color = 'danger'
                        break;
                    case 'info':
                        var icon = 'info'
                        var color = 'info'
                        break;
                    case 'ajax':
                        var icon = 'save'
                        var color = 'secundary'
                        break;
                }
                status_icon = $('<span>').prop({className: 'material-icons h2 text-' + color, innerHTML: icon}).appendTo(status_content)
                status_title = $('<div>').prop({className: 'mt-3 ms-2 w-100'}).appendTo(status_content).append(option.content)

                if(option.accept_event == 'post'){
                    button_acept = $('<button>').prop({className: 'btn btn-sm bg-gradient-' + color + ' w-lg-25 m-0', innerHTML: 'Aceptar'}).attr({type: 'button'}).appendTo(modal_footer)
                    button_acept.bind('click', function(e){
                        window.location.href = option.url_acept
                    })
                }
                else{
                    button_acept = $('<button>').prop({className: 'btn btn-sm bg-gradient-' + color + ' w-lg-25 m-0', innerHTML: 'Aceptar'})
                                    .attr({
                                        type: 'button',
                                        'data-bs-dismiss' : 'modal'
                                    }).appendTo(modal_footer)
                    button_acept.bind('click', function(e){
                        modal.remove()
                    })
                }
                return modal
            })

            $('.main-content').append(modal)
            $('#modalAlert').modal('show');
        };
        return{
            init : init
        }
    })();
    Validations.init();
});