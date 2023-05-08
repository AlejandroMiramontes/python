M1 = [[1, 2, 3], 
     [4, 5, 6]]

M2 = [[-1, 0],
      [0, 1],
      [1, 1]]

M3 = [[0,0],
      [0,0]]

#Multiplicacion de las matrices M1 y M2
for i in range(len(M1)):
 for j in range(len(M2[0])):
  for k in range(len(M2)):
        M3[i][j] += M1[i][k] * M2[k][j]
print(M3)