import pytest
import pandas as pd
from solucion import load_inegi_escolar

FILE = "00-raw-data/inegi-educacion/data.json"

def test_escolar_is_dataframe():
    df_escolar = load_inegi_escolar(FILE)
    assert isinstance(df_escolar, pd.DataFrame), "load_inegi_escolar debe retornar un DataFrame"

def test_escolar_not_empty():
    df_escolar = load_inegi_escolar(FILE)
    assert not df_escolar.empty, "El DataFrame escolar no debe estar vacío"

def test_escolar_has_correct_columns_shape():
    df_escolar = load_inegi_escolar(FILE)
    assert df_escolar.shape[1] == 4, "El DataFrame escolar debe tener 4 columnas (indicadores)"
