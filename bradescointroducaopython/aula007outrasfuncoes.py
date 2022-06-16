#Função open() é utilizada para abertura dos arquivos.
arquivo = open('arquivo.txt', 'w')

#Função write() é utilizada para gravar informações em um aruivo existente.
arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')

#Função close() é muito importante para encerrar o arquivo após a sua utilização.
arquivo.close()

#Função read() realiza a leitura de todo o conteudo do arquivo.
leitura = open('arquivo.txt', 'r') # r significa que o arquivo está sendo aberto em modo leitura.
print (leitura.read())
leitura.close




