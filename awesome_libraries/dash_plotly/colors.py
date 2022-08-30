from turtle import color
import plotly.express as px


data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop', color_discrete_sequence =[px.colors.sequential.speed[5]]*len(data_canada))
fig.show()


