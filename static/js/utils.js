/**
 * Created by ghost on 16/1/5.
 */


function valid_email(email){
    return !/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,5}$/.test(email)
}

function valid_password(password){
    var pattern = /^(?!\D+$)(?![^a-zA-Z]+$).{6,20}$/
    return !pattern.test(password)
}

function valid_motto(text, length){
    return (text.length > length || text.length < 0) ? true : false
}


module.exports = {
    valid_email: valid_email,
    valid_password: valid_password,
    valid_motto: valid_motto
}