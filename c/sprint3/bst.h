#ifndef BST_H
#define BST_H

#include "tnode.h"

typedef struct {
    TNode *root;
} BST;

BST *createTree(void);
int treeEmpty(BST *tree);
void bstInsert(BST *tree, TNode *newNode);
void printAlphabetical(BST *tree, char startChar);
TNode *Tsearch(BST *tree, char *key);
void TRemove(BST *tree, char *key);
void TloadTextFile(BST *tree, char *filename);
void TstoreTextFile(BST *tree, char *filename);
void freeTree(BST *tree);

#endif