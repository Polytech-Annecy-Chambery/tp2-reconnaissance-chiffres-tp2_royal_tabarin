from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    l,valeur,maxi=[],0,0
    ima_bin=image.binarisation(S)
    ima_bin_localise=ima_bin.localisation()
    for i in range(len(liste_modeles)):  
        ima_resized=ima_bin_localise.resize(liste_modeles[i].H,liste_modeles[i].W)
        l.append(ima_resized.similitude(liste_modeles[i]))
        if l[i]>=maxi:
            maxi=l[i]
            valeur=i
    return valeur









