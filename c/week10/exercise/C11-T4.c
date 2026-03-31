#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	char name[20];
	int score;
} Athlete;

int compare_athletes(const void *a, const void *b)
{
	const Athlete *athlete_a = (const Athlete *)a;
	const Athlete *athlete_b = (const Athlete *)b;

	if (athlete_a->score != athlete_b->score) {
		return athlete_b->score - athlete_a->score;
	}

	return strcmp(athlete_a->name, athlete_b->name);
}

int main(void)
{
	Athlete athletes[5];

	for (int i = 0; i < 5; i++) {
		printf("Please input %d athlete info:\n", i + 1);
		if (scanf("%19s %d", athletes[i].name, &athletes[i].score) != 2) {
			return 0;
		}
	}

	qsort(athletes, 5, sizeof(Athlete), compare_athletes);

	printf("\nRanking:\n");
	for (int i = 0; i < 5; i++) {
		printf("%s %d\n", athletes[i].name, athletes[i].score);
	}

	return 0;
}
