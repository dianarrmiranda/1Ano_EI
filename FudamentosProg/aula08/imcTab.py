people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

print("People:", people)

def imc(w,h):
    return w/(h**2)

ValImc = [imc(w,h) for n,h,w in people] 

print(ValImc)

altura = [(n,w,h) for n,h,w in people if w>1.7]
print(altura)

idade = [n for n,w,h in people if 18< imc(w,h) < 25]

print( 'imc', idade)

