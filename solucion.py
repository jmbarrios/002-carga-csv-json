import json
import pandas as pd

def load_inegi_anual(data_file: str) -> pd.DataFrame:
    pass

def load_inegi_escolar(data_file: str) -> pd.DataFrame:
    pass
    

def load_worldbank(data_file: str) -> pd.DataFrame:
    pass

if __name__ == "__main__":

    INEGI_FILE = "00-raw-data/inegi-educacion/data.json"
    WORLDBANK_FILE = "00-raw-data/worldbank-indicadores_desarrollo/9e447903-75a5-4bd0-8ac2-93767606ebde_Series - Metadata.txt"

    inegi_escolar_data: pd.DataFrame = load_inegi_escolar(INEGI_FILE)
    inegi_anual_data: pd.DataFrame = load_inegi_anual(INEGI_FILE)

    worldbank_data: pd.DataFrame = load_worldbank(WORLDBANK_FILE)

    print(f"Uso de memoria del dataset Inegi Anual:\n {inegi_escolar_data.memory_usage(deep=True)}")
    print(f"Uso de memoria del dataset Inegi Escolar:\n {inegi_anual_data.memory_usage(deep=True)}")
    print(f"Uso de memoria del dataset WorldBank:\n {worldbank_data.memory_usage(deep=True)}")