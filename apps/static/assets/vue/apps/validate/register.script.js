new Vue({
    el: '#routes',
    delimiters: ['{$','$}'],
    data:{
        id : '',
        route : 'hola',
        limit : '',
        status : false
    },
    methods : {
        RetisterRoute : function(){
            console.log(this.id)
        }
    }
})