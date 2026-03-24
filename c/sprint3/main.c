#include "bst.h"
#include "tnode.h"

#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

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
        printf("2. Test if tree is empty\n");
        printf("3. Print tree\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");

        c = -999;
        ok = readChoice(&c);

        if (ok == 0) {
            printf("Invalid choice. Please enter a number between 1 and 4.\n");
        } else {
            if (c == 1) {
                TNode *n;
                n = createTNode(NULL);
                if (n != NULL) {
                    bstInsert(tree, n);
                }
            } else if (c == 2) {
                int e;
                e = treeEmpty(tree);
                if (e == 1) {
                    printf("Tree is empty.\n");
                } else {
                    printf("Tree is not empty.\n");
                }
            } else if (c == 3) {
                printAlphabetical(tree);
            } else if (c == 4) {
                stop = 1;
            } else {
                printf("Invalid choice. Please enter a number between 1 and 4.\n");
            }
        }
    }

    freeTree(tree);
    return 0;
}