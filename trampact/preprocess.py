import os
import pandas as pd

def get_data(file_name, is_local_csv=False):
    '''If is_local_csv==False, the method assumes that file_name is a valid URL'''
    df_data = None
    if is_local_csv:
        print(os.path.dirname(__file__))
        csv_path = os.path.join(os.path.dirname(__file__), 'data')

        df_data = pd.read_csv(os.path.join(csv_path, file_name))
    else:
        df_data = pd.read_csv(file_name)
        
    return df_data



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
