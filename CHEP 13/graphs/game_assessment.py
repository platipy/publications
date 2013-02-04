# Representing the Teacher's assessment 

from __future__ import with_statement
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv

# Adjust font size
matplotlib.rcParams.update({'font.size': 30})

evaluations = {}
with open('teacher_data.csv', 'rb') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        item, game, average = row[:3]
        #scores = row[3:]
        if item in evaluations:
            evaluations[item].append((game, float(average)-1))
        else:
            evaluations[item] = [(game, float(average)-1)]


y_ticklabels = ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']
items = ['Evaluation', 'Teaching', 'Fun', 'Usefulness', 'Average Reaction']

x_label_arrangement = np.arange(len(items)*6)  # the x locations for the groups
x_single_arrangement = np.arange(6)
y_label_arrangement = np.arange(len(y_ticklabels))  # the x locations for the groups
width = 0.66       # the width of the bars

# Adjust plot size
fig = plt.figure(figsize=(30,13))
plt.axvline(15, linestyle='--')
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.3, left=0.30)
rects = []
colors = ['r','g','b','y','m']
for index, item in enumerate(items):
    games, scores = zip(*evaluations[item])
    rects.append(ax.bar(x_single_arrangement*len(items)+(index+width+.5)*width, scores, width, color=colors[index]))

ax.set_title('Assesment of Reaction by Game')
ax.set_xlabel('Games')
ax.set_xticks(x_single_arrangement*len(items)+width*3)
ax.set_xticklabels( games, rotation='vertical' )
ax.set_ylabel('Reaction')
ax.set_yticks(y_label_arrangement)
ax.set_yticklabels( y_ticklabels )

# Adjust Legend size
ax.legend( rects, items, loc= 'lower right', title='Areas', prop={'size':25})

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, height,
                ha='center', va='bottom')

#autolabel(rects1)

plt.savefig('teacher_games.png')