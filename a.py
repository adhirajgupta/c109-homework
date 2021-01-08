import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics
import csv
import math

with open('Students.csv',) as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

df = pd.read_csv("Students.csv")
dfData = df["reading score"].tolist()


def mean():
    add = 0
    for i in range(1,len(file_data)):
        num = int(file_data[i][6])
        add += num
        #print("Add = ",add)
    
    mean = add/len(file_data)
    print("Mean = ",mean)
    return mean

def medianmode():
    numbers = [[]]
    for i in range(1,len(file_data)):
        j = int(file_data[i][6])
        numbers[0].append(j)
        #print(numbers[0])
    median = statistics.median(numbers[0])
    print("Median = ",median)
    mode = statistics.mode(numbers[0])
    print("Mode = ",mode)
    return {"x":median,"y":mode,"z":numbers[0]}

def std_dev(mean,nums):
    squared_list = []
    total = 0
    for i in nums:
        a = int(i) - mean
        a = a**2
        squared_list.append(a)
        
    #print("squared_list ",squared_list)

    for i in squared_list:
        total += i
    
    #print("total = ",total)
    result = total/(len(nums)-1)
    #print("result = ",result)
    std_dev = math.sqrt(result)
    print("Std _ dev = ",std_dev)
    return std_dev

a = mean()
b = medianmode()
c = std_dev(a,b["z"])

first_std_start,first_std_end = a-c,a+c
print("first_std_start = ",first_std_start)
print("first_std_end = ",first_std_end)
second_std_start,second_std_end = a-(2*c),a+(2*c)
print("second_std_start = ",second_std_start)
print("second_std_end = ",second_std_end)
third_std_start,third_std_end = a-(3*c),a+(3*c)
print("third_std_start = ",third_std_start)
print("third_std_end = ",third_std_end)



fig = ff.create_distplot([dfData], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[a, a], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()


list_of_data_within_1_std_deviation = [
    result for result in dfData if result > first_std_start and result < first_std_end]
list_of_data_within_2_std_deviation = [
    result for result in dfData if result > second_std_start and result < second_std_end]
list_of_data_within_3_std_deviation = [
    result for result in dfData if result > third_std_start and result < third_std_end]



"""print("a = ",a)
print("b[X] = ",b["x"])
print("b[Y] = ",b["y"])
print("c = ",c)
"""






    






