import datetime
import csv

today = datetime.date.today().strftime("%Y-%m-%d")

filename = "journal.csv"

# Ajoute une ligne si elle n'existe pas déjà pour aujourd'hui
rows = []
try:
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
except FileNotFoundError:
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Activité", "Temps (min)", "XP", "Statut"])

if not any(row and row[0] == today for row in rows):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([today, "Entrée automatique", "0", "0", "🕓"])

print("✅ Journal mis à jour :", today)
