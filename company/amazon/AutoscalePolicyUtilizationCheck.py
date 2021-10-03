import math
'''
A scaling computing system checks its average utilization every second
while it monitors. It implements an autoscale policy to increase 
or reduce instances depending on the current load as described below.
Once an action of increasing or reducing the number of instances is performed,
the system will stop monitoring for 10 seconds. During that time, the 
number of instances don't change

- If average utilization < 25%, then an action is instantiated to reduce
the number of instances by half if the number of instances is greater than 1.
Take the ceiling if the number isn't an integer. If the number of instances 
is 1, take no action.

- If 25% average utilization is 60%, taken no action
- If average utilization > 60%, then an action is instantiated to 
double the number of instances if the doubled value doesn't exceed
2 * 108.

Given an array of integers that represent the average utilization at
each second, determine the number of instances at the end of the time frame
'''

def finalInstances(instances, averageUtil):
    for i in range(len(averageUtil)):
        if averageUtil[i] < 25:
            if instances > 1:
                instances = math.ceil(instances / 2)
            i += 10
            if i > len(averageUtil): break
        if averageUtil[i] > 60:
            if instances <= 216:
                instances *= 2
                i += 10
                if i > len(averageUtil): break
    return instances
