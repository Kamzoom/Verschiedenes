import pandas as pd

# file_path = '/Users/kamillalauter/Downloads/analcatdata_bankruptcy.csv'
#
# # Laden der CSV-Datei
# df = pd.read_csv(file_path)
#
# # Ausgabe der ersten 5 Zeilen, um sicherzustellen, dass die Datei geladen wurde
# print(df.head())

 
file_path = '/Users/kamillalauter/Downloads/analcatdata_bankruptcy.csv'

# Laden der CSV-Datei
df = pd.read_csv(file_path)

# Ausgabe der Anzahl der Instanzen/Zeilen
print("Anzahl der Instanzen:", df.shape[0])
print("Anzahl der Merkmale:", df.shape[1])
print("Namen der Merkmale (Spalten):", df.columns.tolist())
# Entfernen der Spalte 'Company'
df = df.drop('Company', axis=1)

# Überprüfen des Ergebnisses durch Ausgabe der ersten 5 Zeilen
#print(df.head())
# Finde Zeilen, die 'NV' enthalten
nv_zeilen = df.isin(['NA']).any(axis=1)
#lösche alle Zeilen, die NA enthalten
df = df.dropna()
print("Anzahl der Merkmale:", df.shape[1])
print("Anzahl der Instanzen:", df.shape[0])
# Berechnung der Summe der Spalten  'WC/TA' und 'RE/TA'
summe_wc_ta = df['WC/TA'].sum()
summe_re_ta = df['RE/TA'].sum()
print("Summe von 'WC/TA':", summe_wc_ta, "Summe von 'RE/TA':", summe_re_ta)
#Produkt von 'EBIT/TA' und 'S/TA'
produkt = df['EBIT/TA'] * df['S/TA']
print("Produkt von 'EBIT/TA' und 'S/TA':", produkt)
file_path = '/Users/kamillalauter/Downloads/analcatdata_bankruptcy.csv'
#
# # Laden der CSV-Datei
df = pd.read_csv(file_path)
#erste Spalte Company hinzufügen
df['Company'] = df.index
print(df.head())
#Entfernen aller Zeilen mit dem Wert NA
df = df.dropna()
#Hinzufügen der Spalte Produkt und Summe
df['Produkt'] = df['EBIT/TA'] * df['S/TA']
df['Summe'] = df['WC/TA'] + df['RE/TA']
print(df.head())
#Instanzen 10 bis 20 und alle Merkmale
print(df.iloc[10:20, :])
#Die Merkmale in den ersten vier Spalten und alle Instanzen
print(df.iloc[:, :4])
#Die Merkmale WC/TA und EBIT/TA und nur die Instanzen bei den RE/TA kleiner als -20 ist
print(df.loc[df['RE/TA'] < -20, ['WC/TA', 'EBIT/TA']])
#Alle Mermale und nur die Instanzen, bei den RE/TA kleiner -20 und bankrupt null ist
print(df.loc[(df['RE/TA'] < -20) & (df['Bankrupt'] == 0), :])
#Merkmale WC/TA und EBIT/TA und nur die Instanzen, bei denen RE/TA kleiner -20 oder bankrupt null ist
print(df.loc[(df['RE/TA'] < -20) | (df['Bankrupt'] == 0), ['WC/TA', 'EBIT/TA']])

