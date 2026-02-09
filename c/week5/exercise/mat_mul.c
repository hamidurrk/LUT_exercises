void MatMul(const double Mat1[2][2], const double Mat2[2][2], double ResMat[2][2]) {
    ResMat[0][0] = Mat1[0][0] * Mat2[0][0] + Mat1[0][1] * Mat2[1][0];
    ResMat[0][1] = Mat1[0][0] * Mat2[0][1] + Mat1[0][1] * Mat2[1][1];
    ResMat[1][0] = Mat1[1][0] * Mat2[0][0] + Mat1[1][1] * Mat2[1][0];
    ResMat[1][1] = Mat1[1][0] * Mat2[0][1] + Mat1[1][1] * Mat2[1][1];
}
