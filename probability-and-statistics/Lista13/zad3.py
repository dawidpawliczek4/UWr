import pandas as pd
from scipy import stats

# 1. Wczytanie danych bez nagłówka, przypisanie własnych nazw kolumn
df = pd.read_csv('./l13z03.csv', header=None, names=['Gegawy', 'Posiewnice'])

# 2. Rozdzielenie danych na dwie grupy
gegawy = df['Gegawy']
posiewnice = df['Posiewnice']

# 3. Podstawowe statystyki opisowe
mean_gegawy = gegawy.mean()
std_gegawy = gegawy.std(ddof=1)
n_gegawy = gegawy.count()

mean_posiewnice = posiewnice.mean()
std_posiewnice = posiewnice.std(ddof=1)
n_posiewnice = posiewnice.count()

print("Statystyki opisowe:")
print(f"Gęgawy:   n = {n_gegawy}, średnia = {mean_gegawy:.2f}, odchylenie std = {std_gegawy:.2f}")
print(f"Posiewnice: n = {n_posiewnice}, średnia = {mean_posiewnice:.2f}, odchylenie std = {std_posiewnice:.2f}\n")

# 4. Test Shapiro-Wilka (normalność)
shapiro_gegawy = stats.shapiro(gegawy)
shapiro_posiewnice = stats.shapiro(posiewnice)

print("Test Shapiro-Wilka (normalność):")
print(f"Gęgawy:   W = {shapiro_gegawy.statistic:.3f}, p = {shapiro_gegawy.pvalue:.4f}")
print(f"Posiewnice: W = {shapiro_posiewnice.statistic:.3f}, p = {shapiro_posiewnice.pvalue:.4f}\n")


# 5. Test Levene’a (jednakowość wariancji)
levene_test = stats.levene(gegawy, posiewnice)
print("Test Levene’a (jednakowość wariancji):")
print(f"Statystyka = {levene_test.statistic:.3f}, p = {levene_test.pvalue:.4f}\n")
# to mniejsze niz 0.05, wiec odrzucamy hopoteze
# uznajemy, ze wariancja nierowna


# 6. Test t-Studenta Walcha (porównanie średnich, nierówne wariancje)
ttest_welch = stats.ttest_ind(gegawy, posiewnice, equal_var=False)
print("Test t-Studenta (Welch, nierówne wariancje):")
print(f"t-statistic = {ttest_welch.statistic:.3f}, p = {ttest_welch.pvalue:.4f}")
#to znow odrzucamy