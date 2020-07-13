from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError, EqualTo

class loginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class registrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validateUsername(self, username):
        user = user.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Nombre de usuario ya registrado. Elegí otro')

class clientesPaisForm(FlaskForm):	
    txtPais = StringField('País', render_kw={"placeholder": "Buscar Clientes"})
    btnBuscar = SubmitField('Buscar Clientes')

class clientesEdadForm(FlaskForm):  
    txtEdadMinina = IntegerField('Edad mínima:', render_kw={"placeholder": "Ingrese edad"})
    txtEdadMaxima = IntegerField('Edad máxima:', render_kw={"placeholder": "Ingrese edad"})
    btnBuscar = SubmitField('Buscar Clientes')

class clientesFechaForm(FlaskForm):
    dateFecha = DateField('Fecha de alta', render_kw={"placeholder": "yyyy-mm-dd"}, format='%Y-%m-%d')
    btnBuscar = SubmitField('Buscar Clientes')

class agregarClientesForm(FlaskForm):
    txtNombre = StringField('Nombre: ', validators=[DataRequired()])
    txtEdad = StringField('Edad: ', validators=[DataRequired()])
    txtDireccion = StringField('Dirección: ', validators=[DataRequired()])
    txtPais = StringField('País: ', validators=[DataRequired()])
    txtDocumento = StringField('Documento: ', validators=[DataRequired()])
    txtFechaAlta = StringField('Fecha Alta: ', render_kw={"placeholder": "yyyy-mm-dd"}, validators=[DataRequired()])
    txtCorreo = StringField('Correo Electrónico: ', validators=[DataRequired()])
    txtTrabajo = StringField('Trabajo: ', validators=[DataRequired()])
    btnAgregar = SubmitField('Agregar cliente')

class agregarProductoForm(FlaskForm):
    txtCodigo = StringField('Código: ', validators=[DataRequired()])
    txtDescripcion = StringField('Descripción: ', validators=[DataRequired()])
    txtPrecio = StringField('Precio: ', validators=[DataRequired()])
    txtCantidad = StringField('Cantidad: ', validators=[DataRequired()])
    btnAgregar = SubmitField('Agregar producto')