let formIsValid = true;

function checkPasswordMatch() {
    var password = $("#password").val();
    var confirmPassword = $("#confirm-password").val();

    if (password != confirmPassword) {
        $("#confirm-password").removeClass("is-valid").addClass("is-invalid");
        $("#password-feedback").removeClass("valid-feedback").addClass("invalid-feedback").text("Passwords do not match");
        formIsValid = false;
    } else {
        $("#confirm-password").removeClass("is-invalid").addClass("is-valid");
        $("#password-feedback").removeClass("invalid-feedback").addClass("valid-feedback").text("Passwords match");
        formIsValid = true;
    }
}


$("#signup-form").submit(function(event) {
    var password = $("#password").val();
    var confirmPassword = $("#confirm-password").val();
    if (password != confirmPassword) {
        event.preventDefault();
        $("#cnfrm-msg").html("Passwords do not match")
    }
});


const tagsInput = document.getElementById('story-tags');
tagsInput.addEventListener('input', function () {
    const tags = tagsInput.value.split(',');
    if (tags.length > 3) {
        alert('Please enter a maximum of 3 tags.');
        tags.pop(); // Remove the last tag entered
        tagsInput.value = tags.join(',');
    }
});

