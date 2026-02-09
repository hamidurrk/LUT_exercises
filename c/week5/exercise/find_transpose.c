#include <stddef.h>
#include <stdlib.h>
#include <string.h>

void FindTranspose(long double* pldbl, const size_t nRows, const size_t nCols) {
    long double* temp = (long double*)malloc(nRows * nCols * sizeof(long double));
    
    for (size_t i = 0; i < nRows; i++) {
        for (size_t j = 0; j < nCols; j++) {
            temp[j * nRows + i] = pldbl[i * nCols + j];
        }
    }
    
    memcpy(pldbl, temp, nRows * nCols * sizeof(long double));
    
    free(temp);
}