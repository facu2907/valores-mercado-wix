import json
from datetime import date

valores = {
  "novillos_gordos": 2.11,
  "vacas_gordas": 1.80,
  "vaquillonas_gordas": 2.10,
  "novillos": 2.63,
  "novillo_faena": 4.95,
  "vaca": 2.31,
  "vaca_faena": 4.72,
  "vaquillona": 2.55,
  "vaquillona_faena": 4.86,
  "carne_bovina": 5.017,
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

