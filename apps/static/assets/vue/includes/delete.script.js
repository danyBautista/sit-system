$(function(){
    DeleteSoft= (function(){
        var init = function(){
            SelectRegister();
            DeleteRegister();
        },
        SelectRegister = function(){
            $('#delete').bind('click', function(e){
                $('#ID_code').html($(this).data("get-id"))
                $('#id_name').html($(this).data("get-name"))
                $('#id_update_at').html($(this).data("get-update"))
                $('#id_image').attr('src', $(this).data("get-image"))
            })
        },
        DeleteRegister = function(){
            $('form#deleteForm').on('submit', function(e){
                e.preventDefault();
                var parameters = $(this).serializeArray();
                $.ajax({
                    url: $(this).attr('action')+$('#ID_code').html(),
                    type: 'POST',
                    data: parameters,
                    dataType: 'json'
                }).done(function(data){
                    console.log(data);
                    if(!data.hasOwnProperty('error')){
                        location.href = window.location.pathname
                    }
                    message_error(data.error);
                }).fail(function(jqXHR, textStatus, errorThrown){
                    alert(textStatus + ': ' + errorThrown)
                }).always(function(data){

                });
            })
        };
        return{
            init : init
        }
    })();
    DeleteSoft.init();
});
