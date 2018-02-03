from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn import preprocessing, ensemble
from sklearn.externals import joblib

def load_train_data():
    train = pd.read_csv('train.csv')
    labels = train.target.values
    lbl_enc = preprocessing.LabelEncoder()
    labels = lbl_enc.fit_transform(labels)

    train = train.drop('id', axis=1)
    train = train.drop('target', axis=1)
    return train.values, labels.astype('int32')


def train_model_knn(train,labels):
    # train a K Nearest Neighbour classifier
    model = KNeighborsClassifier(n_neighbors=8, metric='euclidean',n_jobs=-1)
    model.fit(train, labels)
    joblib.dump(model, 'knn_model_euclidean3.model') 
    return model


X, y = load_train_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1624)
model = train_model_knn(X_train,y_train)
preds = model.predict_proba(X_test)
print "MLogloss: ", log_loss(y_test, preds)