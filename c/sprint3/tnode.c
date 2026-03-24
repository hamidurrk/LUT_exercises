#include "tnode.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

TNode *createTNode(const char *key)
{
    TNode *n;
    char localInput[200];
    char *nl;
    const char *useThis;
    int i;

    n = (TNode *)malloc(sizeof(TNode));
    if (n == NULL) {
        printf("Memory allocation failed.\n");
        return NULL;
    }

    n->left = NULL;
    n->right = NULL;

    useThis = key;
    if (useThis == NULL) {
        printf("Enter string: ");
        if (fgets(localInput, sizeof(localInput), stdin) == NULL) {
            localInput[0] = '\0';
        }
        nl = strchr(localInput, '\n');
        if (nl != NULL) {
            *nl = '\0';
        }
        useThis = localInput;
    }

    i = 0;
    while (i < 19 && useThis[i] != '\0') {
        n->data[i] = useThis[i];
        i = i + 1;
    }
    n->data[i] = '\0';

    return n;
}

void printTNode(TNode *nodePtr)
{
    if (nodePtr != NULL) {
        printf("(%s)", nodePtr->data);
    } else {
        printf("The node is NULL.");
    }
}

void inOrder(TNode *node)
{
    TNode *leftSide;
    TNode *rightSide;

    if (node != NULL) {
        leftSide = node->left;
        rightSide = node->right;

        if (leftSide != NULL) {
            inOrder(leftSide);
        }

        printTNode(node);

        if (rightSide != NULL) {
            inOrder(rightSide);
        }
    }
}