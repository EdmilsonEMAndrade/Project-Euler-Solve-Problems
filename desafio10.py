def isPrimo(maiorNumero):

    listaPrimo = [2,3,5,7]
    primo = True
    for i in range(9, maiorNumero,+2):
        for c in range (len(listaPrimo)):
            if i%listaPrimo[c] == 0:
                primo = False
                break
            if i/2+1<listaPrimo[c]:
                break
        if primo == True:
            listaPrimo.append(i)
        primo = True
    return (listaPrimo)

def somaLista(listaNum):
    resultado = 0
    for i in range(len(listaNum)):
        resultado += listaNum[i]
    return resultado

lista = isPrimo(2000000)
print(lista)
print(somaLista((lista)))