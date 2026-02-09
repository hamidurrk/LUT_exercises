#include <stdio.h>
#include <complex.h>

void ComplexToMatrix(const double complex z, double Matrix[2][2]);
void MatMul(const double Mat1[2][2], const double Mat2[2][2], double ResMat[2][2]);

int main() {
    double a1, b1, a2, b2;
    double complex z1, z2;
    double Mat1[2][2], Mat2[2][2], ResMat[2][2];
    
    printf("First complex number: ");
    scanf("%lf + %lfi", &a1, &b1);
    z1 = a1 + b1 * I;
    
    printf("Second complex number: ");
    scanf("%lf + %lfi", &a2, &b2);
    z2 = a2 + b2 * I;
    
    ComplexToMatrix(z1, Mat1);
    ComplexToMatrix(z2, Mat2);
    
    MatMul(Mat1, Mat2, ResMat);
    
    printf("[ %f %f ]\n", ResMat[0][0], ResMat[0][1]);
    printf("[ %f %f ]\n", ResMat[1][0], ResMat[1][1]);
    
    return 0;
}
