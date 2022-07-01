# Como utilizar
###  Requisitos:
- Instalação do Python, instale pelo [site oficial](https://www.python.org/downloads/) ou pela [windows store](https://www.microsoft.com/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab) durante a instalação do python, não se esqueça de marcar a opção add Python to Path.

###  Configurando Telegram
- Em seu telegram, iniciei uma conversa com @BotFather
- Clique em Start, e quando abrir as opções, clique em "/newbot"
- Em seguida informe um nome e depois um username para o bot, lembrando que username tem que terminar com "_bot" no final, exemplo "meu_bot"
- Finalizando você vai ver uma mensagem contendo os dados do bot que vc criou, copie o Token e insira no arquivo de configuração, config.yaml
- O 2º parametro a ser configurado é o chat_id, para isso, siga os passos abaixo:
- Criei um grupo no telegram, e adicione o bot que você acabou de criar, informando o username para encontra-lo.
- Com o grupo criado, acesse o link a seguir, alterando o TOKEN na url, pelo o que você acabou de criar: https://api.telegram.org/botSEUTOKEN/getUpdates
- Vai ser exibido na tela um JSON, procure por "chat":"id", geralmente esse valor começa com o sinal de menos(-) e altere no arquivo config.yaml chat_id.

- Arquivo de configuração, para que você mesmo determine como o bot deve funcionar (./config.yaml).

###  Rodando o bot:
- Abra um terminal, se for windows (aperte a tecla do windows + r e digite "cmd").
- Navegue até a pasta onde o bot foi extraído, exemplo: cd "C:\Relatorio Pdv".
- Instale as dependências do bot executando o comando, sem aspas: "pip install -r requirements.txt".
- Vá à pasta correspondente ao pdv que quer executar a tarefa, exemplo: cd "C:\Relatorio Pdv\pdv 1", e execute o comando, sem aspas: "python main.py"

### Setar no terminal IDLE python:
- Pesquisar IDLE no iniciar:

- Execute os seguintes comandos, sem aspas, no campo 'escreva aqui a senha', digite a senha de supervisor no sistema:

"import keyring"

"keyring.set_password('dbvenda','S','escreva aqui a senha')"




