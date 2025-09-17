# Projeto de Automação PowerUp - Hashtag Treinamentos - Jornada Python (Set/25)

Projeto básico de automação para login em site e preenchimento de formulário com os dados presentes em uma base de dados.

## Bibliotecas utilizadas:
* **Pyautogui**: para controle de teclado e mouse;
* **Pandas**: para leitura e manuseio da base de dados;
* **Time**: para inserir delay entre comandos para que o site tenha tempo habil de carregar.

## Comandos Utilizados:

* **Pyautogui.press:** para pressionar uma tecla;
* **Pyautogui.click:** para clicar na tela (_aqui foi necessário primeiramente identificar a posição da tela para o click correto_);
* **Pyautogui.write:** para escrita (_write aceita apenas texto, portanto até um numero deve estar entre parenteses ou utilizar o comando str()_);
* **Pyautogui.scroll:** para rolar a tela (_para **CIMA** o valor deve ser **positivo** e para **BAIXO** o valor deve ser **negativo**_)
* **Pyautogui.PAUSE:** para inserir um delay entre todos os comandos

* **Time.sleep:** para inserir um delay após um comando (_esse diferente do pyautogui.PAUSE irá atuar apenas onde inserido_)

* **Pandas.read_csv:** para ler a tabela (_para que possamos utilizar a tabela o mesmo deve ser inserida dentro de uma váriavel, caso contrario sistema apenas irá ler a tabela e descarta-la_)

* **For:** utilizado para acessar cada linha da tabela.

* **.loc:** para usar o valor presente na linha da tabela (_usado com a variavel "Tabela" ex.: tabela.loc["numero da linha", "nome da coluna"_])

* **str:** para converter um valor em texto

_Para um melhor manuseio incluso os valores utilizados dentro de variaveis_