from flask import Flask, request, make_response, redirect, render_template, jsonify
#from pyswip.prolog import Prolog
from config import config

def create_app(enviroment):
  app = Flask(__name__)
  app.config.from_object(enviroment)

  return app

enviroment = config['production']

app = create_app(enviroment)

def prol(prolog):
  #prolo = Prolog()
  #prolo.consult("proyecto_final.pl")
  peso = prolog['peso']
  fiebre = prolog['fiebre']
  fatiga = prolog['fatiga']
  tos_seca = prolog['tos_seca']
  falta_apetito = prolog['falta_apetito']
  dolor_cuerpo = prolog['dolor_cuerpo']
  dificultad_respirar = prolog['dificultad_respirar']
  mucosidad = prolog['mucosidad']

  h = int(fiebre) * 20
  i = int(fatiga) * 20
  j = int(tos_seca) * 20
  k = int(falta_apetito) * 10
  l = int(dolor_cuerpo) * 10
  m = int(dificultad_respirar) * 10
  n = int(mucosidad) * 3
  r = h + i + j + k + l + m + n

  result = {
    'total_covid': r,
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
  return result

@app.route('/')
def index():
  return render_template('hello.html')

@app.route('/prologrequest', methods=['GET', 'POST'])
def prologrequest():
  data = request.get_json(force=True)
  result = prol(data)
  return jsonify(
    total_covid=result['total_covid'],
    fiebre=result['fiebre'],
    fatiga=result['fatiga'],
    tos_seca=result['tos_seca'],
    falta_apetito=result['falta_apetito'],
    dolor_cuerpo=result['dolor_cuerpo'],
    dificultad_respirar=result['dificultad_respirar'],
    mucosidad=result['mucosidad'],
  )

if __name__ == '__main__':
    app.run(debug=True)