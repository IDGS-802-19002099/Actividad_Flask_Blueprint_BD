from flask import Blueprint
from db import get_connection

from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from flask_wtf.csrf import CSRFProtect

alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/consultaAlumnos', methods=['GET','POST'])
def consultaAlumnos():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consulta_alumnos()')
            resultset = cursor.fetchall()
        connection.close()
        
        return render_template('Alumnos.html', resultset = resultset)
    except Exception as ex: 
        print(ex)

@alumnos.route('/consultaAlumno', methods=['GET'])
def consultaAlumno():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consulta_alumno(%s)',(2))
            resultset = cursor.fetchall()
        connection.close()
        return {'key': resultset}
    except Exception as ex: 
        print(ex)

@alumnos.route('/insertarAlumno', methods=['GET','POST'])
def insertarAlumno():
    try:
        
        ID = (request.form.get('ID'))
        Nombre = (request.form.get('Nombre'))
        Apellido = (request.form.get('Apellido'))
        email = (request.form.get('email'))

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call agrega_alumnos(%s,%s,%s)',
                           (Nombre,Apellido,email))
        connection.commit()
        connection.close()
        
        return render_template('index.html')
    except Exception as ex: 
        print(ex)


@alumnos.route('/actualizarAlumno', methods=['GET','POST'])
def actualizarAlumno():
    try:
        # request.args.get('id')
        ID = (request.form.get('ID'))
        Nombre = (request.form.get('Nombre'))
        Apellido = (request.form.get('Apellido'))
        email = (request.form.get('email'))

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call actualizar_alumno(%s,%s,%s,%s)',
                           (ID,Nombre,Apellido,email))
        connection.commit()
        connection.close()
        
        return render_template('index.html')
    except Exception as ex: 
        print(ex)

@alumnos.route('/eliminarAlumno', methods=['GET','POST'])
def eliminarAlumno():
    try:
        
        ID=request.args.get('id')

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call borrar_alumno(%s)',
                           (ID))
        connection.commit()
        connection.close()
        
        return render_template('index.html')
    except Exception as ex: 
        print(ex)
        
@alumnos.route('/formularioAlumno', methods=['POST'])
def formularioAlumno():
    return render_template('InsertarAlumno.html')

@alumnos.route('/formularioActualizarAlumno', methods=['GET','POST'])
def formularioActualizarAlumno():

# request.args.get('id')
    ID = request.args.get('ID')
    Nombre = request.args.get('Nombre')
    Apellido = request.args.get('Apellido')
    email = request.args.get('email')
    
    return render_template('ActualizarAlumno.html', ID = ID, Nombre = Nombre, Apellido = Apellido, email = email)