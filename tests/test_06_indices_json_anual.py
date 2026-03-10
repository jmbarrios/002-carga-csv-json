import pytest
import pandas as pd
from solucion import load_inegi_anual

FILE = "00-raw-data/inegi-educacion/data.json"

def test_anual_index_is_int():
    df_anual = load_inegi_anual(FILE)
    assert pd.api.types.is_integer_dtype(df_anual.index), "El índice del DataFrame anual debe ser de tipo entero (int)"
