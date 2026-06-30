# 🚀 Automação de Relatório de Vendas e Estoque

Este projeto é uma automação ponta a ponta que realiza o download de uma base de dados de vendas no Google Drive, processa os dados para calcular indicadores logísticos e envia um relatório formatado automaticamente por e-mail.

O projeto demonstra a aplicação prática de conceitos de RPA (Robotic Process Automation) combinados com Análise de Dados para trabalhos manuais que podem ser automatizados de maneira eficiente


🛠️ Tecnologias Utilizadas

*   Python 3
*   PyAutoGUI: Automação de cliques, digitação e controle de interface do usuário.
*   Pandas: Leitura, tratamento e manipulação dos dados da planilha Excel (`.xlsx`).
*   Pyperclip: Manipulação da área de transferência para garantir a colagem correta de textos com caracteres especiais.
*   Time: Gerenciamento dos tempos de espera (`sleep`) para garantir a estabilidade da automação.


 ⚙️ O que a automação faz? (Passo a Passo)

1. Acesso ao Sistema: Abre o navegador Firefox automaticamente e navega até a pasta compartilhada do Google Drive.
2. Download dos Dados: Executa cliques precisos na tela para baixar a base de dados de vendas mais recente (`Vendas - Dez.xlsx`).
3. Análise de Dados com Pandas: O script lê o arquivo Excel e processa os dados para calcular dois indicadores fundamentais:
    * Faturamento Total (Soma da coluna `Valor Final`).
    * Quantidade de Produtos Vendidos (Soma da coluna `Quantidade`).
4. Envio de E-mail: Abre uma nova aba no Gmail, inicia a composição de uma nova mensagem, preenche o destinatário, assunto e cola o corpo do e-mail perfeitamente formatado com os indicadores calculados.


🚀 Como Executar o Projeto

Pré-requisitos:

  Certifique-se de ter o Python instalado e as seguintes bibliotecas adicionais:
        pip install pyautogui pandas pyperclip openpyxl
