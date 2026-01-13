#include <stdio.h>

int main() {
    double radius;
    double height;
    double volume;

    printf("Give the radius: ");
    scanf("%le", &radius);

    printf("Give the height: ");
    scanf("%le", &height);

    volume = 3.1416 * radius * radius * height;

    printf("The volume is %f\n", volume);

    return 0;
    
}