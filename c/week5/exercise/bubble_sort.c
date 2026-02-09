#include <stddef.h>

void BubbleSort(int ai[], const size_t n) {
    for (size_t i = 0; i < n - 1; i++) {
        for (size_t j = 0; j < n - i - 1; j++) {
            if (ai[j] > ai[j + 1]) {
                int temp = ai[j];
                ai[j] = ai[j + 1];
                ai[j + 1] = temp;
            }
        }
    }
}