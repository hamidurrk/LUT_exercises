#include <stdio.h>

float mphToKmh(float mph) {
    return mph * 1.60934;
}

float kmhToMph(float kmh) {
    return kmh * 0.6;
}

int main() {
    int choice;
    float mph, kmh;
    do {
        printf("What is your choice?: \n");
        printf("1. Convert MpH to KmH\n");
        printf("2. Convert KmH to MpH\n");
        printf("0. Exit\n");

        scanf("%d", &choice);
        
        if (choice == 1) {
            printf("Give the speed in mph:\n");
            scanf("%f", &mph);
            kmh = mphToKmh(mph);

            printf("%0.2f mph is equals to %0.2f\n", mph, kmh);
        }
        
        if (choice == 2) {
            printf("Give the speed in kmh:\n");
            scanf("%f", &kmh);
            mph = kmhToMph(kmh);

            printf("%0.2f mph is equals to %0.2f\n", kmh, mph);
        }
    } while(choice != 0);

    printf("Bye bye!\n");
}
