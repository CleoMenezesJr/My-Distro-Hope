function login() {
  let username = document.getElementById('loginUsername').value
  let password = document.getElementById('loginPassword').value
  let csrf = document.getElementById('csrf').value

  if (username == '' && password == '') {
    alert('You must enter both')
  }

  let data = {
    'username' : username,
    'password' : password,
  }

  fetch('/api/login/' , {
      method : 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken' : csrf,
      },

      body : JSON.stringify(data)
  }).then(result => result.json())
  .then(response => {

    if (response.status == 200) {
      window.location.href = '/'
    }
    else {
      alert(response.message)
    }
  })

}

