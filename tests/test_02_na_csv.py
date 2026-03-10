import pytest
import pandas as pd
from solucion import load_worldbank

FILE = "00-raw-data/worldbank-indicadores_desarrollo/9e447903-75a5-4bd0-8ac2-93767606ebde_Series - Metadata.txt"

def test_csv_no_literal_dots():
    df = load_worldbank(FILE)
    has_dots = (df == '..').any().any()
    assert not has_dots, "Se encontraron valores '..' literales. Deben ser reemplazados por NA (nulos)."

def test_csv_has_na_values():
    df = load_worldbank(FILE)
    has_na = df.isna().any().any()
    assert has_na, "No se encontraron valores nulos (NA) en el DataFrame, asegúrate de procesar '..' correctamente."
