<template>
    <label for="${ cid }" class="col-sm-2 control-label"></label>
    <div class="col-sm-10">
        <input type="${ ctype }" class="form-control" id="${ cid }" name="${ cid }" placeholder="${ desc }" v-model="value" @blur="valid" />
        <p class="help-block">${ msg }</p>
    </div>
</template>

<script>
    var utils = require('../utils.js');
    module.exports = {
        props: ['cid', 'desc', 'ctype', 'msg'],
        data: function  () {
            return {value: ""}
        },
        methods: {
            valid: function () {
                if (this.cid == 'email'){
                    if (utils.valid_email(this.value)){
                        this.$parent.$data.email.emailError = true;
                        this.$parent.$data.email.emailErrorMsg = "invalid email";

                    }else {
                        this.$parent.$data.email.emailError = false;
                        this.$parent.$data.email.emailErrorMsg = "";
                    }
                }else if (this.cid == 'password'){
                    if (utils.valid_password(this.value)){
                        this.$parent.$data.password.passwordError = true;
                        this.$parent.$data.password.passwordErrorMsg = "invalid password, must be 6 -- 24 numbers and letter";
                    }else {
                        this.$parent.$data.password.passwordError = false;
                        this.$parent.$data.password.passwordErrorMsg = "";
                    }
                }else if (this.cid == 'confirm'){

                    var confirm = this.value
                    var password = $("#password").val().trim();

                    if (confirm != password){
                        this.$parent.$data.confirm.confirmError = true;
                        this.$parent.$data.confirm.confirmErrorMsg = "password and comfirm must be the same";
                    }else {
                        this.$parent.$data.confirm.confirmError = false;
                        this.$parent.$data.confirm.confirmErrorMsg = "";
                    }
                }
            }
        }
    }
</script>