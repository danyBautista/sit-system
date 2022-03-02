// register modal component
Vue.component("modal", {
  template: "#modal-template"
});
  // start app
new Vue({
    el: "#people",
    delimiters: ['{$','$}'],
    data: {
        showModal: false,
        dni : '',
        name:'',
        first_name:'',
        last_name:'',
        birth_date:'',
        address:'',
        phone:'',
        email:'',
        user_photo_path:'',
        sex:'',
        user:'',
        status: false,
        profile_information:''
    },
    methods: {
      register : function(){
        var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

        let headers = {
            "X-CSRFToken": CSRF_TOKEN,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        };
        data_create = {
          'dni' : this.dni,
          'name' : this.name,
          'first_name': this.first_name,
          'last_name': this.last_name,
          'birth_date': this.birth_date,
          'address': this.address,
          'phone': this.phone,
          'email': this.email,
          'sex' : this.sex,
          'status': this.status,
          'profile_information': this.profile_information
        }

        axios({
          method: 'POST',
          url: '../people/api/create/',
          headers: headers,
          data: data_create
        })
        .then( function(response){
          document.getElementById("people").hide();
          console.log(response)
        })
        .catch(function(error){
          console.log(error)
        })
      }
    },
});
