new Vue({
    el: '#contracts',
    delimiters: ['{$','$}'],
    data:{
        code: '',
        registration_date: '',
        due_date: '',
        document: null,
        stts: true,
        icon_contract: 'privacy_tip'
    },
    methods: {
        onFileChange(e) {
            this.document = e.target.files[0]
        },
        CreateContract : function(){
            const fd = new FormData()
            fd.append('code', this.code)
            fd.append('registration_date', this.registration_date)
            fd.append('due_date', this.due_date)
            fd.append('document', this.document, this.document.name)
            fd.append('status', this.stts)
            var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };
            axios({
                method: 'POST',
                url: '../api/contract/create/',
                headers: headers,
                data: fd
            })
            .then( function(response){
                $("#contracts").modal('hide');
                $("#icon-contract").removeClass('text-dark').addClass('text-success')
                $("#icon-contract").children('i').html('verified_user')
                $("#code").html(response.data.code)
                $('#contract').val(response.data.id)
                console.log(response)
            })
            .catch(function(error){
                console.log(error)
            })
        }
    },
})