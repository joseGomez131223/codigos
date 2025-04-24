def num_primo():
    while True:
        num=input("dame el numero que deseas verificar si es primo o no es primo:")
        if num.isnumeric()==True and int(num)>0:
            n=int(num)
            if n > 1:
                for i in range(2, n):
                    if n % i == 0:
                        print(f"{n} no es primo.")
                        break
                else:
                    print(f"{n} es primo.")
                    break
            else:
                print(f"{n} no es primo.")
print(num_primo())