import pytest
import pandas as pd
from solucion import load_inegi_escolar

FILE = "00-raw-data/inegi-educacion/data.json"

def test_escolar_column_types_are_numeric():
    df_escolar = load_inegi_escolar(FILE)
    for col in df_escolar.columns:
        assert pd.api.types.is_numeric_dtype(df_escolar[col]), f"La columna '{col}' del DataFrame escolar debe ser numérica."
