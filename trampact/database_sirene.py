import pandas as pd
import os
import numpy as np

class Data_sirene_nice:
    
    def __init__(self):
        pass
        
    def get_data(fichier='sirene_nice.csv'):
        #----------info---------------
        #Recup data==>renvoie un dataframe
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        # Path
        path_v2=".."
        path_v3 = "raw_data"
        # Join various path components 
        fichier=os.path.join(path_v2,path_v3, fichier)
        entreprise_df = pd.read_csv(fichier,delimiter=";")
        return entreprise_df

    def get_feature():
        #----------info---------------
        #Recup feature du dataset==>renvoie un dataframe
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        entreprise_df=Data_sirene_nice.get_data()
        features=pd.DataFrame(entreprise_df.columns,columns=["features"])
        return features
    
    def get_feature_interressant():
        #----------info---------------
        #liste toutes les features interressants
        #   ==>renvoie liste
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
         Feature_interessant=["siret",
                               "Date de création de l'établissement",
                               "Date de création de l'unité légale",
                               "Date de fermeture de l'établissement",
                               "Date de fermeture de l'unité légale",
                               "Date du début de la période de l'établissement",
                               "Date de la dernière mise à jour de l'établissement",
                               "Nombre de periodes de l'établissement",
                               "etat_etab",
                               "Enseigne de l'établissement 1",
                               "Civilité de la personne physique",
                               "Nom de la personne physique",
                               "effectifs",
                               "Catégorie de l'entreprise",
                               "Section de l'établissement",
                               "Sous-section de l'établissement",
                               "Division de l'établissement",
                               "Groupe de l'établissement",
                               "Classe de l'établissement",
                               "Nature juridique de l'unité légale",
                               "Adresse de l'établissement",
                               "communes",
                               "y", "x"]
         return Feature_interessant

    def clean_data():
        #----------info---------------
        #RClean data
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        entreprise_df=Data_sirene_nice.get_data()
        #Convertion de donnée data
        entreprise_df["Date de création de l'établissement"]=\
        entreprise_df["Date de création de l'établissement"].replace(' ',"1944-08-28")
        entreprise_df["Date de création de l'établissement"]=pd.to_datetime(entreprise_df["Date de création de l'établissement"])
            
        entreprise_df["Date de création de l'unité légale"]=\
        entreprise_df["Date de création de l'unité légale"].replace(' ',"1944-08-28")
        entreprise_df["Date de création de l'unité légale"]=pd.to_datetime(entreprise_df["Date de création de l'unité légale"])

        entreprise_df["Date de fermeture de l'établissement"]=\
        entreprise_df["Date de fermeture de l'établissement"].replace(' ',"1944-08-28")
        entreprise_df["Date de fermeture de l'établissement"]=pd.to_datetime(entreprise_df["Date de fermeture de l'établissement"])

        entreprise_df["Date du début de la période de l'établissement"]=\
        entreprise_df["Date du début de la période de l'établissement"].replace(' ',"1944-08-28")
        entreprise_df["Date du début de la période de l'établissement"]=pd.to_datetime(entreprise_df["Date du début de la période de l'établissement"])

        entreprise_df["Date de la dernière mise à jour de l'établissement"]=\
        entreprise_df["Date de la dernière mise à jour de l'établissement"].replace(' ',"1944-08-28")
        entreprise_df["Date de la dernière mise à jour de l'établissement"]=pd.to_datetime(entreprise_df["Date de la dernière mise à jour de l'établissement"])

        #Clean coordonate
        entreprise_df["lenght_x"]=entreprise_df.x.apply(lambda x: len(x))
        entreprise_df["lenght_y"]=entreprise_df.y.apply(lambda x: len(x))

        #Entreprise avec des coordonnées
        entreprise_df_clean_coord=\
        entreprise_df[
                        np.logical_and(
                                        entreprise_df.lenght_x>1,
                                        entreprise_df.lenght_y>1
                                        )
                    ].reset_index(drop=True)

        #clean
        entreprise_df_clean_coord.y=pd.to_numeric(entreprise_df_clean_coord.y)
        entreprise_df_clean_coord.x=pd.to_numeric(entreprise_df_clean_coord.x)
        entreprise_df_clean_coord=entreprise_df_clean_coord.drop(['lenght_x', 'lenght_y'], axis=1)
            
        # #Entreprise sans de coordonnées
        # entreprise_df_ss_coord=\
        # entreprise_df[
        #               np.logical_and(
        #                              entreprise_df.lenght_x>1,
        #                              entreprise_df.lenght_y>1
        #                              )==False
        #              ].reset_index(drop=True)
        # entreprise_df_ss_coord=entreprise_df_ss_coord.drop(['lenght_x', 'lenght_y'], axis=1)
        return entreprise_df_clean_coord

    def trace_tramway(fichier='coord_T1.csv'):
        #----------info---------------
        #Recup les coords du tram t1 dans csv
        # ==>return un dataframe
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        # Path
        path_v2=".."
        path_v3 = "raw_data"
        # Join various path components 
        fichier=os.path.join(path_v2,path_v3, fichier)
        point_trajet_tram_df = pd.read_csv(fichier)
        return point_trajet_tram_df
        
    def sirene_distance_df():
        #----------info---------------
        #Renvoie le dataframe original avec 2 features supplementaire
        #2 nouvelles features:
        #  1) distance tram t1 ==> Distance entre le commerce et la ligne de t1
        #  2) proche tram t1 ==> 'oui' ou 'non' indique si le commerce est proche de 500 m de la ligne de tram
        # Return==> dataframe
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        #Definition d'une messure de ref. LE 100M d'un stade d'athletisme
        #Mesure sur un stade d'athlétisme d'avignon stadde du college tavenaux Montfavet
        point_cent_metre=[(43.940717, 4.878154),
                          (43.941653, 4.877714)]
        #distance euclidenne
        cent_metre=((point_cent_metre[0][0]-point_cent_metre[1][0])**2+(point_cent_metre[0][1]-point_cent_metre[1][1])**2)**0.5
        #print('100m de distance',cent_metre)
        cinq_cent_metre=5*cent_metre
        #print('500m de distance',cinq_cent_metre)
        
        #recup le data set
        entreprise_df_clean_coord=Data_sirene_nice.clean_data()
        entreprise_df_clean_coord_reduc=entreprise_df_clean_coord.loc[:,['siret','y','x']]
        point_trajet_tram_df=Data_sirene_nice.trace_tramway()
        #Calcul des distance entre les commerces et la ligne de tram.
        #2 nouvelles features:
        #  1) distance tram t1 ==> Distance entre le commerce et la ligne de t1
        #  2) proche tram t1 ==> 'oui' ou 'non' indique si le commerce est proche de 500 m de la ligne de tram
        distance_proche_T1=[]
        tmp_distance=99999999999.9
        for i in range(0,len(entreprise_df_clean_coord_reduc)):
            tmp_distance=99999999999.9
            oui=0
            for ii in range( 0, len(point_trajet_tram_df)):
                #calcul de la distance entre 1 point tram (ii) et le commerce(i)
                distance=(
                    (entreprise_df_clean_coord_reduc.y[i]-point_trajet_tram_df.y[ii])**2+
                    (entreprise_df_clean_coord_reduc.x[i]-point_trajet_tram_df.x[ii])**2
                    )**0.5
                if distance<tmp_distance:
                        tmp_distance=distance
            #Convertion en distance mettre
            tmp_distance_metre=(500*tmp_distance)/cinq_cent_metre
            #Convertion en distance mettre
            distance_proche_T1.append(round(tmp_distance_metre,2))
        #Injection dans le data frame initial
        entreprise_t1_df=pd.concat([
                                entreprise_df_clean_coord,
                                pd.DataFrame(distance_proche_T1,columns=['distance tram t1'])    
                                    ], axis=1)
        #Creation de la feature "proche t1" avec oui ou non
        entreprise_t1_df["proche t1"]=\
        entreprise_t1_df['distance tram t1'].apply(lambda x: 'oui' if x<=500 else 'non')       
        return entreprise_t1_df  
    
    def sirene_t1_df():
        #----------info---------------
        #Renvoie avec les entreprise proche de la T1
        #   ==> dataframe
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        entreprise_t1_df=Data_sirene_nice.sirene_distance_df()
        entreprise_proche_t1_df=entreprise_t1_df[entreprise_t1_df["proche t1"]=='oui']
        entreprise_proche_t1_df=entreprise_proche_t1_df.reset_index(drop=True)
        return entreprise_proche_t1_df
    
    def ecriture_sirene_clean(fichier='sirene_nice_clean.csv'):
        #----------info---------------
        #Ecriture du fichier sirene propre
        # ==>
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        # Path
        path_v2=".."
        path_v3 = "raw_data"
        # Join various path components 
        fichier_out=os.path.join(path_v2,path_v3, fichier)
        #recup dataframe
        entreprise_df=Data_sirene_nice.sirene_distance_df()
        #dataframe clean ==> sortie CSV
        entreprise_df.to_csv(fichier_out)
        return f"generation du ficher {fichier_out}: ok"
    
    def ecriture_sirene_t1_clean(fichier_t1='sirene_nice_clean_T1.csv'):
        #----------info---------------
        #Ecriture du fichier sirene prochde de t1 propre
        # ==>
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------
        # Path
        path_v2=".."
        path_v3 = "raw_data"
        # Join various path components 
        fichier_out=os.path.join(path_v2,path_v3, fichier_t1)
        #recup dataframe
        entreprise_df=Data_sirene_nice.sirene_t1_df()
        #dataframe clean ==> sortie CSV
        entreprise_df.to_csv(fichier_out)
        return f"generation du ficher {fichier_t1}: ok"
    
# if __name__=='__main__':
#     # data=Data_sirene_nice.get_data()
#     # features=Data_sirene_nice.get_feature()
#     # liste_features=features.features.unique()
#     #print(Data_sirene_nice.get_feature_interressant())
#     #entreprise_df_clean=Data_sirene_nice.clean_data()
#     #print(entreprise_df_clean)
#     entreprise_df=Data_sirene_nice.sirene_distance_df()
#     entreprise_t1_df=Data_sirene_nice.sirene_t1_df()
#     print('ok')