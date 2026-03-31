#ifndef TNODE_H
#define TNODE_H

#include <stdio.h>

typedef struct tnode {
    char data[20];
    struct tnode *left;
    struct tnode *right;
} TNode;

TNode *createTNode(const char *key);
void printTNode(TNode *nodePtr);
void inOrderFiltered(TNode *node, char startChar);
void writePreOrder(TNode *node, FILE *fp);
void freeNodes(TNode *node);

#endif