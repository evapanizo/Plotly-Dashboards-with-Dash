#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

# create a DataFrame from the .csv file:
df = pd.read_csv("./Data/iris.csv")
print(df.head())

# Define a data variable
group_labels = [unique_class for unique_class in df["class"].unique()]
hist_data = [df[df['class'] == flower_class]['petal_length'] for flower_class in group_labels]

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels)
fig.layout.update({'title': 'Distplot of petal lenghts of each flower class'})
pyo.plot(fig, filename='./1-08E-DistplotExercises/my_solution.html')