const peso = document.querySelector('#input-peso');
const fiebre = document.querySelector('#input-fiebre');
const fatiga = document.querySelector('#input-fatiga');
const tosSeca = document.querySelector('#input-tos-seca');
const apetito = document.querySelector('#input-apetito');
const dolorCuerpo = document.querySelector('#input-dolor-cuerpo');
const dificultadRespira = document.querySelector('#input-respirar');
const tieneMucosidad = document.querySelector('#input-mucosidad');

function onSubmit(e) {
  e.preventDefault();
  console.log('evento enviado');
  const data = {
    peso: peso.value,
    fiebre: fiebre.value,
    fatiga: fatiga.value,
    tosSeca: tosSeca.value,
    apetito: apetito.value,
    dolorCuerpo: dolorCuerpo.value,
    dificultadRespira: dificultadRespira.value,
    tieneMucosidad: tieneMucosidad.value,
  };
  console.log(data);
  console.log('prologrequest')
  fetch('/prologrequest', {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .catch(error => console.error('Error:', error))
  .then(response => console.log('Success:', response));
}

const submit = document.querySelector('.form');
submit.addEventListener('submit', onSubmit);