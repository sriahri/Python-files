def preprocess(df):
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    df.fillna(0)
    scaler = preprocessing.StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)
    return (X_train, y_train), (X_test, y_test)


# To get the results for Q11 to Q14

(X_train, y_train), (X_test, y_test) = preprocess(df)
X_train[6][13]
X_test[6][13]
y_train[16]
y_test[16]
