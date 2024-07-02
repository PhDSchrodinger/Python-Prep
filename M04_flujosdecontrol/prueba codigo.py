tope_rango = 10
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):  #recordar que el rango va de (i hasta j-1 donde es (i,j))
        print("este es n",n, "entre div",div)
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
        a = input("quieres el siguiente primo 1 para si 2 para no: ")
        if a != '1':
            print("se finalizara el proceso")
            break
        
    else:
        primo = True
    n += 1
    
