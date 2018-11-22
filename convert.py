#import the libraries needed

import pandas as pd

#read the csv file
df = pd.read_csv('Airbnb_Texas_Rentals.csv',index_col=0)

df['description'].fillna(' ',inplace=True)

df['title'].fillna(' ',inplace=True)

#create .tsv files for every doc.

for i in range(len(df)):

    name = 'directory/doc_{}.tsv'.format(i+1)

    df.iloc[i].to_csv(name,sep='\t', index=False)