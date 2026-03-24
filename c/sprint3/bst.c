#include "bst.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void freeNodes(TNode *node)
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

BST *createTree(void)
{
    BST *x;

    x = (BST *)malloc(sizeof(BST));
    if (x == NULL) {
        printf("Memory allocation failed.\n");
        return NULL;
    }

    x->root = NULL;
    return x;
}

int treeEmpty(BST *tree)
{
    int ans;

    ans = 0;
    if (tree == NULL) {
        ans = 1;
    } else {
        if (tree->root == NULL) {
            ans = 1;
        }
    }

    return ans;
}

void bstInsert(BST *tree, TNode *newNode)
{
    TNode *p;
    int done;

    if (tree != NULL && newNode != NULL) {
        if (tree->root == NULL) {
            tree->root = newNode;
        } else {
            p = tree->root;
            done = 0;

            while (done == 0) {
                int comp;

                comp = strcmp(newNode->data, p->data);

                if (comp == 0) {
                    free(newNode);
                    done = 1;
                } else {
                    if (comp < 0) {
                        if (p->left == NULL) {
                            p->left = newNode;
                            done = 1;
                        } else {
                            p = p->left;
                        }
                    } else {
                        if (p->right == NULL) {
                            p->right = newNode;
                            done = 1;
                        } else {
                            p = p->right;
                        }
                    }
                }
            }
        }
    }
}

void printAlphabetical(BST *tree)
{
    int empty;

    empty = treeEmpty(tree);
    if (empty == 1) {
        printf("Tree is empty.\n");
    } else {
        printf("Tree: ");
        inOrder(tree->root);
        printf("\n");
    }
}

void freeTree(BST *tree)
{
    if (tree != NULL) {
        if (tree->root != NULL) {
            freeNodes(tree->root);
            tree->root = NULL;
        }
        free(tree);
    }
}