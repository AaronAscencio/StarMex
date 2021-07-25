import pandas as pd

import plotly.express as px

df = pd.read_csv("Space_Corrected.csv")
df['DateTime'] = pd.to_datetime(df['Datum'])
df['Year'] = df['DateTime'].apply(lambda datetime: datetime.year)


def country(Location):
    Location = Location[::-1]
    Location = Location[:Location.find(',')]
    Location = Location[::-1]
    Location = Location[1:]
    return Location

df["Country"] = df["Location"].apply(country)
#5 Paises con mas vuelos espaciales
#print(df['Country'].value_counts().head())
#print(df['Company Name'].value_counts())
#5 Compañias con mas vuelos
print(df['Company Name'].value_counts().head())

ds = df["Status Rocket"].value_counts().reset_index()
fig = px.pie(ds, values = "Status Rocket", names = "index", title = "Rocket Status")
fig.show()


ds = df["Status Mission"].value_counts().reset_index()[:3]
print(ds)

