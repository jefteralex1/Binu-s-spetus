from flask import Blueprint, render_template #Importando Blueprint e render_template. Blueprint é usado para estruturar a aplicação em componentes modulares. render_template é utilizado para renderizar templates HTML.

home_route = Blueprint('home', __name__) #Cria uma instância de Blueprint chamada 'home_route'. O primeiro argumento é o nome do blueprint ('home') e o segundo é o nome do módulo atual (__name__). Esta instância será usada para definir as rotas relacionadas ao componente "home".

@home_route.route('/') #Define uma rota para a URL raiz ('/') usando o blueprint 'home_route'. Quando um usuário acessar esta URL, a função 'home' será chamada.
def home():
    return render_template('landing.html') #Define a função 'home' que é chamada quando a rota '/' é acessada. Esta função renderiza e retorna o template 'index.html'.

@home_route.route('/bino')
def site_principal():
    return render_template('bino.html')

@home_route.route('/binoadmin')
def adm():
    return render_template('index.html')


@home_route.route('/churrascometro')
def churrascometro():
    return render_template('churrascometro.html')
    
@home_route.route ('/cardápio')
def cardapio():
    return render_template('cardápio.html')

@home_route.route ('/kits')
def kits():
    return render_template('kits.html')

@home_route.route('/landing')
def lading():
    return render_template('landing.html')