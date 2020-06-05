from flask import Flask, request, make_response, redirect, render_template, jsonify
from pyswip.prolog import Prolog

app = Flask(__name__)

def prol():
  prolog = Prolog()
  prolog.assertz('father(michael,john)')
  prolog.assertz("father(michael,gina)")
  list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
  for soln in prolog.query("father(X,Y)"):
      print(soln["X"], "is the father of", soln["Y"])

@app.route('/home')
def index():
  return render_template('hello.html')

@app.route('/prologrequest', methods=['GET', 'POST'])
def prologrequest():
  print('begin')
  prol()
  print('end')
  return jsonify(
    peso=123,
    fiebre=True,
    tos=False,
  )