# Given an image represented by an NxN matrix, where each
# pixel in the image is 4 bytes, write a method to rotate
# the image by 90 degrees. Can you do this in place? 

def rotateMatrix(matrix) -> None:
    
    n = len(matrix)

    left, right = 0, n - 1
    
    # each iteration of while loop 
    # represents a "layer" of the matrix
    # starting outward going inward 
    while(left < right):
        top, bottom = left, right
        
        for i in range(right - left):
            # record temp values
            top_left = matrix[top][left + i]
            top_right = matrix[top + i][right]
            bottom_right = matrix[bottom][right - i]
            bottom_left = matrix[bottom - i][left]

            # move bottom left to top left 
            matrix[top][left + i] = bottom_left
            # move top left to top right
            matrix[top + i][right] = top_left
            # move top right to bottom right
            matrix[bottom][right - i] = top_right
            # move bottom right to bottom left 
            matrix[bottom - i][left] = bottom_right

        left += 1
        right -= 1

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("ORIGINAL MATRIX")
for row in a:
    print(row)

rotateMatrix(a)
print("ROTATED MATRIX")
for row in a:
    print(row)