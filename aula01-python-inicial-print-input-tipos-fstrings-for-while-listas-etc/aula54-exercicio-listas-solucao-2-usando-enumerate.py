
'''CRIA UMA LISTA PARA SER UTILIZADA NO PROGRAMA'''
lista = []

while True:  # CRIA O LOOP DO PROGRAMA
   
   opcao = input('Selecione uma opção:[i]nserir [a]pagar [l]istar:') # ABSORVE O COMANDO DO USUÁRIO
   if (opcao != 'i') and (opcao != 'a') and (opcao != 'l'):  # TESTA OPÇÕES SELECIONADAS
      print('Opção inválida, escolha i, a ou l')
   elif opcao == 'i':  # SE OPÇÃO INSERIR ADICIONA O VALOR DIGITADO NA VARIAVEL OPCAOI NA LISTA
        opcaoI = input("Insira o item desejado na lista: ")
        lista.append(opcaoI)  
        
   elif opcao == 'a' and lista == []: # SE OPÇÃO SELECIONADA APAGAR E A LISTA ESTÁ VAZIA, INFORMA QUE NÃO É POSSIVEL
       print('Não há itens na lista para serem removidos')
   elif opcao == 'a' and lista != []:  # SE A OPÇÃO É APAGAR E TEM CONTEÚDO NA LISTA, APAGA O ÚLTIMO ITEM
       lista.pop()
   elif opcao == 'l': # SE OPÇÃO SELECIONA FOR LISTAR E NÃO TEM CONTEÚDO, INFORMA QUE NÃO TEM CONTEÚDO PARA LISTAR
       if lista == []:
           print('Não há nada para mostrar')
       else:  # SE OPÇÃO SELECIONA FOR LISTAR E TEM CONTEÚDO, CRIA UM RANGE DE INDICES COM O TAMANHO DA LISTA
           
           for indice, nome in enumerate(lista): # PRINTA CADA INDICE E CADA CONTEÚDO DO INDICE ESPECIFICO A PARTIR DO RANGE GERADO
               print(indice, lista[indice])
              
    
      