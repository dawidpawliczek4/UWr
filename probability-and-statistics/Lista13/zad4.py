import pandas as pd
from scipy import stats

# Wczytanie danych z pliku, przypisanie nazw kolumn
df = pd.read_csv('./l13z04.csv', header=None, names=['Females', 'Males'])

# Rozdzielenie danych na dwie grupy
females = df['Females']
males = df['Males']

# 1. Podstawowe statystyki opisowe
mean_females = females.mean()
std_females = females.std(ddof=1)
n_females = females.count()

mean_males = males.mean()
std_males = males.std(ddof=1)
n_males = males.count()

print("Statystyki opisowe:")
print(f"Samice:   n = {n_females}, średnia = {mean_females:.2f}, odchylenie std = {std_females:.2f}")
print(f"Samce:    n = {n_males}, średnia = {mean_males:.2f}, odchylenie std = {std_males:.2f}\n")

# 2. Test Shapiro-Wilka (normalność)
shapiro_females = stats.shapiro(females)
shapiro_males = stats.shapiro(males)

print("Test Shapiro-Wilka (normalność):")
print(f"Samice:   W = {shapiro_females.statistic:.3f}, p = {shapiro_females.pvalue:.4f}")
print(f"Samce:    W = {shapiro_males.statistic:.3f}, p = {shapiro_males.pvalue:.4f}\n")

# 3. Test Levene'a (jednakowość wariancji)
levene_test = stats.levene(females, males)
print("Test Levene’a (jednakowość wariancji):")
print(f"Statystyka = {levene_test.statistic:.3f}, p = {levene_test.pvalue:.4f}\n")

# 4. Dobór testu t-Studenta w zależności od równości wariancji
equal_var = levene_test.pvalue > 0.05
ttest = stats.ttest_ind(females, males, equal_var=equal_var)

test_type = "standardowy (równe wariancje)" if equal_var else "Welch (nierówne wariancje)"
print(f"Test t-Studenta ({test_type}):")
print(f"t-statistic = {ttest.statistic:.3f}, p = {ttest.pvalue:.4f}")

# 5. Wniosek przy α = 0.05
alpha = 0.05
if ttest.pvalue < alpha:
    print("\nWniosek: Odrzucamy hipotezę zerową. Istnieje istotna różnica masy ciała między samicami a samcami (dymorfizm).")
else:
    print("\nWniosek: Brak podstaw do odrzucenia hipotezy zerowej. Różnica masy ciała nie jest statystycznie istotna.")
