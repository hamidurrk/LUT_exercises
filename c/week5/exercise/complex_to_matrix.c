#include <complex.h>

void ComplexToMatrix(const double complex z, double Matrix[2][2]) {
    double a = creal(z);
    double b = cimag(z);
    
    Matrix[0][0] = a;
    Matrix[0][1] = -b;
    Matrix[1][0] = b;
    Matrix[1][1] = a;
}