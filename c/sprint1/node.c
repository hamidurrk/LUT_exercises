#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"

Node* createNode(const char *key) {
    Node *n = malloc(sizeof(Node));
    n->prev = NULL;
    n->next = NULL;

    if (key == NULL) {
        printf("Enter a string: ");
        fgets(n->data, 20, stdin);

        for (int i = 0; n->data[i] != '\0'; i++) {
            if (n->data[i] == '\n') {
                n->data[i] = '\0';
                break;
            }
        }
    } else {
        strncpy(n->data, key, 19);
        n->data[19] = '\0';
    }

    return n;
}

void printNode(Node *nodePtr) {
    if (nodePtr == NULL) {
        printf("The node is NULL.");
        return;
    }
    printf("[%s]", nodePtr->data);
}
