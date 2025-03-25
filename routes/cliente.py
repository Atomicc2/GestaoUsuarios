from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

'''
Rotas dos clientes:

    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET) - Renderiza o formlário para cadastrar no cliente
    - /clientes/<id> (GET) - Renderiza os dados de um cliente
    - /clientes/<id>/edit (GET) - Renderiza o formulário para atuazaliar os dados de um cliente
    - /clientes/<id>/update (PUT) - Atualiza os dados de um cliente
    - /clientes/<id>/delete (DELETE) - Deleta o registro de um cliente
'''

@cliente_route.route('/')
def form_list_cliente():
    #Faz o requerimento para renderizar na tela a lista de todos os clientes
    clientes = Cliente.select()
    return render_template('form_list_cliente.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    #Envia os dados de um novo cliente para o servidor
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )
    
    return render_template('item_cliente.html', cliente=novo_usuario) 

@cliente_route.route('/new')
def form_add_cliente():
    #Faz o requerimento do formulário de adicionar novo cliente
    return render_template('form_add_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def form_info_cliente(cliente_id):
    #Faz o requerimento das informações de um cliente
    
    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_info_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    #Faz o requerimento de um formulário para atualizar os dados de um cliente
    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_add_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    #Envia os dados atualizados do cliente para o servidor
    data = request.json
    
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
    
    return render_template("item_cliente.html", cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    #Deleta os dados de um cliente

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()

    return {'status': 'OK'}