from flask import Blueprint, render_template, request #Importa Blueprint para modularizar a aplicação, render_template para renderizar templates HTML, e request para acessar dados da requisição HTTP.

from database.cliente import CLIENTES #Importa a variável CLIENTES do módulo cliente no pacote database. CLIENTES é uma lista que armazena dados de clientes.

cliente_route = Blueprint('cliente', __name__) #Cria uma instância de Blueprint chamada 'cliente_route'. O primeiro argumento é o nome do blueprint ('cliente') e o segundo é o nome do módulo atual (__name__). Este blueprint será usado para definir as rotas relacionadas aos clientes.


@cliente_route.route('/')
def lista_clientes():
    '''Listar os Clientes'''
    return render_template('lista_clientes.html', clientes=CLIENTES) #Define uma rota para a URL raiz ('/') no contexto do blueprint 'cliente_route'. A função lista_clientes() renderiza o template 'lista_clientes.html', passando a lista CLIENTES para o template.

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    ''' Inserir os dados do cliente '''
    data = request.json
    #Recebe os dados do cliente em formato JSON da requisição POST.

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    } #Cria um novo dicionário representando o cliente com os dados recebidos e um ID único.

    CLIENTES.append(novo_usuario) #Adiciona o novo cliente à lista CLIENTES.

    return render_template('item_cliente.html', cliente=novo_usuario) #Renderiza o template 'item_cliente.html', passando o novo cliente para o template.

@cliente_route.route('/new')
def form_cliente():
    '''Form para cadastrar um cliente'''
    return render_template('form_cliente.html') #Define uma rota para a URL '/new'. A função form_cliente() renderiza o template 'form_cliente.html', que contém um formulário para cadastrar um novo cliente.

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id): #Define uma rota para URLs no formato '/<cliente_id>', onde <cliente_id> é um número inteiro. A função detalhe_cliente() renderiza um html com um modal que será chamado quando essa rota for acessada.

    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0] #Filtra a lista CLIENTES para encontrar o cliente com o ID fornecido usando uma função lambda, e armazena-o na variável cliente. Uma função lambda é uma pequena função anônima definida no local.

    return render_template('detalhe_cliente.html', cliente=cliente) #Renderiza o template 'detalhe_cliente.html', passando o cliente encontrado para o template.

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id): #Define uma rota para URLs no formato '/<cliente_id>/edit'. A função form_edit_cliente() será chamada quando essa rota for acessada.

    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c #Percorre a lista CLIENTES para encontrar o cliente com o ID fornecido e armazena-o na variável cliente.

    return render_template('form_cliente.html', cliente=cliente) #Renderiza o template 'form_cliente.html', passando o cliente encontrado para o template. Presumivelmente, este formulário será usado para editar os dados do cliente.

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id): #Define uma rota para URLs no formato '/<cliente_id>/update', aceitando apenas requisições HTTP PUT. A função atualizar_cliente() será chamada quando essa rota for acessada.

    cliente_editado = None
    data = request.json #Recebe os dados do cliente em formato JSON da requisição PUT.

    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']
            cliente_editado = c
    # Percorre a lista CLIENTES para encontrar o cliente com o ID fornecido e atualiza os dados desse cliente com os dados recebidos.

    return render_template('item_cliente.html', cliente=cliente_editado) #Renderiza o template 'item_cliente.html', passando o cliente atualizado para o template.

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id): #Define uma rota para URLs no formato '/<cliente_id>/delete', aceitando apenas requisições HTTP DELETE. A função deletar_cliente() será chamada quando essa rota for acessada.

    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id] #Remove o cliente com o ID fornecido da lista CLIENTES.
