from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j]<=S:
                    im_bin.pixels[i][j]=0
                else:
                    im_bin.pixels[i][j]=255
        return im_bin

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        lmax,lmin=0,self.H
        cmax,cmin=0,self.W
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j]==0:
                    if i<lmin:
                        lmin=i
                    if i>lmax:
                        lmax=i
                    if j<cmin:
                        cmin=j
                    if j>cmax:
                        cmax=j
        im_bin.pixels=self.pixels[lmin:lmax,cmin:cmax]
        return im_bin                 
                
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))
        im_bin.pixels=resize(self.pixels, (new_H,new_W), 0)
        im_bin.pixels=np.uint8(im_bin.pixels*255)
        im_bin.H=new_H
        im_bin.W=new_W
        return im_bin


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        pixels_ok=0
        for k in range(self.H):
            for i in range(self.W):
                if self.pixels[k][i]==im.pixels[k][i]:
                    pixels_ok+=1
        return pixels_ok/(self.H*self.W)
