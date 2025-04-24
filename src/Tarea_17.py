def anagramas():
    p1 = input("Ingresa la primera palabra: ").lower()
    p2 = input("Ingresa la segunda palabra: ").lower()
    if sorted(p1) == sorted(p2):
        print("Son anagramas.")
    else:
        print("No son anagramas.")
print(anagramas())