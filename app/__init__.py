from flask import Flask #Importamos del módulo flask de la clase Flask que creará nuestra aplicación.
from flask_bootstrap import Bootstrap

app = Flask(__name__) #Creamos una nueva instancia de Flask y la asignamos a `app`
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'nunca-la-adivinaras'

from app import routes