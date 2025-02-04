import csv
import tkinter
from tkinter import filedialog

def ventanaArchivo():
    root=tkinter.Tk()
    root.withdraw()
    ruta=filedialog.askopenfilename() 
    root.update()
	
    return ruta

def isfloat(cadena):
	try:
		float(cadena)
		return True
	except:
		return False

class Archivo:
    
    def __init__(self):
        self.ruta=""
        
    def extraerRuta(self):
        ruta=self.archivo.split("/")
        ruta="/".join(ruta[:-1])+"/"
        self.ruta=ruta
        
        return ruta
         
    def leerArchivo(self, archivo=""):
        
        if not archivo:
            self.archivo=ventanaArchivo()
            archivo=self.archivo
            
        else:    
            self.archivo=archivo
        llaves=[]
        tabla={}
    
        with open(archivo, "r") as tablas:
    		
            lector_excel=csv.reader(tablas)
    
            llaves=next(lector_excel)
    
            for llave in llaves:
                tabla[llave]=[]
    
    
            for fila in lector_excel:
                cont=0
                for columna in fila:
    
                    if isfloat(columna):
    
                        columna=float(columna)
    				
                    tabla[llaves[cont]].append(columna) 
    
                    cont+=1
                    
            #print(self.archivo)
                    
            return tabla
        
    def crearArchivo(self,nombre_archivo,diccionario,noEstrella):
      with open(self.ruta + nombre_archivo, "w") as archivo:
          temp=diccionario["teff_val"][noEstrella]
          ar=diccionario["ra"][noEstrella]
          dec=diccionario["dec"][noEstrella]
          archivo.write("Esta estrella tiene una temperatura efectiva de "+str(temp)+" sus coordenadas (ascensión recta,declinacion) son ("+str(ar)+","+str(dec)+ ")")
          archivo.write("-------------------------------------\n")
        
    def leerArchivos(self, archivo1="",  *args):
        tabla1=self.leerArchivo(archivo1)
        #tabla2=self.leerArchivo(archivo2)
        
        tablas=[]
        if args:
            if len(args[0])>1 and isinstance(args[0],list):
                for archivo in args[0]:
                    tablas.append(self.leerArchivo(archivo))
            
            elif isinstance(args[0], str):
                for archivo in args:
                    tablas.append(self.leerArchivo(archivo))
        
        #for llave in tabla1.keys():
        #    if llave in tabla2.keys():
        #        tabla1[llave]=tabla1[llave]+tabla2[llave]
                
        #    else:
        #        tabla2[llave]=tabla1[llave]
                
        for llave in tabla1.keys():
            for tabla in tablas:
                if llave in tabla.keys():
                    tabla1[llave]=tabla1[llave]+tabla[llave]
                
        return tabla1
        
    def obtenerColoresCuerpoN(self,ruta=""):
        
        if not ruta:
            ruta=ventanaArchivo()
            
        colores={}
        with open(ruta, "r") as archivo:
            for line in archivo:
                line=line.strip()
                col=line.split("  ")
                #print(col[1])
                if col[1]=="10deg":
                    col[0]=float(col[0].split(" ")[0])
                    colores[col[0]]=col[-1]
                    
        #print(colores)
                
        return colores
        
if __name__=="__main__":
    
    archivo=Archivo()
    datos=archivo.leerArchivo()
    print(datos)
    #estrellas=datos.leerArchivo()
    #print(datos.extraerRuta())
    ventanaArchivo()