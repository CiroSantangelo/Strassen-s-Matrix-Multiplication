import numpy as np

def strassen(A, B):
    # Get the size of the matrices
    n = A.shape[0]
    
    # Base case: if the matrix is 1x1, simply multiply the elements
    if n == 1:
        return A * B
    else: 
        # Divide the matrices into quarters
        mid = n // 2
        A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
        B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]
        
        # Compute the seven products, recursively
        P1 = strassen(A11 + A22, B11 + B22)
        P2 = strassen(A21 + A22, B11)
        P3 = strassen(A11, B12 - B22)
        P4 = strassen(A22, B21 - B11)
        P5 = strassen(A11 + A12, B22)
        P6 = strassen(A21 - A11, B11 + B12)
        P7 = strassen(A12 - A22, B21 + B22)
        
        # Combine the intermediate products to get the result
        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 + P3 - P2 + P6 
        
        # Assemble the result from the four quarters
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
        
        return C

def main():
    # Define input matrices A and B
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]]) 
    
    # Find the size for padding to the next power of two
    n = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1])
    m = 1
    while m < n:
        m *= 2
    
    # Pad the matrices A and B to size m x m with zeros
    A = np.pad(A, ((0, m - A.shape[0]), (0, m - A.shape[1])), mode='constant')
    B = np.pad(B, ((0, m - B.shape[0]), (0, m - B.shape[1])), mode='constant')
    
    # Perform the Strassen matrix multiplication
    C = strassen(A, B)
    
    # Print the relevant submatrix of the result
    print(C[:2, :2])
    
if __name__ == "__main__":
    main()
