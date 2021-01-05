from CheckArrayFormation import canFormArray

if __name__ == '__main__':
    print("CheckArrayFormation")
    pieces = [[78],[4,64],[91]]
    arr = [91,4,64,78]
    print(canFormArray(arr, pieces))
    pieces = [[85]]
    arr = [85]
    print(canFormArray(arr, pieces))
    pieces = [[2,4,6,8]]
    arr = [1,3,5,7]
    print(canFormArray(arr, pieces))
    pieces = [[60],[52,38],[66],[39],[19],[1],[84,55],[17],[14],[49],[91],[5],[75]]
    arr = [75,1,60,91,84,55,5,39,19,52,38,66,14,17,49]
    print(canFormArray(arr, pieces))
    arr = [49, 18, 16]
    pieces = [[16, 18, 49]]
    print(canFormArray(arr, pieces))
    arr = [1, 2, 3]
    pieces = [[2], [1, 3]]
    print(canFormArray(arr, pieces))