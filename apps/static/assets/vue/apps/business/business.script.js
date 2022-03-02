new Vue({
    el: '#business',
    delimiters: ['{$', '$}'],
    data: {
        ruc : '',
        business_name : '',
        address : '',
        phone : '',
        webpage : '',
        registration_date : '',
        opening_date : '',
        logo_small_path : '',
        logo_large_path : '',
        business_description : '',
        geographic_location : '',
        economic_activitie : [],
        list_activities: [],
        status : false,
        kword : ''
    },
    watch: {
        kword: function (val){
            this.SearchEconomicActivities(val)
        }
    },
    methods : {
        SearchEconomicActivities : function(kword){
            var self = this;
            axios.get('../control/api/ecoact/search/?kword=' + kword)
            .then( function (response){
                self.economic_activitie = response.data
            })
            .catch( function(error){
                console.log(error)
            })
        },
        addActivity: function(Activity){
            this.kword = ''
            this.list_activities.push(Activity)
        },
        RegisterBusiness : function(){
            var CSRF_TOKEN = document.getElementsByName("csrfmiddlewaretoken")[0].value;

            let headers = {
                "X-CSRFToken": CSRF_TOKEN,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            };
            var data_type = {
                'name' : this.name,
                'status' : this.status
            };
            var list_id_activity = []
            for (let i = 0; i < this.list_activities.length; i++) {
                list_id_activity.push(this.list_activities[i].id)
            }
            var data_activity = {
                'ruc' : this.ruc,
                'business_name' : this.business_name,
                'address' : this.address,
                'phone' : this.phone,
                'webpage' : this.webpage,
                'registration_date' : this.registration_date,
                'opening_date' : this.opening_date,
                'business_description' : this.business_description,
                'economic_activitie' : list_id_activity,
                'status' : this.status
            }
            axios({
                method: 'POST',
                url: '../business/api/create/',
                headers: headers,
                data: data_activity
            })
            .then(function(response){
                console.log(response)
            })
            .catch(function(error){
                console.log(error)
            })
        }
    }
})