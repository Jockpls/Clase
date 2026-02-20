"""Extrae todos los hashtags."""
import re

texto = "Hoy hablamos de #Python y #MachineLearning en clase"

print(re.findall("#[A-Za-záéíóú]+", texto))
