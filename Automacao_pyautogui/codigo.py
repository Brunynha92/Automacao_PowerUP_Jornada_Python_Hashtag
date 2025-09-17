import pyautogui
import time
import pandas


pyautogui.PAUSE = 0.5
# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")



# abrir o navegador (chrome \\ edge)
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link 
pyautogui.write(site)
pyautogui.press("enter")

#  maximizar a tela
# pyautogui.hotkey("win", "up")

#delay ára carregar o site

time.sleep(3)

# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=937, y=454)

# escrever email e senha
email = "teste@gmail.com"
senha = "12345"

pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)
# Passo 3: Importar a base de produtos pra cadastrar
tabela = pandas.read_csv(r"C:\Users\ACER\OneDrive\Cursos\Hashtag\Jornada_Python_set_2025\Automacao_pyautogui\produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto

for linha in tabela.index:
   

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])

     # clicar no campo de código
    pyautogui.click(x=790, y=308)


    # preencher o campo e passar para o proximo
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # preencher o campo e passar para o proximo
    pyautogui.write(marca)
    pyautogui.press("tab")

    # preencher o campo e passar para o proximo
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # preencher o campo e passar para o proximo
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # preencher o campo e passar para o proximo
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # preencher o campo e passar para o proximo
    pyautogui.write(custo)
    pyautogui.press("tab")

    # preencher o campo e passar para o proximo
    if obs != "nan": #apenas preencher se o campo não estiver vazio
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    # cadastra o produto (botao enviar)
    pyautogui.press("enter")
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

    # Passo 5: Repetir o processo de cadastro até o fim