import pytest
import pandas as pd
from solucion import load_inegi_escolar

FILE = "00-raw-data/inegi-educacion/data.json"

def test_escolar_index_is_int():
    df_escolar = load_inegi_escolar(FILE)
    assert pd.api.types.is_integer_dtype(df_escolar.index), "El índice del DataFrame escolar debe ser de tipo entero (int)"
