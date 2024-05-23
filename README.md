# Strassen Matrix Multiplication

This repository contains an implementation of Strassen's algorithm for matrix multiplication using Python and NumPy. Strassen's algorithm is an efficient algorithm for multiplying large matrices, reducing the complexity compared to the standard matrix multiplication.

## Table of Contents

- [Introduction](#introduction)
- [Algorithm Details](#algorithm-details)
- [Usage](#usage)
- [Example](#example)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

Strassen's algorithm is a divide-and-conquer algorithm invented by Volker Strassen in 1969. It is more efficient than the standard matrix multiplication algorithm for large matrices. This implementation in Python uses NumPy to handle matrix operations and demonstrates the power of Strassen's method.

## Algorithm Details

The `strassen` function implements the Strassen matrix multiplication algorithm. Here's a detailed explanation of how it works:

1. **Matrix Size Check**:
   - The function takes two matrices `A` and `B` as inputs.
   - It first determines the size `n` of the matrices.

2. **Base Case**:
   - If the matrices are 1x1, it simply returns the product of the two elements.

3. **Recursive Division**:
   - If the matrices are larger, they are divided into four submatrices:
     - `A11`, `A12`, `A21`, `A22` for matrix `A`
     - `B11`, `B12`, `B21`, `B22` for matrix `B`

4. **Seven Recursive Products**:
   - Seven products are calculated using the Strassen method:
     - `P1 = strassen(A11 + A22, B11 + B22)`
     - `P2 = strassen(A21 + A22, B11)`
     - `P3 = strassen(A11, B12 - B22)`
     - `P4 = strassen(A22, B21 - B11)`
     - `P5 = strassen(A11 + A12, B22)`
     - `P6 = strassen(A21 - A11, B11 + B12)`
     - `P7 = strassen(A12 - A22, B21 + B22)`

5. **Combining Results**:
   - The results from these products are combined to form the final submatrices of the result:
     - `C11 = P1 + P4 - P5 + P7`
     - `C12 = P3 + P5`
     - `C21 = P2 + P4`
     - `C22 = P1 + P3 - P2 + P6`

6. **Assembling the Final Matrix**:
   - These submatrices (`C11`, `C12`, `C21`, `C22`) are then combined to form the final result matrix `C` using `np.vstack` and `np.hstack`.
