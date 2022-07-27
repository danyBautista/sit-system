$(function(){
    Forms= (function(){
        var init = function(){
            formsave();
        },
        formsave = function(){
            $('#id_form').submit(function(e){
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
                    request = data.error
                    if(!data.hasOwnProperty('error'))
                    {
                        messageOK({
                            show_header: false,
                            lock_escape_key: true,
                        })
                    }
                    else{
                        var html = '<p class="text-xs">No se ha podido registrar por los siguientes problemas</p>'
                        html +=  '<ul class="list-group list-group-flush">'
                        console.log(request)
                        $.each(request, function(key, value){
                            html += '<li class="list-group-item"><strong class="text-uppercase">' + key + ': </strong>' + value + '</li>'
                        })
                        html += '</ul>'
                        messageOK({
                            show_header: false,
                            lock_escape_key: true,
                            status_save: 'error',
                            content: html,
                        })
                    }
                }).
                fail(function(jqXHR, textStatus, errorThrown){
                    console.log(textStatus + ': ' + errorThrown)
                }).
                always(function(data){
                    console.log("complete" + data)
                })

            })
        },
        messageOK = function(options){
            defaults = {
                show_header: true,
                lock_escape_key: false,
                title: 'Mensaje de bienvenida',
                status_save: 'success',
                content: 'El registro se guardo correctamente, en la base de datos.',
                url_acept: $('a.btn-link').attr('href')
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
                modal_dialog = $('<div>').prop({className: 'modal-dialog modal-dialog-centered'}).appendTo(modal)
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

                status_content = $('<div>').prop({className: 'text-sm d-flex'}).appendTo(modal_body)

                switch (option.status_save) {
                    case 'success':
                        icon = 'done';
                        color = option.status_save
                        break;
                    case 'error':
                        icon = 'warning'
                        color = 'warning'
                        break;
                    default:
                        break;
                }
                status_icon = $('<span>').prop({className: 'material-icons h2 text-' + color, innerHTML: icon}).appendTo(status_content)
                status_title = $('<div>').prop({className: 'mt-3 ms-2', innerHTML: option.content}).appendTo(status_content)

                button_acept = $('<button>').prop({className: 'btn btn-sm bg-gradient-danger w-lg-25 m-0', innerHTML: 'Aceptar'}).attr({type: 'button'}).appendTo(modal_footer)

                button_acept.bind('click', function(e){
                    window.location.href = option.url_acept
                })
                return modal
            })

            $('.main-content').append(modal)
            $('#modalAlert').modal('show');
        };
        return{
            init : init
        }
    })();
    Forms.init();
});
