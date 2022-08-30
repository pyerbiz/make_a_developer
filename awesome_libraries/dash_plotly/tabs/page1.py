from dash import html, dbc, dcc, Input, Output
import plotly.express as px
import pandas as pd
from app import app


dfv = pd.read_csv(r"C:\Users\saral\OneDrive\Desktop\projects\repos\make_a_developer\awesome_libraries\dash_plotly\multipage_app\datasets\vgsales.csv")

genre_list = ['Sports', 'Shooter', 'Action', 'Role-Playing', 'Platform',
       'Fighting', 'Misc', 'Racing', 'Adventure', 'Strategy',
       'Simulation', 'Puzzle']