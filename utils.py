from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Erica', idade=32)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    # pessoas = Pessoas.query.filter_by(nome='Flavio')
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoas = Pessoas.query.filter_by(nome='Erica').first()
    print(pessoas.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Erica').first()
    pessoa.idade = 23
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.delete()

def insere_usuario(login,senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('flavio','1234')
    insere_usuario('erica','4321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()
