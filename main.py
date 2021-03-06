# Created by Agneeth Mazumdar
# Released under the MIT License

import csv
import string

import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np


class Exercises(object):


    def __init__(self, name):
        self.name = name
        self.weights = []
        self.sets = []
        self.reps = []

    def addWeight(self, weight):
        self.weights.append(weight)

    def addSets(self, eset):
        self.sets.append(eset)

    def addReps(self, reps):
        self.reps.append(reps)

"""
Create a list of exercises, dates, and exercise objects. Reading the data from
the csv file and making it searchable will require reformatting the data into
its individuals components later on (weight, sets, reps, and dates).
"""

def create_exercise_objects():

    exercises, dates = [], []

    with open('WorkoutData.csv', 'rb') as workout_data:
        csv_workout_data = csv.reader(workout_data)

        for index, row in enumerate(csv_workout_data):

            dates.append(row[0])

            if index == 0:
                exercise_names = row[1:]

        dates = dates[1:]

        for index, value in enumerate(exercise_names):
            exercises.append(Exercises(exercise_names[index]))

    return exercises, exercise_names, dates

"""
Bind the column of workouts with their respective exercises.
"""

def make_wsr_dictionary(counter, names):

    catalog = {}

    with open('WorkoutData.csv', 'rb') as workout_data:
        csv_workout_data = csv.reader(workout_data)

        try:
            temp = [row[counter+1] for index, row in enumerate(csv_workout_data)]
            catalog[names[counter]] = temp[1:]
            temp = []

        except:
            pass

    return catalog

"""
Parse the individual cells and get rid of the spaces so that it's easier
to separate the weight, sets, and reps. Also make sure that empty cells
will not cause runtime errors by filling them in with zeros.
"""

def start_filtering(full_catalog):

    for key, value in full_catalog.iteritems():
        for index, element in enumerate(value):

            value[index] = string.replace(value[index], ' ', 'x')
            value[index] = value[index].split('x')

            if len(value[index]) < 3:
                value[index] = [0, 0, 0]

    return full_catalog

"""
Add the weight, sets, and reps attributes to its respective exercise attribute.
"""

def append_attributes(exercises, full_catalog, names):

    for index, value in enumerate(names):
        full_catalog[names[index]] = map(list, zip(*full_catalog[names[index]]))
        weights_sets_reps = full_catalog[names[index]]

        exercises[index].addWeight(map(int, weights_sets_reps[0]))
        exercises[index].addSets(map(int, weights_sets_reps[1]))
        exercises[index].addReps(map(int, weights_sets_reps[2]))

    return exercises

"""
Ask the user to input the exercise, and set and rep scheme.
"""

def get_graphing_parameters():

    exercise = raw_input('What exercise do you want to graph? \n')
    min_sets = raw_input('What are the minimum number of sets to graph? \n')
    rep_range = raw_input('What minimum rep range do you want to graph? \n')

    return exercise, int(min_sets), int(rep_range)

"""
Graph the user's progress.
"""

def graph_progress(temporary_dates, temporary_weights, names, place_holder):

    temporary_dates = [dt.datetime.strptime(index,'%m/%d/%Y').date() for index in temporary_dates]

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))

    plt.plot(temporary_dates, temporary_weights)
    plt.gcf().autofmt_xdate()

    plt.xlabel('Time')
    plt.ylabel('Weight (lbs)')
    plt.title(names[place_holder])

    plt.show()

def main():

    temporary_dates, temporary_weights, full_catalog = [], [], {}
    place_holder = None

    exercises, names, dates = create_exercise_objects()

    for index, value in enumerate(exercises):
        full_catalog.update(make_wsr_dictionary(index, names))

    full_catalog = start_filtering(full_catalog)
    exercises = append_attributes(exercises, full_catalog, names)

    exercise, min_sets, rep_range = get_graphing_parameters()

    for name_index, value in enumerate(names):
        if value == exercise:
            place_holder = name_index

    for index, value in enumerate(dates):
        if exercises[place_holder].sets[0][index] >= min_sets:
            if exercises[place_holder].reps[0][index] >= rep_range:
                temporary_dates.append(dates[index])
                temporary_weights.append(exercises[place_holder].weights[0][index])

    for index, value in enumerate(temporary_weights):
        if value == 0:
            del temporary_dates[index]
            del temporary_weights[index]

    graph_progress(temporary_dates, temporary_weights, names, place_holder)

if __name__ == "__main__":
    main()
