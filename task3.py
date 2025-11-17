import json
import matplotlib.pyplot as plt

with open("employees.json", "r", encoding="utf-8") as f:
    employees = json.load(f)

positions_count = {}
for emp in employees:
    pos = emp["Position"]
    positions_count[pos] = positions_count.get(pos, 0) + 1

labels = list(positions_count.keys())
sizes = list(positions_count.values())

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        absolute = int(round(pct * total / 100.0))
        return f"{pct:.1f}% ({absolute} ос.)"
    return my_autopct

wedges, texts, autotexts = ax.pie(
    sizes,
    autopct=make_autopct(sizes),
    startangle=90
)

ax.legend(
    wedges, labels,
    title="Посади",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

ax.set_title("Розподіл співробітників за посадами")

plt.show()