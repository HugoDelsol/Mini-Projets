# import pandas as pd
# import numpy as np

# class SnowModel:
    
#     def __init__(self, seuil=0, facteur=3.5):
#         self.seuil = seuil
#         self.facteur = facteur
#         self.fonte = None
#         self.test = None

#     def estimer_fonte(self, temp):
#        self.fonte = np.where(temp > self.seuil, self.facteur * (temp - self.seuil), 0)

# model = SnowModel()

# temp = pd.array([-2.5, 2.0, 5.5])

# print(model.fonte)
# model.estimer_fonte(temp)
# print("Result", model.fonte)
# # print(model.test)


# import numpy as np

# class SnowModel:
#     """Modèle de calcul de fonte de neige par degré-jour."""
    
#     def __init__(self, seuil=0.0, facteur=3.5):
#         self.seuil = seuil
#         self.facteur = facteur

#     def estimer_fonte(self, temperatures):
#         """
#         Calcule la fonte selon la formule : facteur * (T - seuil)
#         Retourne un tableau de même dimension que l'entrée.
#         """
#         # Conversion en array numpy pour garantir la vectorisation
#         temp_array = np.array(temperatures)
        
#         # Calcul vectorisé (plus rapide qu'une boucle)
#         resultat = np.where(temp_array > self.seuil, 
#                             self.facteur * (temp_array - self.seuil), 
#                             0.0)
#         return resultat

# # --- Test du module ---
# model = SnowModel()
# donnees_temp = [-2.5, 2.0, 5.5]

# resultats = model.estimer_fonte(donnees_temp)

# print(f"Températures : {donnees_temp}")
# print(f"Fonte estimée : {resultats}")

# import pandas as pd

# def filtered(data, seuil):

#     moyenne_hauteur = None
#     alertes = None

#     df = pd.DataFrame(data)

#     alertes = df.loc[df["hauteur"] > seuil]

#     if not alertes.empty:
#         moyenne_hauteur = alertes['hauteur'].mean()
#     else:
#         moyenne_hauteur = 0

#     return alertes, moyenne_hauteur

# data = {
#     'heure' : [1, 2, 3, 4, 5],
#     'hauteur' : [1.2, 1.5, 2.1, 2.4, 1.8]
# }

# alertes, moyenne_hauteur = filtered(data, 2.0)

# print("--- Stations en Alerte ---")
# print(alertes)

# print(f"Hauteur moyenne durant l'alerte : {moyenne_hauteur} M")
# from abc import ABC, abstractmethod

# class Barage(ABC):  
    
#     def __init__(self, nom, capacite_max, stock_actuel):
#         self.nom = nom
#         self.capacite_max = capacite_max
#         self.stock_actuel = stock_actuel
    
#     @abstractmethod
#     def gerer_flux(self, debit_entrant):

#         debit_sortant = 0

#         if self.stock_actuel < self.capacite_max:
#             debit_sortant = 0
#         elif self.capacite_max == self.stock_actuel:
#             debit_sortant = debit_entrant
            
#         return debit_sortant
    

# class Enfant(Barage):
#     def gerer_flux(self, debit_entrant):
#         return super().gerer_flux(debit_entrant)
    
    
# modele = Enfant('Engin', 100, 100)

# result = modele.gerer_flux(20)

# print(result)


# import pandas as pd
# data = pd.read_csv("releves_stations_spc.csv")

# class GestionnaireAlerte:

#     def __init__(self):  
#         self.seuils = [0, 1.5, 2.5, 4.0, float('inf')]    
#         self.labels = ["VERT", "JAUNE", "ORANGE", "ROUGE"]

#     def evaluer_risque(self, df):
#         df['vigilance'] = pd.cut(df["hauteur"], bins=self.seuils, labels=self.labels)
#         print(df)

# df = pd.DataFrame(data)
# gestionnaireAlerte = GestionnaireAlerte()
# gestionnaireAlerte.evaluer_risque(df)

# import numpy as np
# import pandas as pd

# class StationHydrometrique:

#     def __init__(self, coeff_a, seuil_bruit):

#         self.coeff_a = coeff_a
#         self.seuil_bruit = seuil_bruit

#     def calculerDebitStation(self, releve_brut):

#         # On ignore ce qui n'est pas entier ou flottant
#         np_array = np.array(releve_brut)
#         # On creer un tableau 2d 
#         df = pd.DataFrame(np_array)
#         # Renomme la colonne 0
#         df = df.rename(columns={ 0: "releve" })
#         # On filtre les odnnees ggrace a loc[]
#         donne_filtrer = df.loc[df['releve'] > self.seuil_bruit]
#         # On s'assure que le nombres de donnees brut filtrere est plus important que les donnee filtrer
#         resultat = np.where(len(donne_filtrer) < len(releve_brut) / 2, "pasbon", 'ok')
#         # On creer une var debit
#         debit = self.coeff_a * (donne_filtrer['releve'] ** 2)
#         # print(debit)

#         print(f'Resultat {resultat}')
#         print(f'Debit {debit}')


# data = [0.01, 1.2, 0.8, -0.5, 2.1, 0.04]
# stationHydrometrique = StationHydrometrique(15.5, 0.05)
# test = stationHydrometrique.calculerDebitStation(data)

# import numpy as np
# import pandas as pd

# class StationHydrometrique:
#     def __init__(self, coeff_a, seuil_bruit):
#         self.coeff_a = coeff_a
#         self.seuil_bruit = seuil_bruit

#     def calculer_debit_station(self, releves_bruts):
#         # 1. Conversion et nettoyage
#         df = np.array(releves_bruts)
#         df = pd.DataFrame(releves_bruts, columns=["hauteur"])
        
#         # On ne garde que les valeurs au-dessus du seuil de bruit
#         donnees_filtrees = df.loc[df["hauteur"] > self.seuil_bruit]

#         # 2. Vérification de la fiabilité (Règle des 50%)
#         if len(donnees_filtrees) < len(releves_bruts) / 2:
#             print("Alerte : Trop de données aberrantes, calcul annulé.")
#             return None

#         # 3. Calcul vectorisé du débit (Q = a * H^2)
#         # On travaille directement sur la colonne pour la performance
#         debits = self.coeff_a * (donnees_filtrees["hauteur"] ** 2)

#         # 4. Résultat
#         max_debit = debits.max()
#         print(f"Débit max calculé : {max_debit:.2f} m3/s")
#         return debits

# # --- Exécution ---
# data = [0.01, 1.2, 0.8, -0.5, 2.1, 0.04, -1.0]
# station = StationHydrometrique(15.5, 0.05)
# station.calculer_debit_station(data)

import pandas as pd

class AnalyseurCrue:

    def __init__(self, seuil=0.5):
        self.seuil = seuil

    def differentiel(self, df):
        df['variation'] = df["hauteur"].diff()

        alerte = df.loc[df['variation'] > self.seuil]

        for ligne in alerte.itertuples():
            print(f"⚠️  Alerte : Variation de {ligne.variation:.2f}m détectée à {ligne.heure} heure")


data = {
    'heure': [1, 2, 3, 4, 5],
    'hauteur' : [2.5, 6, 0.4, 8, 3]
}

df = pd.DataFrame(data)
modele = AnalyseurCrue()
modele.differentiel(df)