import numpy as np

#(1) Store the test results for 5 students over 4 test sessions in a 2-dimensional array, with 100 points as the maximum score. Here, axis 0 corresponds to the students, and axis 1 corresponds to the test sessions. The values can be arbitrary.

a = np.array([[100, 99, 76, 88],
              [98, 70, 97, 54],
              [100, 100, 12, 98],
              [99, 80, 70, 60],
              [97, 95, 90, 85]])
print(a)

#(2) For each student, calculate the highest score, lowest score, average, and variance across the 4 test sessions. Store the results in a 2-dimensional array where axis 0 corresponds to the students and axis 1 corresponds to the aggregation results (highest score, lowest score, average, variance).

b = [[np.max(a, axis=1)[0], np.min(a, axis=1)[0], np.mean(a, axis=1)[0], np.std(a, axis=1)[0]],
     [np.max(a, axis=1)[1], np.min(a, axis=1)[1], np.mean(a, axis=1)[1], np.std(a, axis=1)[1]],
     [np.max(a, axis=1)[2], np.min(a, axis=1)[2], np.mean(a, axis=1)[2], np.std(a, axis=1)[2]],
     [np.max(a, axis=1)[3], np.min(a, axis=1)[3], np.mean(a, axis=1)[3], np.std(a, axis=1)[3]],
     [np.max(a, axis=1)[4], np.min(a, axis=1)[4], np.mean(a, axis=1)[4], np.std(a, axis=1)[4]]]

b = np.array(b)

print("\nColum 1: Highest Score")
print("Colum 2: Lowest Score")
print("Colum 3: Average Score")
print("Colum 4: Variance\n")
print(b)
print("\n")

#(3) For each test score, calculate the absolute difference between the score and the student's average score, resulting in a 2-dimensional array with shape (5, 4).

c = np.array([[np.abs(a[0,0] - b[0,2]), np.abs(a[0,1] - b[0,2]), np.abs(a[0,2] - b[0,2]), np.abs(a[0,3] - b[0,2])],
             [np.abs(a[1,0] - b[1, 2]), np.abs(a[1,1] - b[1, 2]), np.abs(a[1,2] - b[1, 2]), np.abs(a[1,3] - b[1, 2])],
             [np.abs(a[2,0] - b[2, 2]), np.abs(a[2,1] - b[2, 2]), np.abs(a[2,2] - b[2, 2]), np.abs(a[2,3] - b[2, 2])],
             [np.abs(a[3,0] - b[3,2]), np.abs(a[3,1] - b[3,2]), np.abs(a[3,2] - b[3,2]), np.abs(a[3,3] - b[3,2])],
             [np.abs(a[4,0] - b[4,2]), np.abs(a[4,1] - b[4,2]), np.abs(a[4,2] - b[4,2]), np.abs(a[4,3] - b[4,2])]])

print(c)