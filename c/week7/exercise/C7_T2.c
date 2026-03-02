#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct {
    Node *first; 
    Node *last;  
} List;

void add(List *L, int value) {
    Node *new_node = (Node*)malloc(sizeof(Node));
    new_node->data = value;
    new_node->next = NULL;
    
    if (L->first == NULL) {
        L->first = new_node;
        L->last = new_node;
    } else {
        L->last->next = new_node;
        L->last = new_node;
    }
}

int find_max(List *L) {
    Node *current = L->first;
    int max = current->data;
    
    while (current != NULL) {
        if (current->data > max) {
            max = current->data;
        }
        current = current->next;
    }
    
    return max;
}

int main() {
    int n, value;
    
    List *L = (List*)malloc(sizeof(List));
    L->first = NULL;
    L->last = NULL;
    
    printf("Enter the number of integers: ");
    scanf("%d", &n);
    
    printf("Enter %d integers:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &value);
        add(L, value);
    }
    
    printf("\n");
    
    int max = find_max(L);
    printf("The maximum value is: %d\n", max);
    
    Node *current = L->first;
    Node *temp;
    
    while (current != NULL) {
        temp = current;
        current = current->next;
        free(temp);
    }
    
    free(L);
    
    return 0;
}
