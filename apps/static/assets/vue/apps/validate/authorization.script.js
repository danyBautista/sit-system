new Vue({
    el : '#authorization',
    delimiters: ['{$','$}'],
    data: {
        code : '',
        enabled : '',
        file : null,
        stts : true
    },
    methods: {
        onFileChange(e) {
            this.file = e.target.files[0]
        },
        createAuthorization : function(){
            const fd = new FormData()
            fd.append('code', this.code)
            fd.append('enable', this.enabled)
            fd.append('file', this.file, this.file.name)
            fd.append('status', this.stts)

            var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };
            axios({
                method: 'POST',
                url: '../api/authorization/create/',
                headers: headers,
                data: fd
            })
            .then( function(response){
                $("#authorization").modal('hide');
                $("#icon-authorization").removeClass('text-dark').addClass('text-success')
                $("#icon-authorization").children('i').html('verified_user')
                $("#code_autrization").html(response.data.code)
                $('#id_autorization').val(response.data.id)
                console.log(response)
            })
            .catch(function(error){
                console.log(error)
            })
        }
    },
})