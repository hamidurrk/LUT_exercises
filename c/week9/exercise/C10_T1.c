#include <ctype.h>
#include <stdio.h>

void toUpperCase(char *str) {
	for (int i = 0; str[i] != '\0'; i++) {
		str[i] = (char)toupper((unsigned char)str[i]);
	}
}

void toLowerCase(char *str) {
	for (int i = 0; str[i] != '\0'; i++) {
		str[i] = (char)tolower((unsigned char)str[i]);
	}
}

int main(void) {
	char str[1000];
	int choice;
	void (*stringFunctions[])(char *) = {toUpperCase, toLowerCase};

	printf("Enter a string:\n");
	if (fgets(str, sizeof(str), stdin) == NULL) {
		return 1;
	}

	for (int i = 0; str[i] != '\0'; i++) {
		if (str[i] == '\n') {
			str[i] = '\0';
			break;
		}
	}

	printf("Choose operation:\n");
	printf("1. Uppercase\n");
	printf("2. Lowercase\n");
	printf("Enter your choice:\n");

	if (scanf("%d", &choice) != 1 || choice < 1 || choice > 2) {
		return 1;
	}

	stringFunctions[choice - 1](str);
	printf("Processed String: %s\n", str);

	return 0;
}
