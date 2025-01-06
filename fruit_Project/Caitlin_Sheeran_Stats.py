def Mean(lyst):
    return (sum(lyst)/len(lyst))


def Median( lyst):
    lyst.sort()
    if len(lyst) % 2 == 1:
        return lyst[len(lyst) // 2]
    else:
        mid1 = lyst[len(lyst) // 2]
        mid2 =  lyst[(len(lyst) //2) - 1]
        return (mid1 + mid2) / 2



