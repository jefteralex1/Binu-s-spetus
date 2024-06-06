from flask import Flask # Importando o Flask, framework que será usada para criar a aplicação web.

from routes.home import home_route #Importa a variável 'home_route' do módulo 'home' dentro do pacote 'routes'. Um blueprint que define as rotas relacionadas à página inicial.

from routes.cliente import cliente_route #Importa a variável 'cliente_route' do módulo 'cliente' dentro do pacote 'routes'. 'cliente_route' é um blueprint que define as rotas relacionadas aos clientes.

app = Flask(__name__) #Cria uma instância da classe Flask e a armazena na variável 'app'. '__name__' é um parâmetro que indica o nome do módulo atual. Esta instância é a aplicação WSGI.

app.register_blueprint(home_route) #Registra o blueprint 'home_route' na aplicação Flask. Isso adiciona todas as rotas definidas em 'home_route' à aplicação.

app.register_blueprint(cliente_route, url_prefix='/clientes') #Registra o blueprint 'cliente_route' na aplicação Flask, com um prefixo de URL '/clientes'. Todas as rotas definidas em 'cliente_route' serão acessíveis sob este prefixo.

app.run(debug=True) #Inicia o servidor de desenvolvimento do Flask com o modo de debug ativado. O modo de debug permite a recarga automática do servidor quando há mudanças no código e fornece uma interface de debug em caso de erros.
