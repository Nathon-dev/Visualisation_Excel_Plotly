import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import os
import sys


import plotly.io as pio
pio.renderers.default='browser'



# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    Path = os.path.dirname(sys.executable)
elif __file__:
    Path = os.path.dirname(os.path.abspath(__file__))

print("Path is" + Path)



df=pd.read_csv(Path + '\Data.csv', sep = ',')

print(df)

figtot = go.Figure()

for x in range(1, len(df.columns)):
   figtot.add_trace(go.Scatter(x=df.iloc[:,0], y=df.iloc[:,x], name=df.columns[x],
                        line=dict(width=1)))
   print(df.columns[x])

figtot.update_layout(title='',
                  xaxis_title=df.columns[0],
                  yaxis_title='')

# Add dropdown
figtot.update_layout(
    updatemenus=[
        dict(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    args=["type", "lines"],
                    label="Courbes",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Barres",
                    method="restyle"
                ),
                dict(
                    args=["type", "pie"],
                    label="Camembert",
                    method="restyle"
                )




            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.11,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

# Add annotation
figtot.update_layout(
    annotations=[
        dict(text="Type de graphique :", showarrow=False,
                             x=0, y=1.08, yref="paper", align="left")
    ]
)

figtot.show()
