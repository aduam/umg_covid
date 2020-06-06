"""Importando las librerías"""
from flask import Flask, request, render_template, jsonify
"""Importando la librería de prolog"""
from pyswip.prolog import Prolog
from config import config

def create_app(enviroment):
  app = Flask(__name__)
  app.config.from_object(enviroment)

  return app

enviroment = config['production']

app = create_app(enviroment)

"""Función de la lógica de prolog"""
def prol(prolog):
  """Instanciando prolog"""
  prolo = Prolog()

  """Llamando el archivo de prolog"""
  prolo.consult("proyecto_final.pl")

  """Leyendo las variables de prolog"""
  peso = prolog['peso']
  fiebre = prolog['fiebre']
  fatiga = prolog['fatiga']
  tos_seca = prolog['tos_seca']
  falta_apetito = prolog['falta_apetito']
  dolor_cuerpo = prolog['dolor_cuerpo']
  dificultad_respirar = prolog['dificultad_respirar']
  mucosidad = prolog['mucosidad']

  """calculando los datos que vienen de prolog"""
  h = int(fiebre) * 20
  i = int(fatiga) * 20
  j = int(tos_seca) * 20
  k = int(falta_apetito) * 10
  l = int(dolor_cuerpo) * 10
  m = int(dificultad_respirar) * 10
  n = int(mucosidad) * 3
  r = h + i + j + k + l + m + n

  """Declarando la variable que devolverá la función"""
  result = {
    'total_covid': r,
    'farmacias': [
      { 'titulo': 'Farmacia Galeno', 'direccion': '1A. Calle Y 2A. Av. Lote 13 "A", Jocotales Zona 6 Chinautla, Guatemala' },
      { 'titulo': 'Farmacia Galeno', 'direccion': '1a. Calle Lote H1, Zona 0 Colonia El Sauzalito Chinautla, Guatemala' },
      { 'titulo': 'Farmacia Galeno', 'direccion': '15a. Avenida 15-78, Zona 6, Guatemala, Guatemala' },
      { 'titulo': 'Farmacia Galeno', 'direccion': '15 Avenida 10-67 Zona 6 Guatemala' },
      { 'titulo': 'Farmacia Galeno', 'direccion': '15 Calle C 15-72, Cdad. de Guatemala' },
      { 'titulo': 'Farmacia RH', 'direccion': '16 Avenida A 19-04, Cdad. de Guatemala' },
      { 'titulo': 'Farmacia Cruz Verde', 'direccion': '15 Avenida, Cdad. de Guatemala ' },
      { 'titulo': 'Farmacia Similares', 'direccion': '27 Calle Proyectos 4-3' },
      { 'titulo': 'Farmacia El Socorro', 'direccion': '3A Calle Colonia Sauzalito' },
    ],
    'fiebre': {
      'titulo': 'Fiebre',
      'medicina': [
        { 'titulo': 'Acetaminofén', 'precio': 5.00 },
        { 'titulo': 'Ibuprofeno', 'precio': 10.50 },
        { 'titulo': 'Aspirina', 'precio': 8.15 },
      ],
    } if fiebre == '1' else False,
    'fatiga': {
      'titulo': 'Fatiga',
      'medicina': [
        { 'titulo': 'Cafeína', 'precio': 15.00 },
        { 'titulo': 'Metilfenidato', 'precio': 18.50 },
        { 'titulo': 'Dextroafetamina', 'precio': 30.54 },
        { 'titulo': 'Modafinilo', 'precio': 21.75 },
      ],
    } if fatiga == '1' else False,
    'tos_seca': {
      'titulo': 'Tos seca',
      'medicina': [
        { 'titulo': 'Levodropropizina', 'precio': 40.41 },
        { 'titulo': 'Dropropizina', 'precio': 50.50 },
        { 'titulo': 'Dextrometorfano', 'precio': 75.00 },
        { 'titulo': 'Cloval', 'precio': 65.00 },
      ],
    } if tos_seca == '1' else False,
    'falta_apetito': {
      'titulo': 'Falta de apetito',
      'medicina': [
        { 'titulo': 'Aceite de pescado', 'precio': 150 },
        { 'titulo': 'Iproheptadina', 'precio': 109.50 },
        { 'titulo': 'Pizotifeno', 'precio': 85.50 },
      ],
    } if falta_apetito == '1' else False,
    'dolor_cuerpo': {
      'titulo': 'Dolor de cuerpo',
      'medicina': [
        { 'titulo': 'Ibuprofeno', 'precio': 10.50 },
        { 'titulo': 'Paracetamol', 'precio': 35.60 },
        { 'titulo': 'Dipirona', 'precio': 40.45 },
      ],
    } if dolor_cuerpo == '1' else False,
    'dificultad_respirar': {
      'titulo': 'Dificultad al respirar',
      'medicina': [
        { 'titulo': 'Albuterol', 'precio': 10.90 },
        { 'titulo': 'Levalbuterol', 'precio': 50.45 },
        { 'titulo': 'Combivent', 'precio': 180 },
      ],
    } if dificultad_respirar == '1' else False,
    'mucosidad': {
      'titulo': 'Mucosidad',
      'medicina': [
        { 'titulo': 'Ambroxol', 'precio': 95.30 },
        { 'titulo': 'Mucovital', 'precio': 39.50 },
      ],
    } if mucosidad == '1' else False,
  }
  """Retornando el diccionario con los datos devueltos de prolog"""
  return result

"""Ruta principal"""
@app.route('/')
def index():
  return render_template('hello.html')

"""Ruta del solicitud a prolog tipo api con el método POST"""
@app.route('/prologrequest', methods=['GET', 'POST'])
def prologrequest():
  """Obteniendo los datos del cliente (navegador)"""
  data = request.get_json(force=True)

  """Llamando a la función que tiene la lógica de prolog"""
  prolog = prol(data)

  """Retornando al cliente un JSON con los datos de la solicitud"""
  return jsonify(
    total_covid=prolog['total_covid'],
    fiebre=prolog['fiebre'],
    fatiga=prolog['fatiga'],
    tos_seca=prolog['tos_seca'],
    falta_apetito=prolog['falta_apetito'],
    dolor_cuerpo=prolog['dolor_cuerpo'],
    dificultad_respirar=prolog['dificultad_respirar'],
    mucosidad=prolog['mucosidad'],
    farmacias=prolog['farmacias'],
  )

"""Instanciando y levantando el servidor"""
if __name__ == '__main__':
    app.run(debug=True)