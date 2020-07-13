import csv

def abrirCSV(strArchivo):
	"""
	Función para abrir archivos csv
		strArchivo -> el archivo que deseo abrir
		return -> los registros en un listado de diccionario
	"""
	r = []
	with open(strArchivo, 'r', encoding="utf8") as archivo2:
		archivo_csv = csv.DictReader(archivo2)
		for item in archivo_csv:
			r.append(item)
	return r

def abrirCSVsinUTF(strArchivo):
	"""
	Función para abrir archivos csv sin encoding="utf8"
		strArchivo -> el archivo que deseo abrir
		return -> los registros en un listado de diccionario
	"""
	r = []
	with open(strArchivo, 'r') as archivo2:
		archivo_csv = csv.DictReader(archivo2)
		for item in archivo_csv:
			r.append(item)
	return r

def validarUsuarioNuevo(strUsuario):
	"""
	Función para validar si el usuario existe
		strUsuario -> el usuario que deseo validar
		return boolean -> true si el usuario no existe y false si ya se encuentra en el archivo
	"""
	r = True
	listado = []
	usuarios = abrirCSVsinUTF('usuarios.csv')
	for item in usuarios:
		if strUsuario == item['usuario']:
			r = False
			return r
	return r
