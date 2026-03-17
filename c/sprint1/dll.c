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

Node *search(DLL *L, char *key) {
    Node *cur = L->head;

    while (cur != NULL) {
        if (strcmp(cur->data, key) == 0) {
            return cur;
        }
        cur = cur->next;
    }

    return NULL;
}

void Remove(DLL *L, Node *ptr) {
    if (ptr->prev != NULL) {
        ptr->prev->next = ptr->next;
    } else {
        L->head = ptr->next;
    }

    if (ptr->next != NULL) {
        ptr->next->prev = ptr->prev;
    }

    free(ptr);
}

void displayList(DLL *list, char startChar) {
    printf("List: ");

    if (listEmpty(list)) {
        printf("\n");
        return;
    }

    Node *cur = list->head;
    int firstPrinted = 1;

    while (cur != NULL) {
        if (cur->data[0] == startChar) {
            if (!firstPrinted) {
                printf(" <-> ");
            }
            printNode(cur);
            firstPrinted = 0;
        }
        cur = cur->next;
    }

    printf("\n");
}

void loadTextFile(DLL *L, char *filename) {
    FILE *f = fopen(filename, "r");
    char line[100];

    if (f == NULL) {
        printf("Could not open file.\n");
        return;
    }

    while (fgets(line, sizeof(line), f) != NULL) {
        int i = 0;
        while (line[i] != '\0') {
            if (line[i] == '\n') {
                line[i] = '\0';
                break;
            }
            i++;
        }

        Node *n = createNode(line);
        insert(L, n);
    }

    fclose(f);
}

void storeTextFile(DLL *L, char *filename) {
    FILE *f = fopen(filename, "w");

    if (f == NULL) {
        printf("Could not open file.\n");
        return;
    }

    if (listEmpty(L)) {
        fclose(f);
        return;
    }

    Node *cur = L->head;
    while (cur->next != NULL) {
        cur = cur->next;
    }

    while (cur != NULL) {
        fprintf(f, "%s\n", cur->data);
        cur = cur->prev;
    }

    fclose(f);
}

void freeList(DLL *L) {
    Node *cur = L->head;

    while (cur != NULL) {
        Node *nextNode = cur->next;
        free(cur);
        cur = nextNode;
    }

    free(L);
}
