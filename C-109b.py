import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
heightList = df["Height(Inches)"].to_list()
weightList = df["Weight(Pounds)"].to_list()

hmean = statistics.mean(heightList)
wmean = statistics.mean(weightList)

hmedian = statistics.median(heightList)
wmedian = statistics.median(weightList)

hmode = statistics.mode(heightList)
wmode = statistics.mode(weightList)

hstdev = statistics.stdev(heightList)
wstdev = statistics.stdev(weightList)

print("mean,median,mode,stdev of Height is {},{},{},{} respectively" .format(hmean,hmedian,hmode,hstdev))
print("mean,median,mode,stdev of Weight is {},{},{},{} respectively" .format(wmean,wmedian,wmode,wstdev))

hfirststdevstart,hfirststdevend = hmean - hstdev,hmean + hstdev
wfirststdevstart,wfirststdevend = wmean - wstdev,wmean + wstdev

hsecondstdevstart,hsecondstdevend = hmean - (2*hstdev),hmean + (2*hstdev)
wsecondstdevstart,wsecondstdevend = wmean - (2*wstdev),wmean + (2*wstdev)

hthirdstdevstart,hthirdstdevend = hmean - (3*hstdev),hmean + (3*hstdev)
wthirdstdevstart,wthirdstdevend = wmean - (3*wstdev),wmean + (3*wstdev)

hdatafirststdev = [result for result in heightList if result > hfirststdevstart and result < hfirststdevend]
wdatafirststdev = [result for result in weightList if result > wfirststdevstart and result < wfirststdevend]

hdatasecondstdev = [result for result in heightList if result > hsecondstdevstart and result < hsecondstdevend]
wdatasecondstdev = [result for result in weightList if result > wsecondstdevstart and result < wsecondstdevend]

hdatathirdstdev = [result for result in heightList if result > hthirdstdevstart and result < hthirdstdevend]
wdatathirdstdev = [result for result in weightList if result > wthirdstdevstart and result < wthirdstdevend]

print("{}% data for height lies within firststdev".format(len(hdatafirststdev)*100.0/len(heightList)))
print("{}% data for height lies within secondstdev".format(len(hdatasecondstdev)*100.0/len(heightList)))
print("{}% data for height lies within thirdstdev".format(len(hdatathirdstdev)*100.0/len(heightList)))

print("{}% data for weight lies within firststdev".format(len(wdatafirststdev)*100.0/len(weightList)))
print("{}% data for weight lies within secondstdev".format(len(wdatasecondstdev)*100.0/len(weightList)))
print("{}% data for weight lies within thirdstdev".format(len(wdatathirdstdev)*100.0/len(weightList)))






