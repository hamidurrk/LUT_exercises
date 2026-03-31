#include "bst.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

void printAlphabetical(BST *tree, char startChar)
{
    int empty;

    empty = treeEmpty(tree);
    if (empty == 1) {
        printf("Tree is empty.\n");
    } else {
        printf("Tree: ");
        inOrderFiltered(tree->root, startChar);
        printf("\n");
    }
}

TNode *Tsearch(BST *tree, char *key)
{
    TNode *p;

    if (tree == NULL || key == NULL) {
        return NULL;
    }

    p = tree->root;
    while (p != NULL) {
        int comp;

        comp = strcmp(key, p->data);
        if (comp == 0) {
            return p;
        }
        if (comp < 0) {
            p = p->left;
        } else {
            p = p->right;
        }
    }

    return NULL;
}

void TRemove(BST *tree, char *key)
{
    TNode *parent;
    TNode *curr;

    if (tree == NULL || key == NULL) {
        printf("Value not found\n");
        return;
    }

    parent = NULL;
    curr = tree->root;

    while (curr != NULL && strcmp(key, curr->data) != 0) {
        parent = curr;
        if (strcmp(key, curr->data) < 0) {
            curr = curr->left;
        } else {
            curr = curr->right;
        }
    }

    if (curr == NULL) {
        printf("Value not found\n");
        return;
    }

    if (curr->left != NULL && curr->right != NULL) {
        TNode *succParent;
        TNode *succ;

        succParent = curr;
        succ = curr->right;

        while (succ->left != NULL) {
            succParent = succ;
            succ = succ->left;
        }

        strcpy(curr->data, succ->data);
        parent = succParent;
        curr = succ;
    }

    {
        TNode *child;

        if (curr->left != NULL) {
            child = curr->left;
        } else {
            child = curr->right;
        }

        if (parent == NULL) {
            tree->root = child;
        } else {
            if (parent->left == curr) {
                parent->left = child;
            } else {
                parent->right = child;
            }
        }

        printf("The node at address %p is deleted\n", (void *)curr);
        free(curr);
    }
}

void TloadTextFile(BST *tree, char *filename)
{
    FILE *fp;
    char word[256];

    if (tree == NULL || filename == NULL) {
        return;
    }

    fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Could not open file.\n");
        return;
    }

    while (fgets(word, sizeof(word), fp) != NULL) {
        char *nl;
        TNode *n;

        nl = strchr(word, '\n');
        if (nl != NULL) {
            *nl = '\0';
        }

        if (word[0] != '\0') {
            n = createTNode(word);
            if (n != NULL) {
                bstInsert(tree, n);
            }
        }
    }

    fclose(fp);
}

void TstoreTextFile(BST *tree, char *filename)
{
    FILE *fp;

    if (tree == NULL || filename == NULL) {
        return;
    }

    fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Could not open file.\n");
        return;
    }

    writePreOrder(tree->root, fp);
    fclose(fp);
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