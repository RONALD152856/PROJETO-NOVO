de PyQt5 importação uic, QtWidgets
importação sqlite3


def chama_segunda_tela():
    primeira_tela. label_4. setText("")
    nome_usuario = primeira_tela. lineEdit. Texto()
    senha = primeira_tela. lineEdit_2. Texto()
    se nome_usuario == "joao123" e senha == "123456" :
        primeira_tela. fechar()
        segunda_tela. programa()
    outra coisa:
        primeira_tela. label_4. setText("Dados de login incorretos!")
    

def logout():
    segunda_tela. fechar()
    primeira_tela. programa()

def abre_tela_cadastro():
    tela_cadastro. programa()


def cadastrar():
    nome = tela_cadastro. lineEdit. Texto()
    login = tela_cadastro. lineEdit_2. Texto()
    senha = tela_cadastro. lineEdit_3. Texto()
    c_senha = tela_cadastro. lineEdit_4. Texto()

    se (senha == c_senha):
        tente:
            banco = sqlite3. conectar ('banco_cadastro.db') 
            cursor = banco. cursor()
            cursor. executar("CRIAR TABELA SE NÃO EXISTIR cadastro (texto nome,texto de login,texto senha)")
            cursor. executar("INSERIR EM VALORES de cadastro ('+nome+','+login+',''+senha+"')")

            banco. cometer() 
            banco. fechar()
            tela_cadastro. rótulo. setText("Usuario cadastrado com sucesso")

        exceto sqlite3. Erro como erro:
            imprimir("Erro ao inserir os dados: ",erro)
    outra coisa:
        tela_cadastro. rótulo. setText("As senhas digitadas são diferentes")
    

    


app=QtWidgets. QApplication([])
primeira_tela=uic. loadUi ("primeira_tela.ui")
segunda_tela = uic. loadUi ("segunda_tela.ui")
tela_cadastro = uic. loadUi ("tela_cadastro.ui")
primeira_tela. pushButton. clicado. conectar (chama_segunda_tela)
segunda_tela. pushButton. clicado. conectar (logout)
primeira_tela. lineEdit_2. setEchoMode(QtWidgets. O QLineEdit. Senha)
primeira_tela. pushButton_2. clicado. conectar (abre_tela_cadastro)
tela_cadastro. pushButton. clicado. conectar (cadastrar) 


primeira_tela. programa()
aplicativo. Exec()