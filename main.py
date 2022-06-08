import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random 
import csv
import statistics 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("Population mean : ",population_mean)
print("Std deviation : ",std_deviation)
def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

# function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()
#function to get mean 0f 100 data points 1000 times and plot the graph

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()
#for i in range(0,1000):
    #random_index = random.randint(0,len(data))
    #value = data[random_index]
    #data_set.append(value)
#mean = statistics.mean(data_set)
#std_deviation = statistics.stdev(data_set)
#print("Mean of sample : ", mean)
#print("Std deviation of sample : ", std_deviation)
#fig = ff.create_distplot([data], ["temp"], show_hist=False)
#fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0,1], mode="lines", name="mean"))
#fig.show()