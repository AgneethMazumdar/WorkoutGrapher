# Purpose

This script parses through the contents of a training spreedsheet (csv) and graphs the user’s progress given an input of a minimum set and rep scheme. This can be applicable in analyzing the training log of a powerlifter, weightlifter, or a general weight training enthusiast. 

# Requirements

* [Python 2.7](https://www.python.org/) 
* [NumPy] (http://www.numpy.org/)
* [matplotlib] (http://matplotlib.org/)
* [Seaborn] (http://stanford.edu/~mwaskom/software/seaborn/installing.html)

# CSV File Formatting

An example of a month's worth of test data. The script will ignore empty cells but improperly formatted cells will result in errors. If you wanted to read two separate rep and set schemes from a single cell that will result in error, so it's best to choose one that you would like to graph. 

|	| Squat |	Bench |	Deadlift 
|	--- | --- | --- | --- |
1/1/14 | |			
1/2/15 |	135 5x5 |	115 3x5 |	175 1x5
1/5/15 |	145 5x5	| 120 3x5	
1/7/15 |	155 3x5	| |	
1/9/15 |	165 3x5	| 125 3x5	| 185 1x5
1/12/15 |	175 2x5 |	130 3x5 |	
1/14/15	| 155 5x5	|	
1/16/15 |	130 3x5	| | 195 1x5 |
1/19/15	| 165 5x5	| 135 3x5	|
1/21/15	| 175 3x5	|	
1/23/15	| 185 3x5	| 140 3x5	| 205 1x5
1/26/15	| 190 3x5	| 145 3x5	|
1/28/15	| 195 3x5	|	
1/30/15	| 200 3x5	| 150 3x5	| 215 1x5

# Example Prompt and Input/Output 

```
What exercise do you want to graph?
Squat
What are the minimum number of sets to graph? 
0
What minimum rep range do you want to graph? 
0 
```

![alt text](http://i.imgur.com/5A6VaAy.png?1 "Progress Graph")
