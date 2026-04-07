def fondos():
    saldo=0
    meta=1000
    while saldo < meta:
        deposito= int(input("ingrese deposito actual"))
        saldp += deposito
    return saldo

def main():
    resultado= fondos()
    print("meta superada= ", resultado)

if __name__=="__main__":
    main()