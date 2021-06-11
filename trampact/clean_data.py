import pandas as pd
import os
import numpy as np

class data_sirene_nice:
    
    def __init__(self):
        pass
        
    def get_data():
        #----------info---------------
        #Recup data==>renvoie un dataframe
        #
        #Mise a jour: 11/06/2021
        #----------end info---------------

        # Path
        path_v2=".."
        path_v3 = "raw_data"
        fichier='sirene_nice.csv'
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





# #Trajet du tram


# point_trajet_tram = [
#     (43.723348, 7.285484),
#     (43.722790, 7.290817),
#     (43.722704, 7.291874),
#     (43.720651, 7.291798),
# #     (43.719062, 7.291645),
# #     (43.715879, 7.292795),
# #     (43.712934, 7.292888),
# #     (43.710972, 7.292880),
# #     (43.709340, 7.292795),
# #     (43.709450, 7.290437),
# #     (43.709786, 7.287875),
# #     (43.710190, 7.284755),
# #     (43.708508, 7.284264),
# #     (43.707059, 7.283689),
# #     (43.705349, 7.282687),
# #     (43.703214, 7.281455),
# #     (43.702443, 7.280966),
# #     (43.701225, 7.280326),
# #     (43.700631, 7.279172),
# #     (43.699138, 7.277533),
# #     (43.698672, 7.276971),
# #     (43.697897, 7.275090),
# #     (43.697187, 7.272679),
# #     (43.696685, 7.270893),
# #     (43.698019, 7.269681),
# #     (43.699845, 7.268490),
# #     (43.701178, 7.267574),
# #     (43.702567, 7.266745),
# #     (43.703401, 7.266268),
# #     (43.704280, 7.265685),
# #     (43.705236, 7.264954),
# #     (43.706646, 7.264215),
# #     (43.707540, 7.263591),
# #     (43.708626, 7.262950),
# #     (43.710118, 7.262038),
# #     (43.711479, 7.261802),
# #     (43.712329, 7.261797),
# #     (43.713166, 7.261695),
# #     (43.714659, 7.261582),
# #     (43.715760, 7.261507),
# #     (43.716424, 7.261377),
# #     (43.716302, 7.258503),
# #     (43.716691, 7.257332),
# #     (43.717184, 7.257020),
# #     (43.718247, 7.256880),
# #     (43.719692, 7.256671),
# #     (43.721241, 7.256449),
# #     (43.722773, 7.256240),
# #     (43.724218, 7.256022),
# #     (43.725607, 7.255808),
# #     (43.727023, 7.255607),
# #     (43.728406, 7.255398),
# #     (43.729575, 7.255262),
# #     (43.730707, 7.255024)
# ]


# #Selection des commerces proches du tram

# #Definition d'une messure de ref. LE 100M d'un stade d'athletisme
# #Mesure sur un stade d'athlétisme d'avignon stadde du college tavenaux Montfavet
# point_cent_metre=[(43.940717, 4.878154),
#            (43.941653, 4.877714)]
# #distance euclidenne
# cent_metre=((point_cent_metre[0][0]-point_cent_metre[1][0])**2+(point_cent_metre[0][1]-point_cent_metre[1][1])**2)**0.5
# print('100m de distance',cent_metre)
# cinq_cent_metre=5*cent_metre
# print('500m de distance',cinq_cent_metre)



if __name__=='__main__':
    # data=data_sirene_nice.get_data()
    # features=data_sirene_nice.get_feature()
    # liste_features=features.features.unique()
    print(data_sirene_nice.get_feature_interressant())
    entreprise_df_clean=data_sirene_nice.clean_data()
    print(entreprise_df_clean.head(5))
    print('ok')