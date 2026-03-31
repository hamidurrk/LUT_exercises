#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int seed;

	printf("Give me your seed:\n");
	if (scanf("%d", &seed) != 1) {
		return 0;
	}

	srand(seed);

	for (int i = 0; i < 5; i++) {
		int value = rand() % 100 + 1;
		printf("%d", value);
		if (i < 4) {
			printf(" ");
		}
	}
	printf("\n");

	return 0;
}
