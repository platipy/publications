# Representing the Teacher's assessment 

from __future__ import with_statement
import numpy as np
import matplotlib.pyplot as plt
import csv

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


y_ticklabels = {'Evaluation' : 'Very Poorly,Poorly,Fairly,Well,Very Well'.split(','),
                'Fun': 'Very Boring,Boring,Neutral,Fun,Very Fun'.split(','),
                'Teaching': 'Very Poorly,Poorly,Fairly,Well,Very Well'.split(','),
                'Usefulness': 'Very Useless,Useless,Neutral,Useful,Very Useful'.split(','),
                'Average Reaction': ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']}
items = y_ticklabels.keys()

# Generate individual graphs
for item in items:
    games, scores= zip(*evaluations[item])

    x_label_arrangement = np.arange(len(scores))  # the x locations for the groups
    y_label_arrangement = np.arange(len(y_ticklabels[item]))  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig = plt.figure()
    plt.axvline()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.3, left=0.20)
    rects1 = ax.bar(x_label_arrangement+width/2., scores, width, color=['r','r', 'r', 'b','b','b'])

    # add some
    ax.set_title('Assesment of %s by Game' % (item,))
    ax.set_xlabel('Games')
    ax.set_xticks(x_label_arrangement+width)
    ax.set_xticklabels( games, rotation='vertical' )
    ax.set_ylabel('Evaluation')
    ax.set_yticks(y_label_arrangement)
    ax.set_yticklabels( y_ticklabels[item] )
    

    #ax.legend( (rects1[0], ), ('Men', ) )

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, height,
                    ha='center', va='bottom')

    #autolabel(rects1)

    plt.savefig('teacher_%s.png' % (item,))