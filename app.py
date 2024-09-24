from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from bson import ObjectId
from datetime import datetime
from celery_worker import enviar_email_async  # Importar a tarefa do worker

app = Flask(__name__)
app.secret_key = 'gyqz nmrm erjy fmqb'

# Configuração do MongoDB
client = pymongo.MongoClient("mongodb+srv://toshiba:toshiba1@sitemadistribuido.ybqco.mongodb.net/?retryWrites=true&w=majority&appName=sitemadistribuido")
db = client['assistencia_tecnica']
clientes_collection = db['clientes']
chamados_collection = db['chamados']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        cliente_id = clientes_collection.insert_one({
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "endereco": endereco
        }).inserted_id
        flash(f"Cliente {nome} cadastrado com sucesso!")
        return redirect(url_for('index'))
    return render_template('cadastrar_cliente.html')

@app.route('/registrar_chamado', methods=['GET', 'POST'])
def registrar_chamado():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        descricao = request.form['descricao']
        cliente = clientes_collection.find_one({"_id": ObjectId(cliente_id)})
        if cliente:
            chamado = {
                "cliente_id": cliente_id,
                "descricao": descricao,
                "status": "Aberto",
                "data_abertura": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            chamados_collection.insert_one(chamado)
            flash("Chamado registrado com sucesso!")
            return redirect(url_for('index'))
        else:
            flash("Cliente não encontrado.")
    clientes = list(clientes_collection.find())
    return render_template('registrar_chamado.html', clientes=clientes)

@app.route('/enviar_email', methods=['GET', 'POST'])
def enviar_email_route():
    if request.method == 'POST':
        destinatario = request.form['destinatario']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        enviar_email_async.delay(destinatario, assunto, mensagem)  # Tarefa assíncrona
        flash("Email está sendo enviado!")
        return redirect(url_for('index'))
    return render_template('enviar_email.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
