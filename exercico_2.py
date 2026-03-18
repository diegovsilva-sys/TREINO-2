import os

#LIMPAR TERMNNAL
os.system("cls")

login_correto = "Diego"
senha_correta = "12345"

for i in range(3):
       login = input("Digite seu login: ")
       senha = input("Digite sua senha: ")

       login_esta_correto = login == login_correto
       senha_esta_correta = senha == senha_correta

       if login_esta_correto and senha_esta_correta: 
              print("Bem-vindo ao sistema!")
              break
             
       else: 
            print("Login ou senha invalidos...")
            print("Tente novamente... \n")