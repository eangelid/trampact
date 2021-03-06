import os
import pandas as pd

def get_data(file_name, is_local_csv=False):
    '''If is_local_csv==False, the method assumes that file_name is a valid URL'''
    df_data = None
    if is_local_csv:
        csv_path = os.path.join(os.path.dirname(__file__), 'data')

        df_data = pd.read_csv(os.path.join(csv_path, file_name), dtype={'iris_id': object})
        # df_data = pd.read_csv(os.path.join(csv_path, file_name), index_col='iris_id', dtype={'iris_id': object})
        # df_data = pd.read_csv(os.path.join(csv_path, file_name), dtype={'iris_id': object})
    else:
        df_data = pd.read_csv(file_name, index_col='iris_id')
    
    df_data = df_data.reset_index().set_index(['iris_id']).drop(columns=['index'])
    
    return df_data

def drop_tx_columns(data, year):
    return data.drop(columns=[
        f'tx_chom_{year}'
        ,f'tx_empl_{year}'
        ,f'tx_ouvr_{year}'
        ,f'tx_TP_{year}'
        ,f'tx_HLM_{year}'
        ,f'tx_no_transp_{year}'
        ,f'tx_walk_{year}'
        ,f'tx_moto_{year}'
        ,f'tx_voit_{year}'
        ,f'tx_TC_{year}'
        ,f'tx_HH_moins2ans_{year}'
        ,f'tx_HH_2_4ans_{year}'
        ,f'tx_HH_5_9ans_{year}'
        ,f'tx_HH_plus10ans_{year}'
        ,f'tx_HH_with_park_{year}'
        ,f'tx_HH_with_voit_{year}'
        ,f'tx_HH_1voit_{year}'
        ,f'tx_HH_2voit_{year}'
        ,f'tx_empl_prec_{year}'
    ])    

def drop_non_tx_columns(data, year):
    return data.drop(columns=[
        f'actifs_{year}'
        ,f'chom_{year}'
        ,f'empl_{year}'
        ,f'ouvrier_{year}'
        ,f'TP_{year}'
        ,f'Int_{year}'
        ,f'app_stage_{year}'
        ,f'cdd_{year}'
        ,f'rev_{year}'
        ,f'HLM_{year}'
        ,f'no_transp_{year}'
        ,f'walk_{year}'
        ,f'moto_{year}'
        ,f'voit_{year}'
        ,f'TC_{year}'
        ,f'HH_{year}'
        ,f'HH_moins2ans_{year}'
        ,f'HH_2_4ans_{year}'
        ,f'HH_5_9ans_{year}'
        ,f'HH_plus10ans_{year}'
        ,f'HH_with_park_{year}'
        ,f'HH_with_voit_{year}'
        ,f'HH_1voit_{year}'
        ,f'HH_2voit_{year}'
        ,f'pop_{year}'
    ])    

if __name__ == "__main__":
    dbx_url = "https://www.dropbox.com/s/r6kzjdo6l6qbdvg/BD_GENT_2006.csv?dl=1"
    local_csv = 'BD_GENT_2006.csv'
    df_gent_2006 = get_data(local_csv, is_local_csv=True)
    # df_gent_2006 = get_data(dbx_url, is_local_csv=False)
    print(df_gent_2006.shape)
    print(df_gent_2006.describe())
    
    print(df_gent_2006.nunique())

    print(df_gent_2006.info())

    # print(df_gent_2006.dtypes)
