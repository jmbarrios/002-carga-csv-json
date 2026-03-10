import pytest
import pandas as pd
from solucion import load_inegi_anual

FILE = "00-raw-data/inegi-educacion/data.json"

def test_anual_is_dataframe():
    df_anual = load_inegi_anual(FILE)
    assert isinstance(df_anual, pd.DataFrame), "load_inegi_anual debe retornar un DataFrame"

def test_anual_not_empty():
    df_anual = load_inegi_anual(FILE)
    assert not df_anual.empty, "El DataFrame anual no debe estar vacío"

def test_anual_has_correct_columns_shape():
    df_anual = load_inegi_anual(FILE)
    assert df_anual.shape[1] == 2, "El DataFrame anual debe tener 2 columnas (indicadores)"
