#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dll.h"

DLL* createList() {
    DLL *l = malloc(sizeof(DLL));
    l->head = NULL;
    return l;
}

int listEmpty(DLL *list) {
    if (list->head == NULL) {
        return 1;
    }
    return 0;
}

void insert(DLL *list, Node *newNode) {
    Node *prev = NULL;
    Node *cur = list->head;

    while (cur != NULL && strcmp(cur->data, newNode->data) < 0) {
        prev = cur;
        cur = cur->next;
    }

    newNode->prev = prev;
    newNode->next = cur;

    if (prev == NULL) {
        list->head = newNode;
    } else {
        prev->next = newNode;
    }

    if (cur != NULL) {
        cur->prev = newNode;
    }
}

void displayList(DLL *list) {
    printf("List: ");

    if (listEmpty(list)) {
        printf("\n");
        return;
    }

    for (Node *cur = list->head; cur != NULL; cur = cur->next) {
        printNode(cur);
        if (cur->next != NULL) {
            printf(" <-> ");
        }
    }
    printf("\n");
}
