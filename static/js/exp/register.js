const usernameField=document.querySelector('#usernameField');
const feedBackArea=document.querySelector('.invalid_feedback');
const emailField=document.querySelector('#emailField');
const passwordField=document.querySelector('#passwordField');
const emailfeedBackArea=document.querySelector('.emailfeedback');
const usernameSuccessOutput=document.querySelector('.usernameSuccessOutput');
const emailSuccessOutput=document.querySelector('.emailSuccessOutput');
const showPasswordToggle=document.querySelector('.showPasswordToggle');
const submitBtn=document.querySelector('.submit-btn');


const handleToggleInput = (e) => {
    if (showPasswordToggle.textContent === 'SHOW'){
        showPasswordToggle.textContent = 'HIDE';
        passwordField.setAttribute('type', 'text');

    } else {
        showPasswordToggle.textContent = 'SHOW';
        passwordField.setAttribute('type', 'password');
    }
};

showPasswordToggle.addEventListener('click', handleToggleInput);


emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;
    emailSuccessOutput.textContent=`Checking ${emailVal}`;
  
    emailField.classList.remove("is-invalid");
    emailfeedBackArea.style.display = "none";
  
    if (emailVal.length > 0) {
      fetch("/authentication/validate_email", {
        body: JSON.stringify({ email: emailVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
            emailSuccessOutput.style.display = 'none';
            if (data.username_error) {
                submitBtn.disbaled = true;
                usernameField.classList.add("is-invalid");
                emailfeedBackArea.style.display = "block";
                emailfeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
          } else {
              submitBtn.removeAttribute('disabled');
          } 
        });
    }
});


usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;
    usernameSuccessOutput.textContent=`Checking ${usernameVal}`;
    
  
    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display = "none";
  
    if (usernameVal.length > 0) {
      fetch("/authentication/validate_username", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
            usernameSuccessOutput.style.display = 'none';
            if (data.username_error) {
                usernameField.classList.add("is-invalid");
                feedBackArea.style.display = "block";
                feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
                submitBtn.disbaled = true;
            } else {
                submitBtn.removeAttribute('disabled');
            }
        });
    }
});