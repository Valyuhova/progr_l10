import csv
import matplotlib.pyplot as plt
import numpy as np

FILENAME = "edu.csv"

YEARS = list(range(2000, 2020))
YEAR_COLS = [f"{y} [YR{y}]" for y in YEARS]


def read_country_data(country_name):
    years = []
    values = []

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Country Name"] == country_name:
                for y, col in zip(YEARS, YEAR_COLS):
                    val = row.get(col, "")
                    if val not in ("", ".."):
                        years.append(y)
                        values.append(float(val))
                break

    return years, values


country1 = "Ukraine"
country2 = "United States"

years1, data1 = read_country_data(country1)
years2, data2 = read_country_data(country2)

plt.figure(figsize=(8, 5))

plt.plot(years1, data1, label=country1, color="purple", linewidth=2)
plt.plot(years2, data2, label=country2, color="orange", linewidth=2)

plt.title("Out-of-school children, primary", fontsize=15)
plt.xlabel("Year", fontsize=12, color="red")
plt.ylabel("Children", fontsize=12, color="red")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


country_bar = input("Введіть назву країни для діаграми: ")

years_b, data_b = read_country_data(country_bar)

if years_b:
    x = np.arange(len(years_b))

    plt.figure(figsize=(8, 5))
    plt.bar(x, data_b, color="green")

    plt.xticks(x, years_b, rotation=45)
    plt.title(f"Out-of-school children: {country_bar}", fontsize=15)
    plt.xlabel("Year", fontsize=12, color="red")
    plt.ylabel("Children", fontsize=12, color="red")

    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()
else:
    print("Дані для цієї країни відсутні або назва введена неправильно.")