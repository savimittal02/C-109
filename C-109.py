import random
import statistics
import plotly.express as px
import plotly.figure_factory as ff

count = []
diceResult = []
for i in range(0,1000):

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1 + dice2)
    count.append(i)

mean = sum(diceResult)/len(diceResult)
stddev = statistics.stdev(diceResult)
median = statistics.median(diceResult)
mode = statistics.mode(diceResult)

print(mean)
print(median)
print(mode)
print(stddev)

fig = ff.create_distplot([diceResult],["result"])
fig.show()

