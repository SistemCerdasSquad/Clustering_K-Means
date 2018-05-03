# # Load Dataset

import pandas as pd

df = pd.read_csv('data.csv',header=None)
# print(df)


# # Preprocessing
X = []
for value in df[1]:
     X.append([value])


# # Create Model

from sklearn.cluster import KMeans

cls = KMeans(n_clusters=2,random_state=0,max_iter=1000)

cls.fit(X)


# # Testing Model
datatest = pd.read_csv('testing.csv',header=None)

for (laptop,harga) in zip(datatest[0],datatest[1]):
    predict = "murah" if cls.predict([[harga]])[0] == 0 else "mahal"
    print("laptop {laptop} dengan harga {harga} itu {hasil}".format(laptop=laptop,harga=harga,hasil=predict))




