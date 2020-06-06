/* Obteniendo los archivos del html */
const peso = document.querySelector('#input-peso')
const fiebre = document.querySelector('#input-fiebre')
const fatiga = document.querySelector('#input-fatiga')
const tosSeca = document.querySelector('#input-tos-seca')
const apetito = document.querySelector('#input-apetito')
const dolorCuerpo = document.querySelector('#input-dolor-cuerpo')
const dificultadRespira = document.querySelector('#input-respirar')
const tieneMucosidad = document.querySelector('#input-mucosidad')
const tbody = document.querySelector('.tbody')

/* Función en dónde se le envían los datos al servidor */
function onSubmit(e) {
  e.preventDefault()
  const data = {
    peso: peso.value,
    fiebre: fiebre.value,
    fatiga: fatiga.value,
    tos_seca: tosSeca.value,
    falta_apetito: apetito.value,
    dolor_cuerpo: dolorCuerpo.value,
    dificultad_respirar: dificultadRespira.value,
    mucosidad: tieneMucosidad.value,
  }
  /* Enviando la solicitud POST al servidor */
  fetch('/prologrequest', {
    method: 'POST',
    body: JSON.stringify(data),
    headers:{
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .catch(error => console.error('Error:', error))
  .then(response => {
    /* Solicitud éxitosa de parte del servidor */
    const resultado = document.querySelector('.resultado')
    const farmacias = document.querySelector('.farmacias')
    resultado.innerHTML = '';
    tbody.innerHTML = '';
    farmacias.style.display = 'none';
    resultado.style.display = 'flex'
    resultado.insertAdjacentHTML('afterbegin', `<h4>Usted ${response['total_covid'] > 90 ? '' : 'no'} tiene covid</h4>`)
    resultado.insertAdjacentHTML('afterbegin', `<h3>Resultado: <span style="color:${response['total_covid'] > 90 ? 'red' : 'white'}">${response['total_covid']}%</span></h3>`)

    const container = document.createElement('div')
    container.style.display = 'flex'
    container.style.flexWrap = 'wrap'
    if (Object.keys(response).length > 0) {
      resultado.insertAdjacentHTML('beforeend', `<p style="margin: 8px 0; font-size: 13px; font-weight: bold;">Usted puede tomar los siguientes medicamentos:</p>`)
    }
    /* Recorriendo lla respueesta de los síntomas */
    Object.keys(response).reduce((acc, cur) => {
      if (response[cur]) {
        if (cur !== 'total_covid') {
          if (cur !== 'farmacias') {
            farmacias.style.display = 'flex';
            map.style.display = 'block';
            const div = document.createElement('div')
            div.style.display = 'flex'
            div.style.flexDirection = 'column'
            div.style.width = '230px'
            div.style.padding = '16px 0'
            const p1 = document.createElement('p')
            p1.style.margin = '8px 0'
            p1.style.fontSize = '12px'
            p1.style.fontWeight = '700'
            const textP1 = document.createTextNode(`Para ${response[cur].titulo}:`)
            p1.appendChild(textP1)
            div.appendChild(p1)
            container.appendChild(div)

            response[cur].medicina.reduce((a, e) => {
              const p2 = document.createElement('p')
              p2.style.margin = '0 0 2px 0'
              const textP2 = document.createTextNode(`${e.titulo} - Precio: Q. ${e.precio}`)
              p2.appendChild(textP2)
              div.appendChild(p2)
              container.appendChild(div)
            })
          }
        }
      }
    })
    /* Recorriendo la respuesta de las farmacias */
    response['farmacias'].forEach(e => {
      const tr = document.createElement('tr')
      const t1 = document.createElement('td')
      const t2 = document.createElement('td')
      const pt1 = document.createElement('p')
      const pt2 = document.createElement('p')
      const th1 = document.createTextNode(`${e.titulo}`)
      const th2 = document.createTextNode(`${e.direccion}`)
      pt1.appendChild(th1)
      pt2.appendChild(th2)
      t1.appendChild(pt1)
      t2.appendChild(pt2)
      tr.appendChild(t1)
      tr.appendChild(t2)
      tbody.appendChild(tr)
    })
    resultado.appendChild(container)
  });
}

/* Obteniendo los elementos del archivo html */
const submit = document.querySelector('.form');
submit.addEventListener('submit', onSubmit);