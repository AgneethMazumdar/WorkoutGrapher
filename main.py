# Created by Agneeth Mazumdar
# Released under the MIT License 

import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np

import itertools
import csv
import string

class Exercises(object):

    def __init__(self, name, weight, sets, reps):
        self.name = name
        self.weight = weight
        self.sets = sets
        self.reps = reps

def get_names():

    # We have this function so that we don't need to know the number of exercises beforehand

    with open('WorkoutData.csv', 'rb') as workout_data: 
        csv_workout_data = csv.reader(workout_data)

        names = [] 

        for index, row in enumerate(csv_workout_data):

            if index < 1:
                names.append(row)

    names = list(itertools.chain(*names))
    names = names[1:],
    names = list(itertools.chain(*names))

    return names 

def get_dates_and_wsr(counter, wsr_cont):

    loop_counter = counter
    wsr = wsr_cont
    
    with open('WorkoutData.csv', 'rb') as workout_data:
        csv_workout_data = csv.reader(workout_data)

        dates = [] 

        for index, row in enumerate(csv_workout_data):

            dates.append(row[0])
            wsr.append(row[loop_counter]) # For the loop in main

        nested_wsr = [wsr[index:index+len(dates)] for index in xrange(0, len(wsr), len(dates))]

    # We're filtering out the names from wsr and turning it into a nested list 

    for sublist in nested_wsr:
        del sublist[0]

    dates = dates[1:]

    # This is where we'll filter the workout data

    for e_index, value in enumerate(nested_wsr): # triple nested list... exercise --> workout --> wsr

        for w_index, value_2 in enumerate(dates):

            if nested_wsr[e_index][w_index] == '':
                nested_wsr[e_index][w_index] = '0 0x0'
        
            nested_wsr[e_index][w_index] = string.replace(nested_wsr[e_index][w_index], ' ', 'x')
            nested_wsr[e_index][w_index] = nested_wsr[e_index][w_index].split('x')

    return dates, nested_wsr

def get_graphing_parameters():
    
    exercise = raw_input('What exercise do you want to graph? \n')
    min_sets = raw_input('What are the minimum number of sets to graph? \n')
    rep_range = raw_input('What minimum rep range do you want to graph? \n')

    return exercise, min_sets, rep_range

def main():

    wsr, weight, sets, reps, = [], [], [], []

    name_index = get_names()

    for index in range(1, len(name_index)+1):
        dates, nested_wsr = get_dates_and_wsr(index, wsr) 

    # Sorting the weights, sets, and reps into their respective exercise

    for e_index, value in enumerate(nested_wsr):
        for w_index, value in enumerate(dates):

            weight.append(nested_wsr[e_index][w_index][0])
            sets.append(nested_wsr[e_index][w_index][1])
            reps.append(nested_wsr[e_index][w_index][2])

        weight = [int(index) for index in weight]
        sets = [int(index) for index in sets]
        reps = [int(index) for index in reps]

        name_index[e_index] = Exercises(name_index[e_index], weight, sets, reps)

        weight, sets, reps = [], [], []

    # Prompt user to choose what exercise to graph and the minimum sets and reps

    exercise, min_sets, rep_range = get_graphing_parameters()

    for index, value in enumerate(nested_wsr):
        if exercise == name_index[index].name:
            exercise = index

    min_sets = int(min_sets)
    rep_range = int(rep_range)

    # Sorting out what to graph based on user input

    temporary_dates, temporary_weights = [], []

    for index in range(len(dates)):
        if name_index[exercise].sets[index] > min_sets-1 and name_index[exercise].reps[index] > rep_range-1:
            temporary_dates.append(dates[index])
            temporary_weights.append(name_index[exercise].weight[index])

    for index, value in enumerate(temporary_weights):
        if value == 0:
            del temporary_dates[index]
            del temporary_weights[index]

    # Time to start graphing everything

    temporary_dates = [dt.datetime.strptime(index,'%m/%d/%Y').date() for index in temporary_dates]

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))

    plt.plot(temporary_dates, temporary_weights)
    plt.gcf().autofmt_xdate()

    plt.xlabel('Time')
    plt.ylabel('Weight (lbs)')
    plt.title(name_index[exercise].name) 

    plt.show()

if __name__ == "__main__":
    main()
