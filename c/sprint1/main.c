#include <stdio.h>
#include "dll.h"

int main() {
    DLL *list = createList();
    int option;

    while (1) {
        printf("\n1. Insert a string\n");
        printf("2. Display the list\n");
        printf("3. Check if empty\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");

        if (scanf("%d", &option) != 1) {
            printf("Invalid choice.\n");
            char ch;
            do {
                ch = getchar();
            } while (ch != '\n');
            continue;
        }

        if (option == 4) {
            printf("Exited.\n");
            break;
        } else if (option == 1) {
            char ch;
            do {
                ch = getchar();
            } while (ch != '\n');

            Node *node = createNode(NULL);
            insert(list, node);
        } else if (option == 2) {
            displayList(list);
        } else if (option == 3) {
            if (listEmpty(list)) {
                printf("List empty.\n");
            } else {
                printf("List not empty.\n");
            }
        } else {
            printf("Invalid.\n");
        }
    }

    return 0;
}
