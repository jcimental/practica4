# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:17:58 2022

@author: estudiantes
"""
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import numpy as np
#import random as rd

c=3*10**8
h=6.63*10**-34
k=1.38*10**-23

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name,
        a=minval, b=maxval),cmap(np.linspace(minval, maxval, n)))
    return new_cmap

class grafica:
    
    def __init__(self):
        
        self.fig, self.ax = plt.subplots()
        
    
    def mapaEstelar(self, ar, dec, indice="", colores=[], teff=[], guardar=False):
        self.reiniciarFigura()
        
        self.ax.scatter(ar, dec, s=2, color="blue")
        
        self.ax.set_facecolor((0,0,0))
        
        if indice:
            
            for i in indice:
                if teff and colores:
                    self.ax.scatter(ar[i], dec[i], s=2, color=colores[round(teff[i]*0.01)*100])
                    continue
                self.ax.scatter(ar[i], dec[i], s=2, color='r')
            
        #self.ax.set_xlim(45,50)
        #self.ax.set_ylim(2,6)
            
        #self.ax.scatter(229.6375, 2.0811, s=20, color=(1,1,1))
        
        self.ax.set_xlabel("Ascensión recta ($^o$)")
        self.ax.set_ylabel("Declinación ($^o$)")
        
        if guardar:
            self.fig.savefig("mapaEstelar.jpg")
            
        plt.show()

        
    def radiacionCuerpoN(self, teff, guardar=False):
        import numpy as np
        self.reiniciarFigura()
        
        def f(x):
            return (2*(c/x)**3)/(c**2)*h*1/(np.exp((h*(c/x))/(k*teff))-1)   
        
        x=np.linspace(0, 0.0001, 1000)
        
        self.ax.plot(x, f(x))
        
        if guardar:
            self.fig.savefig("radiacionCuerpoNegro.jpg")
            
        plt.show()
        
        
    def diagramaHR(self, bp_rp, phot_g_mean_mag, guardar=True, tempt=False, zoom=False):
        self.reiniciarFigura()
        
        vmin=35000
        vmax=2000
        
        if tempt:
        
            mapeo=self.ax.scatter(bp_rp, phot_g_mean_mag, c=bp_rp, s=2, cmap="RdYlBu", vmin=vmin, vmax=vmax)
            #mapeo=self.ax.scatter(bp_rp, phot_g_mean_mag, c=bp_rp, s=2, cmap="RdYlBu", vmin=11000, vmax=2000)
            
        else:
            mapeo=self.ax.scatter(bp_rp, phot_g_mean_mag, c=bp_rp, s=2, cmap="RdYlBu_r", vmin=-1, vmax=5)
            
        
        self.ax.set_facecolor((0,0,0))
        
        if tempt and zoom:
            temp_max=max(bp_rp)+5
            temp_min=min(bp_rp)-5
            
            cax = self.fig.add_axes([self.ax.get_position().x0,self.ax.get_position().y0-0.1
                                     ,self.ax.get_position().width,0.01])
            
            colb=self.fig.colorbar(mapeo, cax=cax, orientation="horizontal")
            colb.ax.invert_xaxis()
            
            cax2 = self.fig.add_axes([self.ax.get_position().x0,self.ax.get_position().y0
                                     ,self.ax.get_position().width,0.01])
            
            fracmin=(temp_min-vmin)/(vmax-vmin)
            fracmax=(temp_max-vmin)/(vmax-vmin)
            mapeo2=truncate_colormap(plt.get_cmap('jet'), minval=fracmin, maxval=fracmax)
            norm=colors.Normalize(vmin=temp_min, vmax=temp_max)
                
            colb2=colorbar.ColorbarBase(cax2, cmap=mapeo2, norm=norm , orientation="horizontal")
            
            colb2.ax.invert_xaxis()
            
            self.ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
        
            self.ax.set_xlim(temp_min,temp_max)
        
            self.ax.invert_xaxis()
            
        elif tempt and not zoom:
            cax = self.fig.add_axes([self.ax.get_position().x0,self.ax.get_position().y0
                                     ,self.ax.get_position().width,0.01])
                
            colb=self.fig.colorbar(mapeo, cax=cax, orientation="horizontal")
            
            colb.ax.invert_xaxis()
            
            self.ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
            self.ax.set_xlim(2000,5000)
        
            self.ax.invert_xaxis()
            
        else:
            self.ax.set_xlim(-1,5)
        
        #colb.ax.invert_xaxis()
        
        ylim_S = max(phot_g_mean_mag) + 5
        ylim_i = min(phot_g_mean_mag) - 5
        self.ax.set_ylim(ylim_i, ylim_S)
        self.ax.set_ylim(-10,20)
        
        self.ax.invert_yaxis()
        
        if guardar:
            self.fig.savefig("diagramaHR.jpg")
            
        plt.show()
        
    def limpiarFigura(self):
        self.ax.cla()
        self.fig.clf()
        
    def reiniciarFigura(self):
        if self.fig.get_axes() and (self.ax.collections or self.ax.lines):
            self.fig, self.ax = plt.subplots()
            #plt.close()
        
if __name__=="__main__":
    grafica().radiacionCuerpoN(3000)
    cmap=plt.get_cmap("jet")
    #print(plt.get_cmap("jet"))
    #print(colors.LinearSegmentedColormap.from_list('trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=0.01, b=0.02),cmap(np.linspace(0.01, 0.02, 100))))