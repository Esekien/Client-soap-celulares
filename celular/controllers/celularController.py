from flask import Flask, request, redirect, url_for, flash, jsonify
from flask import Blueprint, render_template
from zeep import Client
import json

Route = Blueprint('Login',__name__)

class Loging():

    @Route.route('/',methods=['GET','POST'])
    def index():
        if request.method == 'POST': 
            url = 'https://serviciowebsoapunach.000webhostapp.com/index.php?wsdl'
            client = Client(wsdl=url)
            modelo = request.form['modelo']
            sistema_ope = request.form['sistema_operativo']
            ram = request.form['memoria_ram']
            memoria = request.form['memoria_interna']
            client.service.insertCelular(modelo,sistema_ope,ram,memoria)
            flash('Insertado correctamente')
            # ! data es los datos de las variables, provienen de js atraves de ajax 
            
            
            return redirect('/')
        else:
            return render_template('index.html')

    @Route.route('/consultar',methods=['GET','POST'])
    def get():
        if request.method == 'POST': 
            url = 'https://serviciowebsoapunach.000webhostapp.com/index.php?wsdl'
            
            client = Client(wsdl=url)
            id = request.form['id']
            resultado = client.service.ConsultarCelular(id)
            flash(resultado)
            return redirect('/consultar')
        else:
            return render_template('get.html')

    @Route.route('/eliminar',methods=['GET','POST'])
    def delete():
        if request.method == 'POST': 
            url = 'https://serviciowebsoapunach.000webhostapp.com/index.php?wsdl'
            client = Client(wsdl=url)
            id = request.form['id']
            client.service.borrarCelular(id)
            flash('eliminado correctamente')
            
            return redirect('/eliminar')
        else:
            return render_template('delete.html')

    @Route.route('/modificar',methods=['GET','POST'])
    def put():
        if request.method == 'POST': 
            url = 'https://serviciowebsoapunach.000webhostapp.com/index.php?wsdl'
            client = Client(wsdl=url)
            id = request.form['id']
            modelo = request.form['modelo']
            sistema_ope = request.form['sistema_operativo']
            ram = request.form['memoria_ram']
            memoria = request.form['memoria_interna']
            client.service.modificarCelular(id,modelo,sistema_ope,ram,memoria)
            flash('Modificado correctamente')
            
            
            
            return redirect('/modificar')
        else:
            return render_template('put.html')