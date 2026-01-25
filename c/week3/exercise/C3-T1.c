#include <stdio.h>

int main() {
    float input, bill;
    int tier1 = 500;
    int tier2 = 1000;

    if (input < 0) return 0;

    bill = ((int)input % tier2) * (input - tier2);
}