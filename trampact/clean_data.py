import pandas as pd
import os
import numpy as np

class data_sirene_nice:
    
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
        entreprise_df=data_sirene_nice.get_data()
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
        entreprise_df=data_sirene_nice.get_data()
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
        
    def calcul_feature_distance():
        #----------info---------------
        #Calcul les distances des entreprise et la ligne de tram
        # ==>
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
        entreprise_df_clean_coord=data_sirene_nice.clean_data()
        entreprise_df_clean_coord=entreprise_df_clean_coord.loc[:,['siret','y','x']]
        point_trajet_tram_df=data_sirene_nice.trace_tramway()
        #Calcul des distance entre les commerces et la ligne de tram.
        #2 nouvelles features:
        #  1) distance tram t1 ==> Distance entre le commerce et la ligne de t1
        #  2) proche tram t1 ==> 'oui' ou 'non' indique si le commerce est proche de 100 m de la ligne de tram
        siret_proche_T1=[]
        proche_T1=[]
        distance_proche_T1=[]
        tmp_distance=99999999999.9
        for i in range(0,len(entreprise_df_clean_coord)):
            tmp_distance=99999999999.9
            oui=0
            for ii in range( 0, len(point_trajet_tram_df)):
                #calcul de la distance entre 1 point tram (ii) et le commerce(i)
                distance=(
                    (entreprise_df_clean_coord.y[i]-point_trajet_tram_df.y[ii])**2+
                    (entreprise_df_clean_coord.x[i]-point_trajet_tram_df.x[ii])**2
                    )**0.5
                if distance<tmp_distance:
                        tmp_distance=distance
                if distance <cinq_cent_metre:
                    oui=1
            if oui:
                if len(siret_proche_T1)>=1:
                    siret_unique=0
                    for iii in range(0,len(siret_proche_T1)):
                        if entreprise_df_clean_coord.siret[i]==siret_proche_T1[iii]:
                            siret_unique=1    
                    if siret_unique:
                        proche_T1.append('oui')
                        siret_proche_T1.append(entreprise_df_clean_coord.siret[i])
                else:
                    proche_T1.append('oui')
                    siret_proche_T1.append(entreprise_df_clean_coord.siret[i])
            else:
                proche_T1.append('non')
                siret_proche_T1.append(entreprise_df_clean_coord.siret[i])
            #Convertion en distance mettre
            tmp_distance_metre=(500*tmp_distance)/cinq_cent_metre
            #Convertion en distance mettre
            distance_proche_T1.append(round(tmp_distance_metre,2))



if __name__=='__main__':
    # data=data_sirene_nice.get_data()
    # features=data_sirene_nice.get_feature()
    # liste_features=features.features.unique()
    #print(data_sirene_nice.get_feature_interressant())
    #entreprise_df_clean=data_sirene_nice.clean_data()
    #print(entreprise_df_clean)
    test=data_sirene_nice.calcul_feature_distance()
    
    print('ok')