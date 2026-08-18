a = float(input("Digite o tamanho do primeiro lado: "))
b = float(input("Digite o tamanho do segundo lado: "))
c = float(input("Digite o tamanho do terceiro lado: "))

# Verificação do princípio da existência de um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os comprimentos informados podem formar um triângulo!")
    
    if a == b == c:
        print("Tipo: Triângulo Equilátero (3 lados iguais)")
    elif a == b or a == c or b == c:
        print("Tipo: Triângulo Isósceles (2 lados iguais)")
    else:
        print("Tipo: Triângulo Escaleno (3 lados diferentes)")
else:
    print("Os comprimentos informados NÃO podem formar um triângulo.")