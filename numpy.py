____________________________________________________________ NUMPY DIRECTORY_____________________________________________________________
                                                            --RISHABH SOOD--

Date Created: 10/10/2019
_________________________________________________________________________________________________________________________________________

_________________________________________________________________________________________________________________________________________

Vectors, Matrices and Arrays

-> Creating a Matrix:
   - import numpy as np

     matrix_name = np.array([e1 ,e2 ,e3],
     	                    [e4 ,e5 ,e6],
     	                    [e7 ,e8 ,e9])
   # This creates an array:

   #  e1 e2 e3
   #  e4 e5 e6   -> matrix_name
   #  e7 e8 e9
-> Sparse Matrix is one which only stores non null elements and their addreses in the matrix.
-> Creating a Sparse matrix:
   - from scipy import sparse

     matrix_sparse = sparse.csr_matrix(matrix_name)
-> selecting elements of a matrix or vector: 
   -> #vector_name[elem_index] or for multiple element selection -vector_name[start_index:end_index]
   -> similar can be done for Matrices
   -> -1 index refers to last element.
-> matrix_name.shape returns (row_size ,col_size) of the matrix.
-> matrix_name.size returns row_size*col_size
-> matrix_name.ndim returns dimensional degree of the matrix.
-> inline functions in python are declared using lambda var_name: var_name.operation
-> np.vectorize(func_name) generates a vectorized function from a general function func_name.
-> np.max(matrix_name) returns the largest element in the matrix.

