#include <stdio.h>
#include <math.h>

int main(void)
{
	const double g = 9.8;
	double v;
	double theta;

	printf("Enter initial speed v (m/s):\n");
	if (scanf("%lf", &v) != 1) {
		return 0;
	}

	printf("Enter launch angle theta (radians):\n");
	if (scanf("%lf", &theta) != 1) {
		return 0;
	}

	double h_exact = (v * v * sin(theta) * sin(theta)) / (2.0 * g);
	double t_exact = (2.0 * v * sin(theta)) / g;

	double h_floor = floor(h_exact);
	double h_ceil = ceil(h_exact);
	double t_floor = floor(t_exact);
	double t_ceil = ceil(t_exact);

	printf("Maximum Height:\n");
	printf("--Exact: %.2f m\n", h_exact);
	printf("--Floor: %.2f m\n", h_floor);
	printf("--Ceil : %.2f m\n", h_ceil);

	printf("\n");

	printf("Total Flight Time:\n");
	printf("--Exact: %.2f s\n", t_exact);
	printf("--Floor: %.2f s\n", t_floor);
	printf("--Ceil : %.2f s\n", t_ceil);

	return 0;
}
