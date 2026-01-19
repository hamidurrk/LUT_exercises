#include <stdio.h>

int main() {
    double w, h;

    printf("Width: ");
    scanf("%lf", &w);
    
    printf("Height: ");
    scanf("%lf", &h);

    printf("Area: %e\n", w*h);

    return 0;
}