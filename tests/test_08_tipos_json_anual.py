import pytest
import pandas as pd
from solucion import load_inegi_anual

FILE = "00-raw-data/inegi-educacion/data.json"

def test_anual_column_types_are_numeric():
    df_anual = load_inegi_anual(FILE)
    for col in df_anual.columns:
        assert pd.api.types.is_numeric_dtype(df_anual[col]), f"La columna '{col}' del DataFrame anual debe ser numérica."
