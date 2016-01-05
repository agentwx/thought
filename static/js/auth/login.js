var Vue = require('vue');

Vue.config.delimiters = ['${', '}'];
var vue = new Vue({
    el: "#app",
    data: {
        message: 'hello'
    },
    methods: {
        login: function (api) {
            var email = $('#email').val();
            var password = $('#password').val();
            console.log(this);
            $.ajax({
                async: true,
                url: api,
                data: JSON.stringify({email: email, password: password}),
                type: 'post',
                dataType: 'json',
                success: function (resp) {
                    $(location).attr('href', '/auth/home');
                },
                error: function (XMLHttpRequest, textStatus) {
                    var status_code = XMLHttpRequest.status;
                    var body = JSON.parse(XMLHttpRequest.responseText);
                    alert(body.message)
                }
            });
            return false;
        }
    },
    components: {
        't-input': require('../components/Input.vue'),
        't-submit': require('../components/Submit.vue')
    }

});


