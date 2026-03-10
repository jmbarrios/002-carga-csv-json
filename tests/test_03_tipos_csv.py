import pytest
import pandas as pd
from solucion import load_worldbank

FILE = "00-raw-data/worldbank-indicadores_desarrollo/9e447903-75a5-4bd0-8ac2-93767606ebde_Series - Metadata.txt"

def test_csv_no_object_types():
    df = load_worldbank(FILE)
    tiene_object = any(df.dtypes == 'object')
    assert not tiene_object, "No debe de haber ninguna columna de tipo 'object'. Cambia los tipos a categóricos, numéricos, etc."

def test_csv_memory_limit():
    df = load_worldbank(FILE)
    uso_memoria = df.memory_usage(deep=True).sum()
    limite = 20000
    assert uso_memoria < limite, f"El DataFrame usa demasiada memoria ({uso_memoria} bytes). El límite es {limite} bytes. Optimiza los tipos."
