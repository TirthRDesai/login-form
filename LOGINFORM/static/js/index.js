window.onload = function(){
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
    });
};



function submitSignUp(){
    var name = document.getElementById("nameInputSignUp").value;
    var email = document.getElementById("emailInputSignUp").value;
    var password = document.getElementById("passwordInputSignUp").value;
    $.ajax({
        method: 'POST',
        url: '/checkData/SignUp',
        data: {'name':name , 'email' : email, 'password': password},
        dataType: 'json',
        success: function(d){
            console.log(d);
        }   
    });
}

