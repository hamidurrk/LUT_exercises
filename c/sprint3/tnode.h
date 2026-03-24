#ifndef TNODE_H
#define TNODE_H

typedef struct tnode {
    char data[20];
    struct tnode *left;
    struct tnode *right;
} TNode;

TNode *createTNode(const char *key);
void printTNode(TNode *nodePtr);
void inOrder(TNode *node);

#endif