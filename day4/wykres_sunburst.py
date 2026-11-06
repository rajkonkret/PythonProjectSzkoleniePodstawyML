import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "region": ["Polska", "Polska", "Niemcy", "Niemcy", "Czechy"],
    "kategoria": ["Laptopy", "Telefony", "Laptopy",
                  "Telefony", "Laptopy"],
    "sprzedaz": [120000, 85000, 160000, 95000, 70000]
})

# fig = px.sunburst(
#     df,
#     path=["region", "kategoria"],
#     values="sprzedaz",
#     color="sprzedaz",
#     color_continuous_scale="Viridis",
#     title="Struktura sprzedaży"
# )
#
# fig.show()

df["produkt"] = [
    "MacBook",
    "iPhone",
    "ThinkPad",
    "Samsung",
    "Dell"
]

fig = px.sunburst(
    df,
    path=["region", "kategoria", "produkt"],
    values="sprzedaz",
    color="sprzedaz",
    color_continuous_scale="Viridis"
    # color_continuous_scale="GnBu"
)

fig.show()
