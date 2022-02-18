import os.path
import carga

class Index:

    def __init__ (self, opcion):
        self.opcion=opcion
    

   

def main():
    var=carga.Carga_archivo()
        
    menu='''
    
    Menu Principal:
    1.- Mostrar Patron
    2.- Cargar Nuevo Patron
    3.- Mostrar Nuevo Patron
    4.- Mostrar Datos Del Estudiante
    5.- Salir
    
    '''

    while True:
        print(menu)
        op=input("Ingrese una opcion: ")

        if op == '1':               
            input("mostrar imagen")

        elif op == '2':              
            rt=input("Ingrese la ruta del archivo: ")
            ext=os.path.splitext(rt)
            
            if ext[1]==".xml":    
                
                var.archivoCarga(rt)                 
            else:
                print("Archivo incorrecto")
            
                    
        elif op == '3':
            input("mostrar imagen y bitacora")
            

        elif op == '4':
            texto='''
            Maria Luisa Fernanda Calderon Molina
            201602458
            Introduccion a la Programacion y Computacion 2
            Seccion "A"
            4to Semestre'''
            print(texto)

    
        elif op == '5':
            break
        else:
            print("Opcion Invalida")
            #break

    


if __name__ == "__main__":
    main()
