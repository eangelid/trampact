import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class Machine_learning_sirene:
    
    def __init__(self):
        pass

    def get_data_clean(fichier='sirene_nice_clean.csv'):
            #----------info---------------
            #Recup data==>renvoie un dataframe
            #
            #Mise a jour: 12/06/2021
            #----------end info---------------
            # Path
            path_v2=".."
            path_v3 = "raw_data"
            # Join various path components 
            fichier=os.path.join(path_v2,path_v3, fichier)
            entreprise_df = pd.read_csv(fichier)
            #Convertion date
            entreprise_df["Date de création de l'unité légale"]=pd.to_datetime(entreprise_df["Date de création de l'unité légale"])
            entreprise_df["Date de création de l'établissement"]=pd.to_datetime(entreprise_df["Date de création de l'établissement"])
            entreprise_df["Date du début de la période de l'établissement"]=pd.to_datetime(entreprise_df["Date du début de la période de l'établissement"])
            entreprise_df["Date de la dernière mise à jour de l'établissement"]=pd.to_datetime(entreprise_df["Date de la dernière mise à jour de l'établissement"])
            entreprise_df["Date de fermeture de l'établissement"]=pd.to_datetime(entreprise_df["Date de fermeture de l'établissement"])
            entreprise_df["Date de fermeture de l'unité légale"]=pd.to_datetime(entreprise_df["Date de fermeture de l'unité légale"])
            return entreprise_df
  
    
    # def get_feature_ml_interressant():
    #     #----------info---------------
    #     #liste toutes les features interressants pour le machine learning
    #     #   ==>renvoie liste
    #     #
    #     #Mise a jour: 12/06/2021
    #     #----------end info---------------
    #     Feature_ml_interessant=[
    #             "Date de création de l'unité légale",
    #             "Date de fermeture de l'unité légale",
    #             #"Date de la dernière mise à jour de l'établissement",
    #             #"etat_etab",
    #             "effectifs",
    #             "Classe de l'établissement",
    #             #"Nature juridique de l'unité légale",
    #             #"distance tram t1",
    #             "proche t1"]
    #     return Feature_ml_interessant
    
    
    def encoder_feature(list_feature, filtre_date=False, date_debut=2006,date_end=2012):
        #----------info---------------
        #Encodage des features pour le machine learning
        #Possibilité de creer un filtre par entre 2 date
        #
        #Input:list_feature==>Liste feature
        #Output==> dataframe, list encode x et y
        #
        #Target pour l'analyse ==>y "proche de t1"
        #X==> Autre feature
        #
        #Mise a jour: 14/06/2021
        #----------end info---------------
        entreprise_df=Machine_learning_sirene.get_data_clean()
        feature=list_feature#Machine_learning_sirene.get_feature_ml_interressant()
        entreprise_ml_df=entreprise_df[feature]
        
        #Simplification des features date
        #On garde que les années (on eleve les moins et les jours)
        #"Date de création de l'unité légale",
        entreprise_ml_df["Date de création de l'unité légale"]=\
        entreprise_ml_df["Date de création de l'unité légale"].dt.year
        #"Date de fermeture de l'unité légale"
        #entreprise_ml_df["Date de fermeture de l'unité légale"]=\
        #entreprise_ml_df["Date de fermeture de l'unité légale"].dt.year
        
        #Filtre par date:
        if filtre_date:
            entreprise_ml_df=entreprise_ml_df[
                                                np.logical_and(
                                                        entreprise_ml_df["Date de création de l'unité légale"]>= date_debut,
                                                        entreprise_ml_df["Date de création de l'unité légale"] <= date_end
                                                                )
                                                ].reset_index(drop=True)

        #Definition de X
        X=entreprise_ml_df.drop(columns="proche t1")
        #Definition de y
        y=entreprise_ml_df[["proche t1"]]

        
        # Encodage de X
        # 1. INSTANTIATE
        #Remarque importante, sparce=True (par defaut)
        ohe =OneHotEncoder()
        # 2. FIT
        ohe.fit(X)
        # 3. Transform
        X_encoder = ohe.transform(X).toarray()
        # 4. Recup categorie
        list_X_encoder=np.concatenate(ohe.categories_).tolist()
            #Autre methode
            # list_X_encoder=[]
            # for i in ohe.categories_:
            #     i=i.tolist()#==>Transforme l'array en liste
            #     list_X_encoder.extend(i)==>Met la liste dans une autre liste initial
        
        # Encodage de y
        # 1. INSTANTIATE
        #Remarque importante, sparce=True (par defaut)
        ohe_proche_t1 = OneHotEncoder(drop='if_binary') # Instanciate encoder
        # 2. FIT
        ohe_proche_t1.fit(y) # Fit encoder
        # 3. Transform
        y_encoder=ohe_proche_t1.transform(y).toarray()
        # 4. Recup categorie
        list_y_encoder=np.concatenate(ohe_proche_t1.categories_).tolist()
        
        return y_encoder, X_encoder, list_y_encoder, list_X_encoder


# if __name__=='__main__':
#     # data=Machine_learning_sirene.get_data_clean()
#     # entreprise_ml_df=Machine_learning_sirene.encoder_feature()
#     # print(entreprise_ml_df)
#     print('ok')