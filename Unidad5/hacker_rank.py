print("Ejercicio 1")
n=input("Escribe un numero nnmssss")
num=int(n)
if num % 2==0 and 2<= num  <= 5:
    print("Not Weird")
elif num % 2==0 and 6<= num  <=20:
    print("Weird")
elif num % 2==0 and num>20: #aca
    print("Not Weird")
else: 
    
    print("Weird")

print("Ejercicio 2")
num1=input("Primer digito")
a=int(num1)
num2=input("Segundo digito")
b=int(num2)
print(a+b)
print(a-b)
print(a*b)

print("ejercicio 3")
c = int(input())
d = int(input())

# 1. División entera
print(c // d)

# 2. División flotante
print(c / d)
