new Vue({
    el: '#message',
    delimiters: ['{$', '$}'],
    data: {
        gbMessage : 'bg-message',
        icon : '',
        title: '',
        content: '',
    },
    methods: {
        closeMessage : function()
        {
            this.bgMessage = 'bg-message'
            this.icon = '',
            this.title = '',
            this.content = '',
            $('#message').modal('hide')
        }
    },
})