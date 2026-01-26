#include <stdio.h>

int main() {
    float usage, bill;
    
    printf("How much electricity did you use this month?\n");
    scanf("%f", &usage);
    
    if (usage <= 500) {
        bill = usage * 0.18;
    }
    else if (usage <= 1000) {
        bill = 500 * 0.18 + (usage - 500) * 0.21;
    }
    else {
        bill = 500 * 0.18 + 500 * 0.21 + (usage - 1000) * 0.25;
    }
    
    printf("Total electricity bill this month is %.2f EUR.\n", bill);
    
    return 0;
}