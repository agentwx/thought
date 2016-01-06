var Vue = require('vue');
var swal = require('sweetalert');
var utils = require('../utils.js');

var jQuery = $ = require('jquery');

window.jQuery = jQuery;

require('bootstrap');

require('../../css/sweetalert.css');



Vue.config.delimiters = ['${', '}'];

var vue = new Vue({
    el: "#app",
    data: {
        email: {
            emailError: false,
            emailErrorMsg: "",
        },
        password: {
            passwordError: false,
            passwordErrorMsg: ""
        },
        confirm: {
            confirmError: false,
            confirmErrorMsg: ""
        }
    },
    methods: {
        register: function (api) {
            var email = $("#email").val().trim();
            var password = $("#password").val().trim();
            var confirm = $("#confirm").val().trim();
            
            
            // 提交验证
            if (utils.valid_email(email)){
                this.email.emailError = true;
                this.email.emailErrorMsg = "invalid email";
            }else{
                this.email.emailError = false;
                this.email.emailErrorMsg = "";
            }

            if (utils.valid_password(password)){
                this.password.passwordError = true;
                this.password.passwordErrorMsg = "invalid password, must be 6 -- 24 numbers and letter";
            }else {
                this.password.passwordError = false;
                this.password.passwordErrorMsg = "";
            }

            if (password != confirm){
                this.confirm.confirmError = true;
                this.confirm.confirmErrorMsg = "password and comfirm must be the same";
            }else{
                this.confirm.confirmError = false;
                this.confirm.confirmErrorMsg = "";
            }

           
            if (this.email.emailError || this.email.passwordError || this.confirm.confirmError){
                return false
            }else {
                $.ajax({
                    async: true,
                    url: api,
                    data: JSON.stringify({email: email, password: btoa(password)}),
                    type: 'post',
                    dataType: 'json',
                    success: function (resp) {
                        console.log(resp)
                        swal({
                            title: "Register Successful",
                            type: "success",
                            timer: 2000,
                            allowOutsideClick: true
                        }, function(){
                            $(location).attr('href', '/home');
                        })
                    },
                    error: function (XMLHttpRequest, textStatus) {
                        var status_code = XMLHttpRequest.status;
                        var body = JSON.parse(XMLHttpRequest.responseText);
                        swal({
                            title: body.message,
                            type: "error",
                            timer: 2000,
                            allowOutsideClick: true
                        })
                    }
                });
                return false;
            }   
        }
    },
    components: {
        't-input': require('../components/Input.vue'),
        't-submit': require('../components/Submit.vue')
    }
});
