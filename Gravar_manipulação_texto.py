arquivo = open('testeArquvo.txt','w')

arquivo.write('teste em python ')
arquivo.write('conclusão')
arquivo.close()

#leitura do arquivo

leitura = open('testeArquvo.txt','r')
print(leitura.read())
leitura.close()
