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

const createIdentity = (event) => {
  event.preventDefault();

  let firstName = document.getElementById("fName").value.trim();
  let lastName = document.getElementById("lName").value.trim();
  let email = document.getElementById("email").value.trim();
  let password = document.getElementById("password").value;
  let passwordVerify = document.getElementById("passwordVerify").value;
  let dob = document.getElementById("dob").value;
  let pin = document.getElementById("pin").value;

  if (password !== passwordVerify) {
    alert("Passwords do not match!");
    return;
  }

  if (pin.length < 4 || isNaN(pin)) {
    alert("PIN must be at least 4 digits long and numeric.");
    return;
  }

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
