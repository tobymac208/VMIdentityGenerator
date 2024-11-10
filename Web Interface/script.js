class PasswordGenerator {
  static createPhrasePassword() {
      // Simple password generator - you can replace this with your actual password generation logic
      const words = ['Secure', 'Random', 'Password', 'Generator'];
      const numbers = Math.floor(Math.random() * 1000);
      const special = '!@#$%^&*';
      return words[Math.floor(Math.random() * words.length)] + 
             words[Math.floor(Math.random() * words.length)] + 
             numbers + 
             special[Math.floor(Math.random() * special.length)];
  }
}

class Identity {
  constructor(firstName, lastName, email, dob, pin, password) {
      this.firstName = firstName;
      this.lastName = lastName;
      this.email = email;
      this.dob = dob;
      this.pin = pin;
      this.password = password;
  }

  identityDetails() {
      return `Name: ${this.firstName} ${this.lastName}
Email: ${this.email}
Date of Birth: ${this.dob}
Password: ${this.password}
PIN: ${this.pin}`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('identityForm');
  const results = document.getElementById('results');
  const firstName = document.getElementById('firstName');
  const lastName = document.getElementById('lastName');
  const email = document.getElementById('email');
  const changeEmailBtn = document.getElementById('changeEmail');
  const dob = document.getElementById('dob');
  const pin = document.getElementById('pin');
  const confirmPin = document.getElementById('confirmPin');
  const generateBtn = document.getElementById('generateIdentity');
  const downloadBtn = document.getElementById('downloadIdentity');
  const createNewBtn = document.getElementById('createNew');
  const identityDetails = document.getElementById('identityDetails');

  // Update email when name changes
  [firstName, lastName].forEach(input => {
      input.addEventListener('input', () => {
          email.value = `${firstName.value}.${lastName.value}@outlook.com`.toLowerCase();
      });
  });

  // Handle email change
  changeEmailBtn.addEventListener('click', () => {
      email.readOnly = false;
      email.focus();
  });

  // Generate identity
  generateBtn.addEventListener('click', () => {
      if (pin.value !== confirmPin.value) {
          alert('PINs do not match!');
          return;
      }

      if (!firstName.value || !lastName.value || !email.value || !dob.value || !pin.value) {
          alert('Please fill in all fields!');
          return;
      }

      const password = PasswordGenerator.createPhrasePassword();
      const identity = new Identity(
          firstName.value,
          lastName.value,
          email.value,
          dob.value,
          pin.value,
          password
      );

      identityDetails.textContent = identity.identityDetails();
      form.classList.add('hidden');
      results.classList.remove('hidden');
  });

  // Download identity file
  downloadBtn.addEventListener('click', () => {
      const content = identityDetails.textContent;
      const blob = new Blob([content], { type: 'text/plain' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${firstName.value}${lastName.value}.txt`;
      a.click();
      window.URL.revokeObjectURL(url);
  });

  // Create new identity
  createNewBtn.addEventListener('click', () => {
      form.reset();
      form.classList.remove('hidden');
      results.classList.add('hidden');
  });
});