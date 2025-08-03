import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

st.set_page_config(layout="wide")
st.markdown('<h1 style="color:#F47900;">OUTPUT STOFFSTROM</h1>', unsafe_allow_html=True)

df = pd.read_csv("STAT_OUTPUT_SS.csv")
df["AF_DATUM"] = pd.to_datetime(df["AF_DATUM"], dayfirst=True).dt.strftime("%d.%m.%Y")
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(
    filter=True,
    sortable=True,
    resizable=True,
    auto_size=True,           # let columns report their ideal width
)

# Define custom CSS for header
custom_css = {
    ".custom-header": {
        "background-color": "#F47900",
        "color": "white",
        "font-weight": "bold",
        "text-align": "center",
    }
}

# Configure AgGrid
gb = GridOptionsBuilder.from_dataframe(df)
# apply `custom-header` class to every column's header
for col in df.columns:
    gb.configure_column(col, headerClass="custom-header")
gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=20)
german_locale = {
    "page": "Seite",
    "more": "mehr",
    "to": "bis",
    "of": "von",
    "next": "Nächste",
    "last": "Letzte",
    "first": "Erste",
    "previous": "Vorherige",
    "loadingOoo": "Lade...",
    "selectAll": "Alle auswählen",
    "searchOoo": "Suchen...",
    "blanks": "Leer",
    "filterOoo": "Filter...",
    "applyFilter": "Filter anwenden",
    "equals": "Gleich",
    "notEqual": "Ungleich",
    "contains": "Enthält",
    "notContains": "Enthält nicht",
    "startsWith": "Beginnt mit",
    "endsWith": "Endet mit",
    "andCondition": "UND",
    "orCondition": "ODER",
    "noRowsToShow": "Keine Zeilen verfügbar",
    "copy": "Kopieren",
    "copyWithHeaders": "Mit Überschriften kopieren",
    "ctrlC": "Strg+C",
    "paste": "Einfügen",
    "ctrlV": "Strg+V",
    "export": "Exportieren",
    "columns": "Spalten",
    "filters": "Filter",
    "rowGroupColumnsEmptyMessage": "Ziehen Sie hier, um nach dieser Spalte zu gruppieren"
}

gb.configure_grid_options(localeText=german_locale)
opts = gb.build()

AgGrid(
    df,
    gridOptions=opts,
    allow_unsafe_jscode=True,     # needed for our onGridReady
    enable_enterprise_modules=False,custom_css=custom_css,
    theme="material",
    height=500,
)
