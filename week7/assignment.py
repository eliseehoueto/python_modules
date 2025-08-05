import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('sales_data.csv')
    print("Le jeu de données a été chargé avec succès.")
except FileNotFoundError:
    print("Error. The file is not found")
    exit()

print("\n--- Exploration initiale des données ---")
print("\nAffichage des 5 premières lignes du jeu de données :")
print(df.head())

print("\nInformations sur le jeu de données (types de colonnes, valeurs non-nulles) :")
df.info()

print("\nStatistiques descriptives pour les colonnes numériques :")
print(df.describe())

print("\nNombre de valeurs manquantes par colonne :")
print(df.isnull().sum())

print("\n--- Analyse de données ---")


if 'product' in df.columns:
    nombre_par_categorie = df['product'].value_counts()
    print("\nNElements numbers by category :")
    print(nombre_par_categorie)
else:
    print("\nColumn not seen.")

if 'Revenue ($)' in df.columns:
    moyenne_valeur = df['Revenue ($)'].mean()
    print(f"\nMeen of column 'Revenue ($)' : {moyenne_valeur:.2f}")
else:
    print("\nThe column Revenue ($) don't exist")


if 'Revenue ($)' in df.columns:
    plt.figure(figsize=(8, 6))
    df['Revenue ($)'].hist(bins=20)
    plt.title( 'Revenue ($)')
    plt.xlabel('Revenue ($)')
    plt.ylabel('Fréquency')
    plt.grid(True)
    plt.show()

if 'product' in df.columns:
    nombre_par_categorie.plot(kind='bar', figsize=(10, 6))
    plt.title('Répartition by ' + 'product')
    plt.xlabel('product')
    plt.ylabel('product')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() 
    plt.show()
else:
    print("We can't create a diagram ")

