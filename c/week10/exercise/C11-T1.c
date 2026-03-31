#include <stdio.h>
#include <time.h>

int main(void)
{
	long start_input;
	long end_input;

	printf("Please input two integers:\n");
	if (scanf("%ld %ld", &start_input, &end_input) != 2) {
		return 0;
	}

	time_t start_time = (time_t)start_input;
	time_t end_time = (time_t)end_input;
	double duration = difftime(end_time, start_time);

	printf("Start: %s", ctime(&start_time));
	printf("Duration: %.2f seconds\n", duration);

	return 0;
}
