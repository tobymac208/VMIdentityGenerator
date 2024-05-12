const download = (filename, text) => {
  var element = document.createElement("a");
  element.setAttribute(
    "href",
    "data:text/plain;charset=utf-8," + encodeURIComponent(text)
  );
  element.setAttribute("download", filename);

  element.style.display = "none";
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
};

const generatePassword = () => {
  const CHARACTERS_FOR_PASSWORD =
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ1234567890$!@#";
  const REQUIRED_LENGTH_OF_PASSWORD = 10;
  const MAXIMUM_LENGTH_OF_PASSWORD = 40;

  let length_of_password = REQUIRED_LENGTH_OF_PASSWORD;
  let generated_password = "";

  // Attempt to get the password length from the user.
  try {
    length_of_password = Number(
      document.getElementById("passwordLength").value
    );
  } catch (e) {
    alert(
      `Invalid password length. Using default length of ${REQUIRED_LENGTH_OF_PASSWORD}`
    );
  }

  if ( length_of_password > MAXIMUM_LENGTH_OF_PASSWORD || length_of_password < REQUIRED_LENGTH_OF_PASSWORD) {
    alert(
      `The password either too long or too short. Must be greater than ${REQUIRED_LENGTH_OF_PASSWORD} and less than or equal to the maximum of ${MAXIMUM_LENGTH_OF_PASSWORD}. Defaulting to ${REQUIRED_LENGTH_OF_PASSWORD}.`
    );
    length_of_password = REQUIRED_LENGTH_OF_PASSWORD;
  }

  for (let i = 0; i < length_of_password; i++) {
    generated_password +=
      CHARACTERS_FOR_PASSWORD[Math.floor(Math.random() * CHARACTERS_FOR_PASSWORD.length)];
  }

  // Upate the elements on the page with the new password.
  document.getElementById("password").value = generated_password;
  document.getElementById("passwordVerify").value = generated_password;
};

const createIdentity = (event) => {
  event.preventDefault();

  let firstName = document.getElementById("fName").value.trim();
  let lastName = document.getElementById("lName").value.trim();
  let email = document.getElementById("email").value.trim();
  let password = document.getElementById("password").value;
  let passwordVerify = document.getElementById("passwordVerify").value;
  let dob = document.getElementById("dob").value;
  let pin = document.getElementById("pin").value;

  const PIN_MIN_LENGTH = 4;

  if (password !== passwordVerify) {
    alert("Passwords do not match!");
    return;
  }

  if (pin.length < PIN_MIN_LENGTH || isNaN(pin)) {
    alert(`PIN must be at least ${PIN_MIN_LENGTH} digits long and numeric.`);
    return;
  }

  // Collect all of the information and send it over to the textarea element on the page. Allows the user to save all of the information.
  let identityInformation =
    "Name: " +
    firstName +
    " " +
    lastName +
    "\nEmail: " +
    email +
    "\nPassword: " +
    password +
    "\nDate of birth: " +
    dob +
    "\nPIN: " +
    pin;
  document.getElementById("identityInformation").value = identityInformation; // Populates the field on the page.
  document.getElementById("filename").value = firstName[0] + lastName + ".txt"; // Generates a filename

  // Further processing (e.g., sending data to the server) should go here.
  console.log({
    firstName,
    lastName,
    email,
    password, // In real applications, never log or expose passwords.
    dob,
    pin,
  });
};

document
  .getElementById("identityForm")
  .addEventListener("submit", createIdentity);
