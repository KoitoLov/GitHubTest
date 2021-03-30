import random

caras = 0
cruces = 0
for i in range(100):

    tirar_moneda = random.choice(["Cara", "Cruz"])
    if tirar_moneda == "Cara":
        caras += 1
    elif tirar_moneda == "Cruz":
        cruces +=1

print("Han salido", caras, "caras. Y", cruces, "cruces.")