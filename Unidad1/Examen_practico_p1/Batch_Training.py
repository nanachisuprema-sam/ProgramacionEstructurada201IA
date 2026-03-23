#Simulación de Entrenamiento por Lotes (Batch Training):
#Diseñar un algoritmo que simule el proceso de alimentación de datos a una Red Neuronal. 
#El programa debe solicitar al usuario el ingreso del tamaño de "lotes de tensores" 
#(en MegaBytes, MB) que se van cargando a la memoria VRAM. 
#El proceso de carga debe detenerse inmediatamente cuando el consumo total 
#acumulado supere el límite de seguridad de 2,500 MB para evitar un error de "Out of Memory" (OOM).

def Datos():
    Limite = 2500  
    VRAM = 0
    
    while VRAM < Limite:
        lotes = float(input("Ingrese el tamaño del lote (MB): "))
        if VRAM + lotes > Limite:
            print(f"Error, la carga de {lotes} MB superaría el límite de {Limite} MB.")
            break
        
        VRAM += lotes
        print("MegaBytes acumulados: ", VRAM)

def main():
    Datos()
    
if __name__ == "__main__":
    main()


