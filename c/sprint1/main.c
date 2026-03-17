#include <stdio.h>
#include <string.h>
#include "dll.h"

int main() {
    DLL *list = createList();
    int option;
    char key[100];
    char filename[200];
    char startChar;

    while (1) {
        printf("\n1. Insert a string\n");
        printf("2. Filter by initial letter\n");
        printf("3. Find a string and delete it\n");
        printf("4. Import data from a file\n");
        printf("5. Store list to a file\n");
        printf("6. Free the space and exit\n");
        printf("Enter your choice: ");

        if (scanf("%d", &option) != 1) {
            printf("Invalid choice.\n");
            int ch = getchar();
            while (ch != '\n' && ch != EOF) {
                ch = getchar();
            }
            continue;
        }

        int ch = getchar();
        while (ch != '\n' && ch != EOF) {
            ch = getchar();
        }

        if (option == 1) {
            Node *node = createNode(NULL);
            insert(list, node);
        } else if (option == 2) {
            printf("Enter initial letter: ");
            if (fgets(key, sizeof(key), stdin) != NULL) {
                startChar = key[0];
                displayList(list, startChar);
            }
        } else if (option == 3) {
            printf("Enter string to find and delete: ");
            if (fgets(key, sizeof(key), stdin) != NULL) {
                key[strcspn(key, "\n")] = '\0';

                Node *found = search(list, key);
                if (found != NULL) {
                    Remove(list, found);
                    printf("String deleted.\n");
                } else {
                    printf("String not found.\n");
                }
            }
        } else if (option == 4) {
            printf("Enter filename: ");
            if (fgets(filename, sizeof(filename), stdin) != NULL) {
                filename[strcspn(filename, "\n")] = '\0';
                loadTextFile(list, filename);
            }
        } else if (option == 5) {
            printf("Enter filename: ");
            if (fgets(filename, sizeof(filename), stdin) != NULL) {
                filename[strcspn(filename, "\n")] = '\0';
                storeTextFile(list, filename);
            }
        } else if (option == 6) {
            freeList(list);
            printf("Done.\n");
            break;
        } else {
            printf("Invalid choice.\n");
        }
    }

    return 0;
}
