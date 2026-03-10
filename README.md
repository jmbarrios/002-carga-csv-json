# 📊 Práctica: Carga de Archivos CSV y JSON en Pandas 🐼

¡Hola! En esta práctica, pondrás a prueba tus habilidades para extraer y preparar datos desde diferentes fuentes. Implementarás funciones para cargar información desde un archivo de texto tabular (CSV/TSV) y un archivo estructurado en JSON, utilizando la biblioteca `pandas`.

🎯 **Objetivo Principal:**
Cargar la información de forma correcta y optimizar el uso de memoria a través de una adecuada asignación de tipos de datos a las columnas. 

 Todo tu código debe ser escrito en el archivo `solucion.py`. Sólo puedes utilizar las bibliotecas nativas de Python y `pandas`. Se recomienda incluir *typing* en tus funciones.

---

## 🌎 Parte 1: Carga de indicadores del Banco Mundial (CSV)

### 📖 Contexto de los Datos
En los archivos de datos del banco mundial se encuentra información sobre indicadores de desarrollo de México. Estos corresponden a diferentes métricas de temas sociales, económicos, de salud y ambientales.

Los archivos fueron descargados desde el [DataBank](https://databank.worldbank.org/), la cual es una herramienta donde se pueden consultar miles de indicadores mundiales. Aquí se pueden generar conjuntos de datos personalizados para su análisis.

### 🛠️ Instrucciones
El primer paso consiste en cargar el archivo de texto plano separado por tabuladores (`\t`):
`00-raw-data/worldbank-indicadores_desarrollo/9e447903-75a5-4bd0-8ac2-93767606ebde_Series - Metadata.txt`

Implementa la función `load_worldbank(data_file: str) -> pd.DataFrame` en `solucion.py`.
Debes cumplir los siguientes requisitos:
1. Cargar el archivo en un DataFrame de pandas.
2. Identificar y definir los valores `..` como valores nulos (`NA`).
3. Asignar de manera correcta y óptima los tipos de datos a cada columna para minimizar el uso de memoria (`str`, `float`, `category`, etc.). 
4. **Importante**: No debe existir ninguna columna de tipo `object` al finalizar la carga.

---

## 🏫 Parte 2: Carga de Datos de Educación (JSON)

### 📖 Contexto de los Datos
El archivo de `00-raw-data/inegi-educacion/data.json` fue construído usando la API del [Banco de Indicadores del INEGI](https://www.inegi.org.mx/servicios/api_indicadores.html), esta es pública y puede comenzar a usarse después de hace un registro para recibir un token de uso. 

En este ejemplo se solicitó la información de 6 indicadores:

| ID indicador | Descripción |
| ----------- | ----------- |
| 6207067825 | Gasto nacional en educación total como porcentaje del PIB |
| 6000000001 | Tasa neta de matriculación en la enseñanza primaria (6 a 11 años de edad) |
| 6300000246 | Razón entre niñas y niños en la enseñanza primaria |
| 6300000229 | Razón entre niñas y niños en la enseñanza secundaria |
| 6300000235 | Razón entre mujeres y hombres en la enseñanza media superior |
| 6300000231 | Razón entre mujeres y hombres en la enseñanza superior | 

Los primeros dos indicadores se miden de forma anual, mientras que los últimos cuatro se miden por ciclo escolar.

### 🛠️ Instrucciones
La segunda parte consiste en cargar un conjunto de datos desde formato JSON:
`00-raw-data/inegi-educacion/data.json`

Este archivo contiene 6 series. Las dos primeras son de frecuencia anual y las últimas 4 corresponden a cada ciclo escolar.

Implementa dos funciones en `solucion.py`:
- `load_inegi_anual(data_file: str) -> pd.DataFrame`
- `load_inegi_escolar(data_file: str) -> pd.DataFrame`

**💡 Pista**: Los datos de las observaciones están en el atributo `Series` que es una lista cuyas entradas son diccionarios con la llave `OBSERVATIONS` y el nombre de cada indicador está en la llave `INDICADOR` de cada elemento del atributo `Series`.

Debes cumplir los siguientes requisitos para ambos DataFrames:
1. Extraer adecuadamente los valores de la estructura JSON.
2. El índice del DataFrame debe ser de tipo entero (`int`) correspondiente al año (`TIME_PERIOD`).
3. Las columnas deben corresponder a cada indicador, utilizando nombres informativos de acuerdo al identificador del indicador.
4. Asignar los tipos numéricos correctos para los valores extraídos.

---

## ✅ Evaluación

La evaluación se realizará mediante pruebas unitarias automáticas empleando `pytest`. Cada función que pases te sumará puntos para llegar a la calificación perfecta de **130 pts**. 🏆 

**📈 Manejo de CSV (World Bank):**
- **10 pts**: Cargar correctamente el archivo csv/txt.
- **10 pts**: Definir adecuadamente los valores `..` como `NA`.
- **20 pts**: Definir de manera correcta y optimizada los tipos de datos (y cumplir con el límite superior de uso de memoria en las pruebas).

**📉 Manejo de JSON (INEGI):**
- **20 pts** *(10 pts por df)*: Crear los DataFrames desde el archivo JSON de forma correcta.
- **30 pts** *(15 pts por df)*: Definir el índice del DataFrame como tipo `int`.
- **40 pts** *(20 pts por df)*: Asignar los tipos de datos correctos a las columnas en los DataFrames cargados desde el JSON.

¡Mucho éxito! 🚀
