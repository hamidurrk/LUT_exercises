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

void inOrderFiltered(TNode *node, char startChar)
{
    if (node != NULL) {
        if (node->left != NULL) {
            inOrderFiltered(node->left, startChar);
        }

        if (node->data[0] == startChar) {
            printTNode(node);
        }

        if (node->right != NULL) {
            inOrderFiltered(node->right, startChar);
        }
    }
}

void writePreOrder(TNode *node, FILE *fp)
{
    if (node != NULL && fp != NULL) {
        fprintf(fp, "%s\n", node->data);

        if (node->left != NULL) {
            writePreOrder(node->left, fp);
        }
        if (node->right != NULL) {
            writePreOrder(node->right, fp);
        }
    }
}

void freeNodes(TNode *node)
{
    if (node != NULL) {
        if (node->left != NULL) {
            freeNodes(node->left);
        }
        if (node->right != NULL) {
            freeNodes(node->right);
        }
        free(node);
    }
}