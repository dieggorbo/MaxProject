import db
from flask import (Flask, Blueprint, flash, render_template, request, url_for)


app = Flask(__name__)
app.config["SECRET_KEY"] = "as987d48dgr3fn89wsdkjnsd67tg23dg"

@app.route('/', methods=('GET', 'POST'))
def contact():

  if request.method == 'POST':
    payload = {
      "name": request.form['name'],
      "email": request.form['email'],
      "sugestion": request.form['sugestion']
    }

    db.insert(payload)
    flash('Obrigado ' + request.form['name'] + ', sua sugestao foi enviada')
 
  return render_template('contato.html')
