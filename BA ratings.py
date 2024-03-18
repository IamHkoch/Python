##raw data prior cleaned on Excel

import pandas as pd

Data = pd.read_csv(r"/Users/koch/PycharmProjects/pythonProject/BA_reviews/BA_reviews_clean.csv")

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 1000)

##EDA

Data.info()
Data.describe()
Data['seat_type'].value_counts()
Data['traveller_type'].value_counts()
Data['trip_verified'].value_counts()
Data['recommended'].value_counts()

##DC
##finding null values

Data.isnull().sum()
print(Data.isnull().sum())

##replacing missing values

Data['trip_verified'] = Data['trip_verified'].fillna('Not Verified')
Data['date_flown'].fillna('Unknown', inplace=True)

Mode_TT = Data['traveller_type'].mode()[0]
print(Mode_TT)
Data['traveller_type'] = Data['traveller_type'].fillna('Couple Leisure')

Mode_ST = Data['seat_type'].mode()[0]
print(Mode_ST)
Data['seat_type'] = Data['seat_type'].fillna('Economy Class')

Data.isnull().sum()

##further DC

Data['place'] = Data['place'].str.title()
Data['traveller_type'] = Data['traveller_type'].str.title()
Data['seat_type'] = Data['seat_type'].str.title()
Data['recommended'] = Data['recommended'].str.title()
Data['trip_verified'] = Data['trip_verified'].str.title()

Data.rename(columns = {'place' : 'country'}, inplace=True)

Data['country'].value_counts().unique
print(Data['country'].value_counts().unique)

print(Data.describe())

##visualising

import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

##pulling the mean and mode for x categories

Data['traveller_type'].value_counts()
print(Data['traveller_type'].value_counts())

Data1 = {
    'traveller_type': ['Couple Leisure', 'Solo Leisure', 'Business', 'Family Leisure'],
    'rating': [0,3,6,10],
}

Df1 = pd.DataFrame(Data1)

Totals1 = Df1.groupby('traveller_type')['rating'].mean().round(2)
Mode_for_traveller_type = Df1.groupby('traveller_type')['rating'].apply(lambda x: x.mode().iloc[0])

print(Totals1)
print(Mode_for_traveller_type)

##barplot average rating per traveller type

Totals = Df1.groupby('traveller_type')['rating'].mean().reset_index()

plt.bar(Totals['traveller_type'], Totals['rating'], color = 'red')

plt.xlabel('Traveller type')
plt.ylabel('Customer rating')
plt.title('Average rating per type of traveller')

plt.tight_layout()
plt.show()

##Average rating per seat class

Data['seat_type'].value_counts()
print(Data['seat_type'].value_counts())

Data2 = {
    'seat_type': ['Economy Class', 'Business Class', 'Premium Economy', 'First Class'],
    'rating': [0,3,6,10]
}

Df2 = pd.DataFrame(Data2)

Totals2 = Df2.groupby('seat_type')['rating'].mean()

print(Totals2)

Totals3 = Df2.groupby('seat_type')['rating'].mean().reset_index()

plt.bar(Totals3['seat_type'], Totals3['rating'], color = 'blue')

plt.xlabel('Seat type')
plt.ylabel('Customer rating')
plt.title('Average rating ber seat class')

plt.tight_layout()
plt.show()