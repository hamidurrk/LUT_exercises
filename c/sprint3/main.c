#include "bst.h"
#include "tnode.h"

#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int readChoice(int *choice)
{
    char arr[128];
    char *p;
    long n;

    if (choice == NULL) {
        return 0;
    }

    if (fgets(arr, sizeof(arr), stdin) == NULL) {
        return 0;
    }

    errno = 0;
    p = NULL;
    n = strtol(arr, &p, 10);

    while (p != NULL && (*p == ' ' || *p == '\t')) {
        p = p + 1;
    }

    if (p == NULL) {
        return 0;
    }

    if (*p != '\n' && *p != '\0') {
        return 0;
    }

    if (errno == ERANGE) {
        return 0;
    }

    if (n > INT_MAX || n < INT_MIN) {
        return 0;
    }

    *choice = (int)n;
    return 1;
}

static int readNoWhitespaceText(const char *prompt, char *out, size_t outSize)
{
    char arr[256];
    char *nl;
    size_t i;

    if (prompt == NULL || out == NULL || outSize == 0) {
        return 0;
    }

    printf("%s", prompt);
    if (fgets(arr, sizeof(arr), stdin) == NULL) {
        return 0;
    }

    nl = strchr(arr, '\n');
    if (nl != NULL) {
        *nl = '\0';
    }

    if (arr[0] == '\0') {
        return 0;
    }

    i = 0;
    while (arr[i] != '\0') {
        if (arr[i] == ' ' || arr[i] == '\t') {
            return 0;
        }
        i = i + 1;
    }

    i = 0;
    while (i + 1 < outSize && arr[i] != '\0') {
        out[i] = arr[i];
        i = i + 1;
    }
    out[i] = '\0';

    return 1;
}

static int readStartChar(char *ch)
{
    char arr[64];

    if (ch == NULL) {
        return 0;
    }

    printf("Enter initial letter: ");
    if (fgets(arr, sizeof(arr), stdin) == NULL) {
        return 0;
    }

    if (arr[0] == '\n' || arr[0] == '\0') {
        return 0;
    }

    *ch = arr[0];
    return 1;
}

int main(void)
{
    BST *tree;
    int stop;

    tree = createTree();
    if (tree == NULL) {
        return 1;
    }

    stop = 0;
    while (stop == 0) {
        int c;
        int ok;

        printf("\n1. Insert a node\n");
        printf("2. Filter by initial letter\n");
        printf("3. Search word\n");
        printf("4. Delete word\n");
        printf("5. Load file\n");
        printf("6. Store file\n");
        printf("7. Free the space and exit\n");
        printf("Enter your choice: ");

        c = -999;
        ok = readChoice(&c);

        if (ok == 0) {
            printf("Invalid choice. Please enter a number between 1 and 7.\n");
        } else {
            if (c == 1) {
                char word[20];
                TNode *n;

                if (readNoWhitespaceText("Enter word (max 19 chars, no whitespace): ", word,
                                         sizeof(word)) == 1) {
                    n = createTNode(word);
                    if (n != NULL) {
                        bstInsert(tree, n);
                    }
                } else {
                    printf("Invalid input.\n");
                }
            } else if (c == 2) {
                char ch;

                if (readStartChar(&ch) == 1) {
                    printAlphabetical(tree, ch);
                } else {
                    printf("Invalid input.\n");
                }
            } else if (c == 3) {
                char word[20];
                TNode *found;

                if (readNoWhitespaceText("Enter word (max 19 chars, no whitespace): ", word,
                                         sizeof(word)) == 1) {
                    found = Tsearch(tree, word);
                    if (found != NULL) {
                        printf("The address is: %p\n", (void *)found);
                    } else {
                        printf("Value not found\n");
                    }
                } else {
                    printf("Invalid input.\n");
                }
            } else if (c == 4) {
                char word[20];

                if (readNoWhitespaceText("Enter word (max 19 chars, no whitespace): ", word,
                                         sizeof(word)) == 1) {
                    TRemove(tree, word);
                } else {
                    printf("Invalid input.\n");
                }
            } else if (c == 5) {
                char filename[20];

                if (readNoWhitespaceText(
                        "Enter filename (max 19 chars, no whitespace): ", filename,
                        sizeof(filename)) == 1) {
                    TloadTextFile(tree, filename);
                } else {
                    printf("Invalid input.\n");
                }
            } else if (c == 6) {
                char filename[20];

                if (readNoWhitespaceText(
                        "Enter filename (max 19 chars, no whitespace): ", filename,
                        sizeof(filename)) == 1) {
                    TstoreTextFile(tree, filename);
                } else {
                    printf("Invalid input.\n");
                }
            } else if (c == 7) {
                printf("Exiting program...\n");
                stop = 1;
            } else {
                printf("Invalid choice. Please enter a number between 1 and 7.\n");
            }
        }
    }

    freeTree(tree);
    return 0;
}