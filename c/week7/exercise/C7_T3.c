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

void print_list(List *L) {
    Node *current = L->first;
    
    while (current != NULL) {
        printf("%d", current->data);
        if (current->next != NULL) {
            printf(" -> ");
        }
        current = current->next;
    }
    printf("\n");
}

void reverse(List *L) {
    Node *prev = NULL;
    Node *current = L->first;
    Node *next = NULL;
    
    Node *old_first = L->first;
    
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    
    L->first = prev;
    L->last = old_first;
}

int main() {
    int n, value;
    
    List *L = (List*)malloc(sizeof(List));
    L->first = NULL;
    L->last = NULL;
    
    printf("Enter the number of integers: ");
    scanf("%d", &n);
    
    printf("Enter %d integers: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &value);
        add(L, value);
    }
    
    printf("\n");
    
    printf("Original list: ");
    print_list(L);
    
    reverse(L);
    
    printf("Reversed list: ");
    print_list(L);
    
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
