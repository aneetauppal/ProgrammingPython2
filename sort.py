#!/usr/bin/python

dataList = [-5, -6, 7, 9, -30, 2, 30]
newList = []


def sorting(dataList):
    while dataList:
        minimum = dataList[0]
        for x in dataList:
            if x < minimum:
                minimum = x
        newList.append(minimum)
        dataList.remove(minimum)
    return newList

List = sorting(dataList)
print List
