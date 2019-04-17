# Edit Distance / Alignment Program
# Description: Given 2 strings, this program constructs an edit distance
#              graph using a 2D array, provides the edit distance value, 
#              and performs an alignment of the two strings to reflect
#              the calculated edits

import sys

def editDist(str1, str2):
   # to store path information for backtracking 
   pathTracker = {}

   # initialize len(str1)+1 x len(str2)+1 2D array 
   matrix = [[None for col in range(len(str2) + 1)] for row in range(len(str1) + 1)]

   # assign increasing values to first row and col
   matrix[0][0] = 0
   for i in range(1, len(str1) + 1):
      matrix[i][0] = i
      pathTracker[(i, 0)] = ((i - 1, 0), 'U')
   for i in range(1, len(str2) + 1):
      matrix[0][i] = i
      pathTracker[(0, i)] = ((0, i - 1), 'L')

   # populate matrix values
   for row in range(1, len(str1) + 1):
      for col in range(1, len(str2) + 1):
         pathData = None
         prevRow = row - 1
         prevCol = col - 1

         # there is a match
         if str2[prevCol] == str1[prevRow]:
            matrix[row][col] = matrix[prevRow][prevCol]
            pathTracker[(row, col)] = ((prevRow, prevCol), 'D')

         # pick min from diagonal, left, and upper fields
         else:
            diagonal = matrix[prevRow][prevCol]
            left = matrix[row][prevCol]
            up = matrix[prevRow][col]
            matrix[row][col] = min(diagonal, left, up) + 1

            # store path information for future alignment use
            minVal = diagonal
            pathData = ((prevRow, prevCol), 'D')
            if left < minVal:
               minVal = left
               pathData = ((row, prevCol), 'L')
            if up < minVal:
               minVal = up
               pathData = ((prevRow, col), 'U')
               if left < up:
                  minVal = left
                  pathData = ((row, prevCol), 'L')
            pathTracker[(row, col)] = pathData
   
   # Back tracking to obtain alignment
   alignment1 = ''
   alignment2= ''
   position = (len(str1), len(str2)) # start at bottom right corner of matrix

   while True:
      # retrieve parent coordinates and direction from dictionary
      origin, direction = pathTracker[position]

      # case diagonal origin
      if direction == 'D':
         alignment1 = str1[position[0] - 1] + alignment1
         alignment2 = str2[position[1] - 1] + alignment2

      # case left origin
      elif direction == 'L':
         alignment1 = '_' + alignment1
         alignment2 = str2[position[1] - 1] + alignment2

      # case up origin
      else:
         alignment1 = str1[position[0] - 1] + alignment1
         alignment2 = '_' + alignment2
      
      # case done backtracking
      if origin == (0, 0):
         break

      # update the position to check next
      position = origin

   # output matrix and alignment
   print("The matrix:\n")
   print('-' * len(matrix[1]) * 6)
   print('\n')
   for row in matrix:
      for num in row:
        print("{:4}".format(num), ':' ,end="")
      print('\n')
      print('-' * len(row) * 6)
      print('\n')

   print("The edit distance is: ", matrix[len(str1)][len(str2)])

   print("\nAlignment is:")
   print(alignment1)
   print(alignment2)

   return

if __name__ == '__main__':
   word1 = word2 = ''
   word1 = input("The first word: ")
   word2 = input("The second word: ")
   if word1 == '' or word2 == '':
      sys.exit("Invalid Entry")

   editDist(word1, word2)
