
from sklearn import pipeline
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


pd.set_option('display.max_columns', None)

df_train = pd.read_csv('uclm_student_train.csv')
df_train

df_test = pd.read_csv('uclm_student_test.csv')
df_test


#arbol de decision, naive bayes - libreria sklearn
#estos evitan la fuga de datos
#StandardScaler antes de hacer validacion cruzada 

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

def StudentGen():
    

