#Necesario para hacer el renderizado HTML de las templates
from flask import render_template, redirect, url_for, flash, session
from app import app
from .forms import *
import csv
from .utilCsv import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    """
    Función que permite loggearse con usuario y contraseña
        return -> el template renderizado para loguearse
    """
    if not 'username' in session:
        formulario = loginForm()
        if formulario.validate_on_submit():
            with open('usuarios.csv') as archivo:
                archivo_csv = csv.reader(archivo)
                registro = next(archivo_csv)
                while registro:
                    if formulario.username.data == registro[0] and formulario.password.data == registro[1]:
                        print('postback success')
                        flash('Bienvenido/a')
                        session['username'] = formulario.username.data
                        return render_template('ingresoOK.html', nombre=session['username'])
                    registro = next(archivo_csv, None)
                else:
                    print('postback error')
                    flash('Ingresaste mal el usuario o contraseña. Reintenta')
                    return redirect(url_for('ingresar'))
        return render_template('login.html', formulario=formulario)
    else:
        return index()

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """
    Función que permite registrar un usuario y contraseña
        return -> el template renderizado para registrarse
    """
    formulario = registrationForm()
    if formulario.validate_on_submit():
        if formulario.password.data == formulario.password2.data:
            if validarUsuarioNuevo(formulario.username.data):               
                with open('usuarios.csv', 'a+', newline='') as archivo:
                    archivo_csv = csv.writer(archivo)
                    registro = [formulario.username.data, formulario.password.data]
                    archivo_csv.writerow(registro)
                flash('Usuario creado correctamente')
                return redirect(url_for('ingresar'))
            else:
                flash("Usuario previamente registrado")
        else:
            flash('Las passwords no coinciden')
    return render_template('registro.html', form=formulario)

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    """
    Función que muestra los clientes registrados
        return -> el template renderizado con los encabezados de la lista clientes 
        y las inserciones
    """
    iClientes = []
    iEncabezados = []    
    if 'username' in session:
        try:
            if not 'iClientes' in session:
                iClientes = abrirCSV('clientes.csv')
            else:
                iClientes = session['iClientes']
                
            iEncabezados = iClientes[0].keys()
            
        except Exception as e:
            flash('Error: ' + str(e))
        finally:
            return render_template('clientes.html', inserciones = iClientes, encabezados=iEncabezados)
    else:
        return ingresar()

@app.route('/clientesPaises', methods=['GET', 'POST'])
def clientesPais():
    """
    Función que muestra los clientes filtrados por país
        return -> el template renderizado con los encabezados de la lista clientes 
        y las inserciones
    """
    Clientes = []
    Encabezados = []    
    ClientesMostrados = []
    formulario = clientesPaisForm()
    if 'username' in session:
        if formulario.is_submitted(): 
            Clientes = abrirCSV('clientes.csv')
            session['Clientes'] = Clientes
            for item in Clientes:
                if str(item['País']).upper() == formulario.txtPais.data.upper():
                    ClientesMostrados.append(item)
            Encabezados = Clientes[0].keys()
            if ClientesMostrados == []:
                flash("No hay clientes en ese país")
        return render_template('clientesPais.html', inserciones=ClientesMostrados, encabezados=Encabezados, formulario=formulario)
    else:
        return ingresar()

@app.route('/clientesEdad', methods=['GET', 'POST'])
def clientesEdad():
    """
    Función que muestra los clientes filtrados por rango de edad
        return -> el template renderizado con los encabezados de la lista clientes 
        y las inserciones
    """
    Clientes = []
    Encabezados = []    
    ClientesMostrados = []
    formulario = clientesEdadForm()
    if 'username' in session:
        if formulario.is_submitted():
            Clientes = abrirCSV('clientes.csv')
            session['Clientes'] = Clientes
            for item in Clientes:
                if int(item['Edad']) >= formulario.txtEdadMinina.data and int(item['Edad']) <= formulario.txtEdadMaxima.data:
                    ClientesMostrados.append(item)
            Encabezados = Clientes[0].keys()
            if ClientesMostrados == []:
                flash("No hay clientes en ese rango etáreo")
        return render_template('clientesEdad.html', inserciones=ClientesMostrados, encabezados=Encabezados, formulario=formulario)
    else:
        return ingresar()

@app.route('/clientesFecha', methods=['GET', 'POST'])
def clientesFecha():
    """
    Función que muestra los clientes filtrados por fecha de alta
        return -> el template renderizado con los encabezados de la lista clientes 
        y las inserciones
    """
    Clientes = []
    Encabezados = []    
    ClientesMostrados = []
    formulario = clientesFechaForm()
    if 'username' in session:
        if formulario.is_submitted():
            Clientes = abrirCSV('clientes.csv')
            session['Clientes'] = Clientes
            for item in Clientes:
                if item['Fecha Alta'] == str(formulario.dateFecha.data):
                    ClientesMostrados.append(item)
            Encabezados = Clientes[0].keys()
            if ClientesMostrados == []:
                flash("No hay clientes dados de alta en esa fecha")
        return render_template('clientesFecha.html', inserciones=ClientesMostrados, encabezados=Encabezados, formulario=formulario)
    else:
        return ingresar()

@app.route('/agregarCliente', methods=['GET', 'POST'])
def agregarCliente():
    """
    Función que permite agregar un nuevo cliente
        return -> el template renderizado para ingresar el nuevo registro
    """
    nuevoCliente = []
    formulario = agregarClientesForm()
    if 'username' in session:
        if formulario.is_submitted():
            Clientes = abrirCSV('clientes.csv')
            for item in Clientes:
                if item['Documento'] != formulario.txtDocumento.data:
                    with open('clientes.csv', 'a+', newline="") as archivo:
                        archivo_csv = csv.writer(archivo)
                        registro = [formulario.txtNombre.data, formulario.txtEdad.data, formulario.txtDireccion.data, formulario.txtPais.data, formulario.txtDocumento.data, formulario.txtFechaAlta.data, formulario.txtCorreo.data, formulario.txtTrabajo.data ]
                        archivo_csv.writerow(registro)
                    flash("El cliente se registró correctamente")
                    return redirect(url_for('agregarCliente'))
                else:
                    flash("El cliente ya esta en la base de datos")
                    return render_template('agregarCliente.html', form=formulario)
            flash("El cliente se agregó correctamente")
        return render_template('agregarCliente.html', form=formulario)
    else:
        return ingresar()

@app.route('/agregarProducto', methods=['GET', 'POST'])
def agregarProducto():
    """
    Función que permite agregar un nuevo producto de venta.
        return -> el template renderizado para ingresar el nuevo registro
    """
    formulario = agregarProductoForm()
    if 'username' in session:
        if formulario.validate_on_submit():
            Productos = abrirCSV('productos.csv')
            for item in Productos:
                if item['codigo'] != formulario.txtCodigo.data:
                    with open('productos.csv', 'a+', newline="") as archivo:
                        archivo_csv = csv.writer(archivo)
                        registro = [formulario.txtCodigo.data, formulario.txtDescripcion.data, formulario.txtPrecio.data, formulario.txtCantidad.data]
                        archivo_csv.writerow(registro)
                    flash("El producto se registró correctamente")
                    return redirect(url_for('agregarProducto'))
                else:
                    flash("El producto ya esta previamente registrado")
                    return render_template('agregarProducto.html', form=formulario)
        return render_template('agregarProducto.html', form=formulario)
    else:
        return ingresar()

@app.route('/bienvenido', methods=['GET', 'POST'])
def bienvenido():
    """
    Función que informa que el usuario ingreso correctamente a la aplicación
        return -> el template renderizado con un mensaje de ingreso exitoso
    """
    if 'username' in session:
        return render_template('ingresoOK.html', usuario=formulario.username.data)
    else:
        return ingresar()

@app.route('/sobre')
def sobre():
    """
    Función que muestra datos del desarrollador e información relacionada
        return -> el template renderizado con la información
    """
    return render_template('sobre.html')

@app.errorhandler(404)
def no_encontrado(e):
    """
    Función que muestra un mensaje de excepción 404
        return -> el template renderizado con el mensaje
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    """
    Función que muestra un mensaje de excepción 500
        return -> el template renderizado con el mensaje
    """
    return render_template('500.html'), 500

@app.route('/logout', methods=['GET'])
def logout():
    """
    Función que cierra la sesion del usuario
        return -> el template renderizado con mensaje de logout exitoso
    """
    if 'username' in session:
        session.pop('username')
        return render_template('logout.html')
    else:
        return redirect(url_for('index'))