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

def sugerirElementoArchivo(strPedido, strCampoEspecificado, strArchivo):
	"""
	Función que me devuelve un listado de sugerencias segun el campo especificado
		strPedido -> el string que deseo encontrar
		strCampoEspecificado -> el campo donde deseo que se encuentre el string que envio de busqueda
		strArchivo -> el archivo donde deseo buscar el dato
	    return una lista con los resultados de busqueda
	"""
	resultado = []
	Listado = abrirCSV(strArchivo)
	for item in Listado:
			if strPedido in item[strCampoEspecificado]:
				listado.append(item)

	return resultado