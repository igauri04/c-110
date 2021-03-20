import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import panadas as pd 
import csv

df = pd.read_csv("studentMarks.csv")
data = df["math_score"].tolist()


fig = ff.create_distplot([data],["math scores"],show_hist = False)
fig.show()