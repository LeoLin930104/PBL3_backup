function signIn() {
  alert('Sign In clicked!');
}

function signUp() {
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if (password === confirmPassword) {
    alert('Account created for ' + name + ' with email ' + email);
  } else {
    alert('Passwords do not match!');
  }
}

function recommendRoutes() {
  alert('Recommend Me Routes clicked!');
}

var map = L.map('map').setView([35.6895, 139.6917], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

var shrines = [
  { name: 'Shrine 1', lat: 35.6895, lng: 139.6917 },
  { name: 'Shrine 2', lat: 35.688, lng: 139.692 },
  { name: 'Shrine 3', lat: 35.687, lng: 139.693 }
];

shrines.forEach(shrine => {
  L.marker([shrine.lat, shrine.lng]).addTo(map)
    .bindPopup(shrine.name)
    .openPopup();
});
