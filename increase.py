import pandas as pd
import mlflow
def load_data(filename):
    return pd.read_csv(filename)

data = load_data('data.csv')

def increase_experience(df,column,scale):
    df[column]=df[column]+scale
    return df



if __name__=='__main__':
    import sys
    scale = int(sys.argv[1])
    ie = increase_experience(data,'no_languages',scale)
    with mlflow.start_run("incrementer"):

        ie.to_csv('increased.csv',index=False)
        mlflow.log_artifact('increased.csv')