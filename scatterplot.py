import pandas as pd
import plotly.express as px

df = pd.read_csv("COVID-19_data.csv")
fig = px.scatter(df,title="#COVID-19 cases", x="Date", y="Cases",
	          color="Country",
                   size_max=60)
fig.show()
