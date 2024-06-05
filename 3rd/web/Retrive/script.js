const userDataForm = document.getElementById('userDataForm');
const retrieveButton = document.getElementById('retrieveButton');
const nameResult = document.getElementById('nameResult');
const emailResult = document.getElementById('emailResult');
const messageResult = document.getElementById('messageResult');
const genderResult = document.getElementById('genderResult');
const branchResult = document.getElementById('branchResult');
const registrationNumberResult = document.getElementById('registrationNumberResult');
const locationResult = document.getElementById('locationResult');
const resultDiv = document.getElementById('result');

// Store data in local storage on submit
userDataForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const branch = document.getElementById('branch').value;
    const registrationNumber = document.getElementById('registrationNumber').value;
    const location = document.getElementById('location').value;

    localStorage.setItem('userName', name);
    localStorage.setItem('userEmail', email);
    localStorage.setItem('userMessage', message);
    localStorage.setItem('userGender', gender);
    localStorage.setItem('userBranch', branch);
    localStorage.setItem('userRegistrationNumber', registrationNumber);
    localStorage.setItem('userLocation', location);

    alert('Data stored!');
});

// Retrieve data on button click
retrieveButton.addEventListener('click', () => {
    const name = localStorage.getItem('userName');
    const email = localStorage.getItem('userEmail');
    const message = localStorage.getItem('userMessage');
    const gender = localStorage.getItem('userGender');
    const branch = localStorage.getItem('userBranch');
    const registrationNumber = localStorage.getItem('userRegistrationNumber');
    const location = localStorage.getItem('userLocation');

    nameResult.textContent = 'Name: ' + name;
    emailResult.textContent = 'Email: ' + email;
    messageResult.textContent = 'Message: ' + message;
    genderResult.textContent = 'Gender: ' + gender;
    branchResult.textContent = 'Branch: ' + branch;
    registrationNumberResult.textContent = 'Registration Number: ' + registrationNumber;
    locationResult.textContent = 'Location: ' + location;

    resultDiv.style.display = 'block'; // Show result area
});
