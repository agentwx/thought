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
        motto: {
            mottoError: false,
            mottoErrorMsg: "",
            mottoLength: 20
        }
    },
    methods: {
        add: function (api) {
            var text = $("#motto").val().trim();
            

             // 提交验证
            if (utils.valid_motto(text, this.motto.mottoLength)){
                this.motto.mottoError = true;
                this.motto.mottoErrorMsg = "motto text must be less than " + this.motto.mottoLength + " lettes";
            }else{
                this.motto.mottoError = false;
                this.motto.mottoErrorMsg = "";
            }
            if (this.motto.mottoError) {
                return false
            }else {
                $.ajax({
                    async: true,
                    url: api,
                    type: 'post',
                    data: JSON.stringify({text: text}),
                    dataType: 'json',
                    success: function (resp) {
                        console.log(resp)
                        swal({
                            title: "Post motto Successful",
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
        "t-textarea": require("../components/Textarea.vue"),
        "t-submit": require("../components/Submit.vue")
    },
    events: {
        "child-valid": function (value) {
            if (utils.valid_motto(value, this.motto.mottoLength)){
                this.motto.mottoError = true;
                this.motto.mottoErrorMsg = "motto text must be less than " + this.motto.mottoLength + " lettes";
            }else{
                this.motto.mottoError = false;
                this.motto.mottoErrorMsg = "";
            }  
        }
    }

});


