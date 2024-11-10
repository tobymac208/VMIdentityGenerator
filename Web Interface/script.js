/**
 * Handles secure random password generation
 */
class PasswordGenerator {
  static generateSecureRandom(max) {
    const array = new Uint32Array(1);
    crypto.getRandomValues(array);
    return array[0] % max;
  }

  static createPhrasePassword() {
    const words = [
      'Secure', 'Random', 'Password', 'Generator', 'Complex', 'Unique',
      'Strong', 'Safe', 'Protected', 'Private', 'Encrypted', 'Shield',
      'Guard', 'Defend', 'Protect', 'Lock'
    ];
    const special = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    const numbers = '0123456789';

    const components = [
      words[this.generateSecureRandom(words.length)],
      words[this.generateSecureRandom(words.length)],
      numbers[this.generateSecureRandom(10)],
      numbers[this.generateSecureRandom(10)],
      special[this.generateSecureRandom(special.length)],
      special[this.generateSecureRandom(special.length)]
    ];

    // Shuffle components for additional security
    for (let i = components.length - 1; i > 0; i--) {
      const j = this.generateSecureRandom(i + 1);
      [components[i], components[j]] = [components[j], components[i]];
    }

    return components.join('');
  }
}

/**
* Manages identity information with secure data handling
*/
class Identity {
  #actualPin;        // Private field for PIN
  #actualPassword;   // Private field for password

  constructor(vmName, firstName, lastName, email, dob, pin, password) {
    this.vmName = this.sanitizeInput(vmName);
    this.firstName = this.sanitizeInput(firstName);
    this.lastName = this.sanitizeInput(lastName);
    this.email = this.sanitizeInput(email);
    this.dob = this.sanitizeInput(dob);
    this.#actualPin = pin;
    this.#actualPassword = password;
    this.pin = '****';
    this.password = '********';
  }

  sanitizeInput(input) {
    const div = document.createElement('div');
    div.textContent = String(input).trim();
    return div.innerHTML;
  }

  identityDetails() {
    return `Virtual Machine: ${this.vmName}
Name: ${this.firstName} ${this.lastName}
Email: ${this.email}
Date of Birth: ${this.dob}
PIN: ${this.pin}
Password: ${this.password}`;
  }

  getDownloadContent() {
    return `Identity Details for VM: ${this.vmName} (Keep Secure)
=========================
Name: ${this.firstName} ${this.lastName}
Email: ${this.email}
Date of Birth: ${this.dob}
PIN: ${this.#actualPin}
Password: ${this.#actualPassword}

Generated: ${new Date().toLocaleString()}
Keep this information private and secure.`;
  }
}
document.addEventListener('DOMContentLoaded', () => {
  // Element selections using a more maintainable object structure
  const elements = {
    form: document.getElementById('identityForm'),
    results: document.getElementById('results'),
    inputs: {
      vmName: document.getElementById('vmName'),
      firstName: document.getElementById('firstName'),
      lastName: document.getElementById('lastName'),
      email: document.getElementById('email'),
      dob: document.getElementById('dob'),
      pin: document.getElementById('pin'),
      confirmPin: document.getElementById('confirmPin'),
      password: document.getElementById('password'),
      confirmPassword: document.getElementById('confirmPassword'),
      generatePassword: document.getElementById('generatePassword')
    },
    buttons: {
      changeEmail: document.getElementById('changeEmail'),
      generateIdentity: document.getElementById('generateIdentity'),
      downloadIdentity: document.getElementById('downloadIdentity'),
      createNew: document.getElementById('createNew')
    },
    display: {
      identityDetails: document.getElementById('identityDetails')
    }
  };

  // Enhanced validation functions with better error messages
  const validators = {
    vmName: (value) => ({
      isValid: /^[A-Za-z0-9\s-]+$/.test(value),
      message: 'VM Name can only contain letters, numbers, spaces, and hyphens'
    }),
    name: (value) => ({
      isValid: /^[A-Za-z\s-]+$/.test(value),
      message: 'Name can only contain letters, spaces, and hyphens'
    }),
    email: (value) => ({
      isValid: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
      message: 'Please enter a valid email address'
    }),
    pin: (value) => ({
      isValid: /^\d{4}$/.test(value),
      message: 'PIN must be exactly 4 digits'
    }),
    date: (value) => {
      const selectedDate = new Date(value);
      const today = new Date();
      const minDate = new Date();
      minDate.setFullYear(today.getFullYear() - 120); // Reasonable maximum age

      return {
        isValid: selectedDate < today && selectedDate > minDate,
        message: `Date of birth must be between ${minDate.toLocaleDateString()} and ${today.toLocaleDateString()}`
      };
    },
    password: (value) => {
      const checks = {
        length: value.length >= 8,
        uppercase: /[A-Z]/.test(value),
        lowercase: /[a-z]/.test(value),
        number: /\d/.test(value),
        special: /[!@#$%^&*(),.?":{}|<>]/.test(value)
      };

      const failed = Object.entries(checks)
        .filter(([, passes]) => !passes)
        .map(([check]) => check);

      return {
        isValid: failed.length === 0,
        message: failed.length > 0 ? getPasswordErrorMessage(failed) : ''
      };
    }
  };

  function getPasswordErrorMessage(failedChecks) {
    const messages = {
      length: 'at least 8 characters',
      uppercase: 'an uppercase letter',
      lowercase: 'a lowercase letter',
      number: 'a number',
      special: 'a special character'
    };

    const missing = failedChecks.map(check => messages[check]);
    return `Password must contain ${missing.join(', ')}`;
  }

  function updateEmail() {
    if (validators.name(elements.inputs.firstName.value).isValid &&
      validators.name(elements.inputs.lastName.value).isValid) {
      elements.inputs.email.value = `${elements.inputs.firstName.value}.${elements.inputs.lastName.value}@outlook.com`
        .toLowerCase()
        .replace(/[^a-z.@]/g, '');
    }
  }

  function togglePasswordFields(disabled) {
    elements.inputs.password.disabled = disabled;
    elements.inputs.confirmPassword.disabled = disabled;
    if (disabled) {
      elements.inputs.password.value = '';
      elements.inputs.confirmPassword.value = '';
      const errorDiv = elements.inputs.password.parentElement.querySelector('.password-error');
      if (errorDiv) errorDiv.remove();
    }
  }

  function validatePasswordInput(e) {
    const validation = validators.password(e.target.value);
    const existingError = elements.inputs.password.parentElement.querySelector('.password-error');

    if (existingError) existingError.remove();

    if (!validation.isValid) {
      const errorDiv = document.createElement('div');
      errorDiv.className = 'password-error';
      errorDiv.textContent = validation.message;
      elements.inputs.password.parentElement.appendChild(errorDiv);
    }
  }

  // Event Listeners
  [elements.inputs.firstName, elements.inputs.lastName].forEach(input => {
    input.addEventListener('input', updateEmail);
  });

  elements.buttons.changeEmail.addEventListener('click', () => {
    elements.inputs.email.readOnly = false;
    elements.inputs.email.focus();
  });

  elements.inputs.generatePassword.addEventListener('change', (e) => {
    togglePasswordFields(e.target.checked);
  });

  elements.inputs.password.addEventListener('input', validatePasswordInput);

  elements.buttons.generateIdentity.addEventListener('click', () => {
    // Validate all inputs
    const validations = {
      vmName: validators.vmName(elements.inputs.vmName.value),
      firstName: validators.name(elements.inputs.firstName.value),
      lastName: validators.name(elements.inputs.lastName.value),
      email: validators.email(elements.inputs.email.value),
      dob: validators.date(elements.inputs.dob.value),
      pin: validators.pin(elements.inputs.pin.value)
    };

    // Check for validation failures
    for (const [field, validation] of Object.entries(validations)) {
      if (!validation.isValid) {
        alert(validation.message);
        elements.inputs[field].focus();
        return;
      }
    }

    // Validate PIN confirmation
    if (elements.inputs.pin.value !== elements.inputs.confirmPin.value) {
      alert('PINs do not match!');
      elements.inputs.pin.focus();
      return;
    }

    // Handle password validation
    let finalPassword;
    if (elements.inputs.generatePassword.checked) {
      finalPassword = PasswordGenerator.createPhrasePassword();
    } else {
      const passwordValidation = validators.password(elements.inputs.password.value);
      if (!passwordValidation.isValid) {
        alert(passwordValidation.message);
        elements.inputs.password.focus();
        return;
      }

      if (elements.inputs.password.value !== elements.inputs.confirmPassword.value) {
        alert('Passwords do not match!');
        elements.inputs.password.focus();
        return;
      }
      finalPassword = elements.inputs.password.value;
    }

    // Create and display identity
    const identity = new Identity(
      elements.inputs.vmName.value,
      elements.inputs.firstName.value,
      elements.inputs.lastName.value,
      elements.inputs.email.value,
      elements.inputs.dob.value,
      elements.inputs.pin.value,
      finalPassword
    );

    elements.display.identityDetails.textContent = identity.identityDetails();
    elements.form.classList.add('hidden');
    elements.results.classList.remove('hidden');

    // Store identity temporarily for download
    elements.results.dataset.downloadContent = identity.getDownloadContent();
  });

  elements.buttons.downloadIdentity.addEventListener('click', async () => {
    try {
      // Configure save dialog options
      const options = {
        suggestedName: `${elements.inputs.vmName.value}_${elements.inputs.firstName.value}${elements.inputs.lastName.value}_identity.txt`,
        types: [{
          description: 'Text Files',
          accept: {
            'text/plain': ['.txt'],
          },
        }],
      };

      // Show save dialog
      const handle = await window.showSaveFilePicker(options);

      // Create file content
      const content = elements.results.dataset.downloadContent;
      const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });

      // Write the file
      const writable = await handle.createWritable();
      await writable.write(blob);
      await writable.close();

      // Clean up sensitive data
      delete elements.results.dataset.downloadContent;
    } catch (err) {
      // Handle if user cancels the save dialog
      if (err.name !== 'AbortError') {
        console.error('Failed to save file:', err);
        alert('Failed to save the identity file. Please try again.');
      }
    }
  });

  elements.buttons.createNew.addEventListener('click', () => {
    elements.form.reset();
    elements.form.classList.remove('hidden');
    elements.results.classList.add('hidden');
    elements.inputs.email.readOnly = true;
    togglePasswordFields(false);
    delete elements.results.dataset.downloadContent; // Clean up sensitive data
  });
});