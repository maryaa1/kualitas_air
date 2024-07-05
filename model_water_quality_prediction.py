# -*- coding: utf-8 -*-
"""Model_Water Quality prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mIgwbYL7XQpecZ1vETRfn2bulpPnwjj5

------------------------------------------
## import libraries
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.figure_factory as ff

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation,Dropout

data = pd.read_csv('water_potability.csv')

data

data.isnull().sum()

"""-----------------------------------------
## EDA
"""

fig, ax = plt.subplots(figsize = (18,18))
sns.heatmap(data.corr(), ax = ax, annot = True)

fig,ax = plt.subplots(figsize=(8,8))
abs(data.corr().round(2)['Potability']).sort_values()[:-1].plot.barh(color='c')

data[data['Potability']==0][['ph','Sulfate','Trihalomethanes']].median()

data['ph'].fillna(value=data['ph'].median(),inplace=True)
data['Trihalomethanes'].fillna(value=data['Trihalomethanes'].median(),inplace=True)
data = data.dropna()

data.isnull().sum()

data.shape

data.info()

fig,ax = plt.subplots(figsize=(8,8))
abs(data.corr().round(2)['Potability']).sort_values()[:-1].plot.barh(color='c')

data.corr()['Potability'][:-1].sort_values().plot(kind='bar')

trace = go.Pie(labels = ['Potable', 'Not Potable'], values = data['Potability'].value_counts(),
               textfont=dict(size=15), opacity = 0.8,
               marker=dict(colors=['lightskyblue','gold'],
                           line=dict(color='#000000', width=1.5)))


layout = dict(title =  'Distribution of Drinkable Water')

fig = dict(data = [trace], layout=layout)
py.iplot(fig)

plt.figure(figsize = (15,10), tight_layout = True)

for i, feature in enumerate(data.columns):
    if feature != 'Potability':

        plt.subplot(3,3,i+1)
        sns.histplot(data = data, x =feature, palette = 'mako', hue = 'Potability',alpha = 0.5, element="step",hue_order=[1,0] )

sns.pairplot(data = data,hue = 'Potability',palette='mako_r', corner=True)

"""-----------------------------------------
## Data Splitting
"""

X = data.drop('Potability',axis=1).values
y = data['Potability'].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=40)

"""-----------------------------
## Data Scalling
"""

scaler = MinMaxScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print('training shape : ',X_train.shape)
print('testing shape : ',X_test.shape)

"""------------------------------
## Modelling
"""

model = Sequential() # Initialising the ANN

model.add(Dense(units = 16, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 9, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 2, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
model.compile(optimizer = 'adam', loss = 'binary_crossentropy')

model.fit(x=X_train,
          y=y_train,
          epochs=100,
          validation_data=(X_test, y_test), verbose=1
          )

model_loss = pd.DataFrame(model.history.history)

model_loss.plot()

y_pred = model.predict(X_test)
y_pred = [ 1 if y>=0.5 else 0 for y in y_pred ]

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,y_pred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

accuracy = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
print("Accuracy: "+ str(accuracy*100)+"%")

model = Sequential()
model.add(Dense(units=16,activation='relu'))
model.add(Dense(units=8,activation='relu'))
model.add(Dense(units=4,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(x=X_train,
          y=y_train,
          epochs=200,
          validation_data=(X_test, y_test), verbose=1
          )

model_loss = pd.DataFrame(model.history.history)
model_loss.plot()

y_pred = model.predict(X_test)
y_pred = [ 1 if y>=0.5 else 0 for y in y_pred ]

print(classification_report(y_test,y_pred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

accuracy = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
print("Accuracy: "+ str(accuracy*100)+"%")

model = Sequential()
model.add(Dense(units=10,activation='relu'))
model.add(Dense(units=8,activation='relu'))
model.add(Dense(units=8,activation='relu'))
model.add(Dense(units=6,activation='relu'))
model.add(Dense(units=6,activation='tanh'))
model.add(Dense(units=5,activation='relu'))
model.add(Dense(units=1,activation='tanh'))
model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(x=X_train,
          y=y_train,
          epochs=300,
          validation_data=(X_test, y_test), verbose=1
          )

model_loss = pd.DataFrame(model.history.history)
model_loss.plot()

y_pred = model.predict(X_test)
y_pred = [ 1 if y>=0.5 else 0 for y in y_pred ]

print(classification_report(y_test,y_pred))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

accuracy = (cm[0][0]+cm[1][1])/(cm[0][0]+cm[0][1]+cm[1][0]+cm[1][1])
print("Accuracy: "+ str(accuracy*100)+"%")

print("Masukkan nilai untuk fitur berikut:")
pH = float(input("pH: "))
hardness = float(input("Hardness: "))
solids = float(input("Solids: "))
chloramines = float(input("Chloramines: "))
sulfate = float(input("Sulfate: "))
conductivity = float(input("Conductivity: "))
organic_carbon = float(input("Organic Carbon: "))
trihalomethanes = float(input("Trihalomethanes: "))
turbidity = float(input("Turbidity: "))

# Membuat DataFrame dari input
input_data = pd.DataFrame({
    'pH': [pH],
    'Hardness': [hardness],
    'Solids': [solids],
    'Chloramines': [chloramines],
    'Sulfate': [sulfate],
    'Conductivity': [conductivity],
    'Organic_carbon': [organic_carbon],
    'Trihalomethanes': [trihalomethanes],
    'Turbidity': [turbidity]
})

# Normalisasi data input
input_normalized = scaler.transform(input_data)

# Menggunakan model untuk membuat prediksi
prediction = model.predict(input_normalized)
predicted_label = (prediction > 0.5).astype(int)  # Mengasumsikan threshold 0.5 untuk klasifikasi

# Menampilkan hasil prediksi
print(f"Prediksi kualitas air (0: Tidak layak minum, 1: Layak minum): {predicted_label[0]}")

import pickle

# Menyimpan model
filename = 'model_water_quality_prediction.sav'  # Memperbaiki spasi yang tidak perlu dalam nama file
with open(filename, 'wb') as file:
    pickle.dump(model, file)