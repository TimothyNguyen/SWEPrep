'''
Given a list of points, find the nearest points that shares either an x or a y coordinate with the queried point.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y.

Input

numOfPoints, an integer representing the number of points;

points, a list of strings representing the names of each point [i];

xCoordinates, a list of integers representing the X coordinates of each point[i];

yCoordinates, a list of integers representing the Y coordinates of each point[i];

numOfQueriedPoints, an integer representing the number of points queried;

queriedPoints, a list of strings representing the names of the queried points.

Output

Return a list of strings representing the name of the nearest points that shares either an x or a y coordinate with the queried point.

Example 1:

Input:

numOfPoints = 3

points = ["p1","p2","p3"]

xCoordinates = [30, 20, 10]

yCoordinates = [30, 20, 30]

numOfQueriedPoints = 3

queriedPoints = ["p3", "p2", "p1"]

Output:

["p1", NONE, "p3"]

Example 2:

Input:

numOfPoints = 5

points = ["p1", "p2","p3", "p4", "p5"]

xCoordinates = [10, 20, 30, 40, 50]

yCoordinates = [10, 20, 30, 40, 50]

numOfQueriedPoints = 5

queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

Output

[NONE, NONE, NONE, NONE, NONE]
'''
def nearestCities(numOfPoints, points, xCoordinates, yCoordinates, numOfQueriedPoints, queriedPoints):
    store = collections.defaultdict(list)
    for index, i in enumerate(points):
        store[i].append(xCoordinates[index])
        store[i].append(yCoordinates[index])
    print(store)
    res = []
    for i in queriedPoints:
        queried_points_store = store[i]
        for key, values in store.items():
            if key == i:
                res.append(None)
                continue
            if set(queried_points_store) & set(values):
                res.append(key)
                break
    return list(set(res))