import numpy as np
import time

def es1(array_1d: np.array ):
    return array_1d[::-1]

def es2():
    '''
    Given the following square array, compute the product of the elements on its
    diagonal. [[1 3 8] [-1 3 0] [-3 9 2]]
    '''
    A = np.array([[1,3,8],  
                  [-1,3,0], 
                  [-3,9,2]])

    print(A)
    print(A.shape)

    res = 1
    for i, array in enumerate(A):
        res *= array[i]

    return res

def es3():
    A = np.random.rand(3,6)

    mean_val = np.mean(A)   
    return mean_val


def es4():
    '''
    Given two arrays a and b, compute how many time an item of a is higher than the
corresponding element of b.
a: [[1 5 6 8] [2 -3 13 23] [0 -10 -9 7]]
b: [[-3 0 8 1] [-20 -9 -1 32] [7 7 7 7]]
    '''

    a = np.array([

    [1, 5, 6, 8],

    [2, -3, 13, 23],

    [0, -10, -9, 7]

    ])

    b = np.array([

        [-3, 0, 8, 1],

        [-20, -9, -1, 32],

        [7, 7, 7, 7]

    ])

    res = np.sum(a > b)

    print(res)

def eucl_distance():
    A = np.random.rand(100000, 100)
    b = np.random.rand(100)

    start = time.perf_counter()

    distances = []
    for row in A:
        sum = 0
        for i in range(len(b)):
            diff = row[i] - b[i]
            sum += diff * diff
        distances.append(sum ** 0.5)

    end = time.perf_counter()

    print("Tempo:", end - start)

    start = time.perf_counter()

    distances = np.sqrt(np.sum((A-b) ** 2, axis=1))

    end = time.perf_counter()

    print("Tempo:", end - start)



def main():
    eucl_distance()

if __name__ == "__main__":
    main()