import os
import pandas as pd
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
  
    
    def get_feature_ml_interressant():
        #----------info---------------
        #liste toutes les features interressants pour le machine learning
        #   ==>renvoie liste
        #
        #Mise a jour: 12/06/2021
        #----------end info---------------
        Feature_ml_interessant=[
                "Date de création de l'unité légale",
                "Date de fermeture de l'unité légale",
                #"Date de la dernière mise à jour de l'établissement",
                #"etat_etab",
                "effectifs",
                "Classe de l'établissement",
                #"Nature juridique de l'unité légale",
                #"distance tram t1",
                "proche t1"]
        return Feature_ml_interessant
    
    
    def encoder_feature():
        #----------info---------------
        #Encodage des features pour le machine learning
        #"Encodage" sur les dates ==> 2006-04-31==>2006
        #   ==> dataframe
        #
        #Mise a jour: 12/06/2021
        #----------end info---------------
        entreprise_df=Machine_learning_sirene.get_data_clean()
        feature=Machine_learning_sirene.get_feature_ml_interressant()
        entreprise_ml_df=entreprise_df[feature]
        
        # encodage de "Classe de l'établissement"
        ohe = OneHotEncoder(sparse = False) # Instanciate encoder
        ohe.fit(entreprise_ml_df[["Classe de l'établissement"]]) # Fit encoder
        liste_encodage=list(ohe.categories_[0])
        etablissement_encoder=ohe.transform(entreprise_ml_df[["Classe de l'établissement"]])
        add_df=pd.concat([
                        entreprise_ml_df["Classe de l'établissement"],
                        pd.DataFrame(etablissement_encoder,columns = list(liste_encodage))
                        ],axis=1)
        ##injection dans le dataframe
        entreprise_ml_df_encoder_0=pd.concat([
                                entreprise_ml_df,
                                add_df    
                                ],axis=1)
        entreprise_ml_df_encoder_0=entreprise_ml_df_encoder_0.drop(columns="Classe de l'établissement")
        
        # encodage de "effectifs"
        ohe = OneHotEncoder(sparse = False) # Instanciate encoder
        ohe.fit(entreprise_ml_df[["effectifs"]]) # Fit encoder
        liste_encodage=list(ohe.categories_[0])
        etablissement_encoder=ohe.transform(entreprise_ml_df[["effectifs"]])
        add_df=pd.concat([
                        entreprise_ml_df["effectifs"],
                        pd.DataFrame(etablissement_encoder,columns = liste_encodage)
                        ],axis=1)
        ##injection dans le dataframe
        entreprise_ml_df_encoder_1=pd.concat([
                                entreprise_ml_df_encoder_0,
                                add_df    
                                ],axis=1)
        entreprise_ml_df_encoder_1=entreprise_ml_df_encoder_1.drop(columns="effectifs")
        
        # encodage de "proche de t1"
        ohe = OneHotEncoder(drop='if_binary',sparse = False) # Instanciate encoder
        ohe.fit(entreprise_ml_df[["proche t1"]]) # Fit encoder
        entreprise_ml_df_encoder_1["proche t1"]=ohe.transform(entreprise_df[["proche t1"]])
        
        #"Encodage sur les dates"
        #"Date de création de l'unité légale",
        entreprise_ml_df_encoder_1["Date de création de l'unité légale"]=\
        entreprise_ml_df_encoder_1["Date de création de l'unité légale"].dt.year
        #"Date de fermeture de l'unité légale"
        entreprise_ml_df_encoder_1["Date de fermeture de l'unité légale"]=\
        entreprise_ml_df_encoder_1["Date de fermeture de l'unité légale"].dt.year
        return entreprise_ml_df_encoder_1


# if __name__=='__main__':
#     # data=Machine_learning_sirene.get_data_clean()
#     # entreprise_ml_df=Machine_learning_sirene.encoder_feature()
#     # print(entreprise_ml_df)
#     print('ok')