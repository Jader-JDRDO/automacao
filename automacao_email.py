# Precisa Instalar
# pyautogui -> automacoes
# Pandas ->
import pyautogui #automaçao de tarefas
import pandas #leitura e interpretação de tabelas
import time #tempo de descanso entre processamento do codigo


link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
# Passo a passo do desafio

#da um tempo de 2 segundos para executar cada linha de codigo
pyautogui.PAUSE = 2
#tempo de descanso serve para caso o seu computador nao seja tao rapido, não de ruim ou a automacao saia errada

# Passo 1: Entrar no sistema da empresa (link no drive)
# Abrir o navegador
pyautogui.press("win") #clica no botao windows do seu computador
pyautogui.write("Firefox") #digita o navegador que voce usa majoritariamente
pyautogui.press("enter") #clica no botao enter do seu computadador

time.sleep(5) #tempo de espera de 2 segundos para executar o proximo codigo

pyautogui.write(link) #escreveu o link que você deixou a cima na barra de pesquisa do navegador(URL)
# Digitei o link do sistema
pyautogui.press('enter') #aperta o botao enter para entrar
time.sleep(3) #tempo de espera de 3 egundos
# Apertei enter e esperei

# Passo 2: Navegar no sistema para encontrar a base de dados
pyautogui.click(x=427, y=468,clicks = 2) #posiçao do botao padrao na minha tela e dois clicks
time.sleep(2) #descanso de 2 segundos


# Passo 3: Exportar a base de dados (baixar o arquivo)
pyautogui.click(x=1336, y=451) #posiçao do botao que quero utilizar
time.sleep(2) #espera de 2 segundos
#pyautogui.clic(x=1336,y=451, button='right') outro tipo de modo para concluir a tarefa
pyautogui.click(x=1052, y=555) # posicao onde quero clicar
time.sleep(5) # tempo de espera de 5 segundos para carregar apropriadamente


# Passo 4: Calcular os indicadores (Faturamento e quantidade de produtos vendidos)
caminho = r"Exportar\Vendas - Dez.xlsx" #local do arquivo que foi baixado e o nome dele
tabela = pandas.read_excel(caminho) #pandas leu o arquivo e o interpretou

print(tabela) # exibiçao da tabela que o pandas interpretou

faturamento = tabela['Valor Final'].sum() #soma da coluna faturamento que eu necessito para fazer o relatorio 
quantidadeprod = tabela['Quantidade'].sum() #soma da coluna quantidade que eu necessito para fazer o relatorio

print(f'O faturamento total foi de {faturamento} e a quantidade de produtos vendida foi de {quantidadeprod}')
#exibiçao das contas para eu ter ciencia se esta tudo certo

# Passo 5: Enviar as informaçoes por e-mail
import pyautogui
import time
import pyperclip # funçao para copiar e colar textos
email='jader.raoliveira@gmail.com' #email que quero mandar o relatorio


time.sleep(5) # espera de 5 segundos por garantia
pyautogui.hotkey('ctrl','t') #abrindo nova aba no navegador
pyautogui.write('https://mail.google.com/mail/u/0/#inbox') #escrevendo o link do email que quero entrar 
pyautogui.press('enter') #pressionando enter no meu computador  
time.sleep(5) #tempo de espera de 5 segundos por garantia de carregamento

pyautogui.click(x=107, y=206) #posicao do botao escrever que aparece no meu computador
time.sleep(2) #tempo de espera de 2 segundos

pyautogui.write(email) #colando o email que eu deixei preescrito
time.sleep(2) #tempo de espera de 2 segundos
pyautogui.press('tab') #pressionando a tecla tab no meu computador para sair das opçoes depois de escrever o email

pyautogui.press('tab')#pressionando a tecla tab novamente para ir para a proxima 'linha' que quero utilizar
time.sleep(2) #tempo de descanso de 2 segundos


pyperclip.copy('Relatório de Vendas')#copiando o texto que tem caracteres especiais que nao sao aceitos pelo pyautogui
pyautogui.hotkey('ctrl','v')#colando o texto com caracteres especiais
pyautogui.press('tab') #indo para a proxima 'linha' que quero utilizar
time.sleep(2) #tempo de espera de 2 segundos
texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidadeprod:,}

Qualquer dúvida estou à disposição.
Att.,
Jader Oliveira
"""
#texto preescrito para relatorio de dados
#formataçao do texto ',' virgula serve para 
#o . é o separador de casa decimal geralmente acompanhada com um numero que tu quer que tenha de casas decimais
#o f siginifca float que no caso sao numeros decimais
pyperclip.copy(texto) #copiando o texto de relatorio de dados
pyautogui.hotkey('ctrl','v')#colando o texto de relatorio de dados no lugar que desejo
time.sleep(2) # tempo de espera de 2 segundos
pyautogui.click(x=846, y=832) #clicando no botao enviar que esta localizado nessa posicao da minha tela

time.sleep(5)
print(pyautogui.position()) #me mostrando a posiçao do mouse na minha tela apos 5 segundos 

