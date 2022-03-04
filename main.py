ejemplo = "b=7"
ejemplo1 = "a = 32.4 *(-8.6 - b)/       6.1"
ejemplo2 = "d = a ^ b // Esto es un comentario"
caracteres = ["=", "+","-", "*", "/", "^", "(", ")"]
tokens_definicion = {"=":"Asignacion",
                    "+":"Suma",
                    "-":"Resta",
                    "*":"Multiplicacion",
                    "/":"Division",
                    "^":"Potencia",
                    "(":"Parentesis que abre",
                    ")":"Parentesis que cierra",
                    "//":"Comentario",
                    ".":"Real",
                    "n":"Entero",
                    "v":"Variable",
                    "no valido":"no valido"}


def leer_string(string_input):
  listaConstructora = []
  listaElementos = []
  string_input2 = string_input
  string_input = string_input.replace(" ", "")
  string_input = string_input.replace("\n","")
  for i in range(len(string_input)):
    if (string_input[i].isdigit() or string_input[i] == "."):
      listaConstructora.append(string_input[i])
    elif (string_input[i] == "/" and string_input[i + 1] == "/"):
      if(listaConstructora):
        listaElementos.append("".join(map(str, listaConstructora)))
      listaConstructora.clear()
      listaElementos.append(string_input2[string_input2.find('//'):])
      return(listaElementos)
    elif (not (string_input[i].isdigit()) and (string_input[i] in caracteres) or string_input[i].isalpha()):
      if (listaConstructora):
          listaElementos.append("".join(map(str, listaConstructora)))
      listaElementos.append(string_input[i])
      listaConstructora.clear()
    else:
      if (listaConstructora):
          listaElementos.append("".join(map(str, listaConstructora)))
      listaElementos.append(f"{string_input[i]} token no valido")

  listaElementos.append("".join(map(str, listaConstructora)))

  return(listaElementos)


def lexer_aritmetico(archivoTexto):
  lineas = []
  with open(archivoTexto, 'r') as archivo:
    lineas = archivo.readlines()

  for linea in lineas:
    linea.replace('\n',"")
    linea_tokens = leer_string(linea)
    for linea in linea_tokens:
      try:
        print(f"{linea}, {tokens_definicion[linea]}")
      except:
        if("//" in linea):
          token = "//"
        elif(linea.isdigit()):
          token = "n"
        elif("." in linea and "//" not in linea):
          token = "."
        elif(linea[0].isalpha()):
          token = "v"
        else:
          token = "no valido"
        print(f"{linea}, {tokens_definicion[token]}")
      


#print(leer_string(ejemplo2))
lexer_aritmetico('archivo.txt')
