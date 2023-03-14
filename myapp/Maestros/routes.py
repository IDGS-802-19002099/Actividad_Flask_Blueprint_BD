from flask import Blueprint

maestros = Blueprint('maestros',__name__)

from db import get_connection

from flask import Flask, redirect, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect

@maestros.route('/consultaMaestros', methods=['GET','POST'])
def consultaMaestros():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consulta_maestros()')
            resultset = cursor.fetchall()
        connection.close()
        
        return render_template('Maestros.html', resultset = resultset)
    except Exception as ex: 
        print(ex)

@maestros.route('/consultaMaestro', methods=['GET'])
def consultaMaestro():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consulta_maestro(%s)',(2))
            resultset = cursor.fetchall()
        connection.close()
        return {'key': resultset}
    except Exception as ex: 
        print(ex)

@maestros.route('/insertarMaestro', methods=['GET','POST'])
def insertarMaestro():
    try:
        
        ID = (request.form.get('ID'))
        Nombre = (request.form.get('Nombre'))
        Apellido = (request.form.get('Apellido'))
        email = (request.form.get('email'))

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call insertar_maestro(%s,%s,%s)',
                           (Nombre,Apellido,email))
        connection.commit()
        connection.close()
    
        return render_template('index.html')
      #  return render_template('InsertarMaestro.html')
    except Exception as ex: 
        print(ex)

@maestros.route('/formularioMaestro', methods=['POST'])
def formularioMaestro():
    return render_template('InsertarMaestro.html')




@maestros.route('/actualizarMaestro', methods=['GET','POST'])
def actualizarMaestro():
    try:
        # request.args.get('id')
        ID = (request.form.get('ID'))
        Nombre = (request.form.get('Nombre'))
        Apellido = (request.form.get('Apellido'))
        email = (request.form.get('email'))

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call actualizar_maestro(%s,%s,%s,%s)',
                           (ID,Nombre,Apellido,email))
        connection.commit()
        connection.close()
        
        return render_template('index.html')
    except Exception as ex: 
        print(ex)
        return render_template('index.html')

@maestros.route('/eliminarMaestro', methods=['GET','POST'])
def eliminarMaestro():
    try:
        
        ID=request.args.get('id')

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call borrar_maestro(%s)',
                           (ID))
        connection.commit()
        connection.close()
        
        return render_template('index.html')
    except Exception as ex: 
        print(ex)
        

@maestros.route('/formularioActualizarMaestro', methods=['GET','POST'])
def formularioActualizarMaestro():

# request.args.get('id')
    ID = request.args.get('ID')
    Nombre = request.args.get('Nombre')
    Apellido = request.args.get('Apellido')
    email = request.args.get('email')
    
    return render_template('ActualizarMaestros.html', ID = ID, Nombre = Nombre, Apellido = Apellido, email = email)