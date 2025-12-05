# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 16:07:51 2025

@author: Camilo Alarcon
"""

import pandas as pd
import os # 👈 Necesitas el módulo 'os' para manejar rutas y crear carpetas

# =======================================================================
# 📌 CONFIGURACIÓN DE RUTAS 
# =======================================================================

# --- RUTA DE ENTRADA ---
# Ruta completa al archivo Excel de origen (incluyendo el nombre del archivo).
# EJEMPLO: "C:\Users\Camilo Alarcon\Desktop\Proyecto Analisis\ReportHistory.xlsx"
INPUT_FILE_PATH = r"C:\Users\Camilo Alarcon\Desktop\Analisis\Analisis Trading\data_raw\ReportHistory-500288728.xlsx"

# --- RUTA DE SALIDA ---
# Ruta de la carpeta donde se guardarán los archivos Excel procesados (Posiciones.xlsx, etc.).
# Si la carpeta no existe, el script la creará.
# EJEMPLO: r"C:\Users\Camilo Alarcon\Desktop\Proyecto Analisis\Salida Tablas Procesadas"
OUTPUT_DIR = r"C:\Users\Camilo Alarcon\Desktop\Analisis\Analisis Trading\data_clean" 

# =======================================================================

# 1. Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)
print(f"Carpeta de salida: '{OUTPUT_DIR}'")

# Cargar el archivo sin encabezados desde la ruta de entrada
try:
    df = pd.read_excel(INPUT_FILE_PATH, header=None)
except FileNotFoundError:
    print(f"ERROR: Archivo no encontrado en la ruta: {INPUT_FILE_PATH}")
    exit()

# Títulos que identifican cada tabla
titles = ["Posiciones", "Órdenes", "Transacciones"]

# Diccionario para guardar posiciones de inicio
indexes = {}

# Buscar fila donde aparece cada título
for title in titles:
    row = df[df.apply(lambda row: row.astype(str).str.contains(title, case=False)).any(axis=1)].index
    if len(row) > 0:
        indexes[title] = row[0]

# Ordenar en el orden en que aparecen
sorted_titles = sorted(indexes, key=lambda k: indexes[k])

# Procesar las tablas
for i, title in enumerate(sorted_titles):

    # Fila donde empieza el encabezado real
    start = indexes[title] + 1

    # Determinar el fin del bloque
    if i < len(sorted_titles) - 1:
        # Fin = fila anterior al siguiente título
        end = indexes[sorted_titles[i+1]]
    else:
        # Última tabla llega hasta el final REAL del documento
        end = len(df)

    # EXTRA: ampliar rango hacia atrás por si hay filas vacías antes del título
    raw_table = df.iloc[start:end].copy()

    # Eliminar filas totalmente vacías
    raw_table = raw_table.dropna(how="all")

    # Asegurar que existe al menos una fila (encabezado)
    # Nota: Aquí asumo que la primera fila no vacía es el encabezado.
    if len(raw_table) > 0:
        raw_table.columns = raw_table.iloc[0]
        table = raw_table[1:].reset_index(drop=True)
    else:
        print(f"Advertencia: La tabla '{title}' está vacía. Saltando.")
        continue


    # Guardar archivo individual
    safe_title = title.replace("ó", "o").replace("Ó", "O")
    
    # 🎯 CREAR LA RUTA COMPLETA DE SALIDA (Carpeta + Nombre del archivo)
    filename = f"{safe_title}.xlsx"
    OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIR, filename)

    table.to_excel(OUTPUT_FILE_PATH, index=False)
    print(f"Archivo creado: {filename} (Filas: {len(table)})")