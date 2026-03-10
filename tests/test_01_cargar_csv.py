import pytest
import pandas as pd
from solucion import load_worldbank

FILE = "00-raw-data/worldbank-indicadores_desarrollo/9e447903-75a5-4bd0-8ac2-93767606ebde_Series - Metadata.txt"

def test_csv_is_dataframe():
    df = load_worldbank(FILE)
    assert isinstance(df, pd.DataFrame), "El resultado debe ser un DataFrame de pandas"

def test_csv_not_empty():
    df = load_worldbank(FILE)
    assert not df.empty, "El DataFrame no debe estar vacío"

def test_csv_has_rows():
    df = load_worldbank(FILE)
    assert df.shape[0] > 0, "El DataFrame debe tener filas"

def test_csv_has_columns():
    df = load_worldbank(FILE)
    assert df.shape[1] > 0, "El DataFrame debe tener columnas"
