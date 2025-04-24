def fibunacci():
    while True:
        limit = input("Ingresa un número límite para la serie de Fibonacci: ")
        if limit.isnumeric()==True and int(limit) >0:
            limite=int(limit)
            print("continua")
            break
        else:
            print("Solo numeros positivos/enteros")
    a,b = 0, 1 
    c=0
    while c < limite:
        print(a, end=" ")  
        a,b = b,a+b
        c+=1
print(fibunacci())