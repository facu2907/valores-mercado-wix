import json
from datetime import date

valores = {
  "novillos_gordos": 2.11,
  "vacas_gordas": 1.80,
  "vaquillonas_gordas": 2.10,
  "novillos": 2.49,
  "novillo_faena": 4.65,
  "vaca": 2.16,
  "vaca_faena": 4.36,
  "vaquillona": 2.38,
  "vaquillona_faena": 4.51,
  "carne_bovina": 4.65,
  "soja": 356,
  "trigo": 275,
  "maiz": 240,
  "sorgo": 235,
  "cebada": 250,
  "colza": 395,
  "carinata": 405,
  "fecha_actualizacion": date.today().isoformat()
}

with open("valores.json", "w") as f:
    json.dump(valores, f, indent=2)

