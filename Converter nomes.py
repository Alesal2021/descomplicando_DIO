s = input("digite seu nome:")  # Entrada de dados
#Aqui usei os metodos replace para mudar as vogais em caracteres e o upper para transformar as letras minusculas em maiusculas
print(s.replace('a','@').replace('e','&').replace('i','!')
      .replace('o','#').replace('u','*').upper().format(s))
