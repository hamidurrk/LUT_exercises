#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} Node;

typedef struct {
    Node *front;
    Node *rear;
} Queue;

int is_empty(Queue *q) {
    return q->front == NULL;
}

void enqueue(Queue *q, int value) {
    Node *new_node = (Node*)malloc(sizeof(Node));
    new_node->data = value;
    new_node->next = NULL;
    
    if (is_empty(q)) {
        q->front = new_node;
        q->rear = new_node;
    } else {
        q->rear->next = new_node;
        q->rear = new_node;
    }
    
    printf("Enqueued: %d\n", value);
}

int dequeue(Queue *q) {
    if (is_empty(q)) {
        printf("Queue is empty!\n");
        return -1;
    }
    
    Node *temp = q->front;
    int value = temp->data;
    
    q->front = q->front->next;
    
    if (q->front == NULL) {
        q->rear = NULL;
    }
    
    free(temp);
    printf("Dequeued: %d\n", value);
    
    return value;
}

void print_queue(Queue *q) {
    if (is_empty(q)) {
        printf("Queue is empty!\n");
        return;
    }
    
    printf("Queue: ");
    Node *current = q->front;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

void free_queue(Queue *q) {
    Node *current = q->front;
    Node *temp;
    
    while (current != NULL) {
        temp = current;
        current = current->next;
        free(temp);
    }
}

int main() {
    Queue *q = (Queue*)malloc(sizeof(Queue));
    q->front = NULL;
    q->rear = NULL;
    
    int choice, value;
    
    while (1) {
        printf("Menu:\n");
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Print Queue\n");
        printf("4. Quit\n");
        printf("Choose an option: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                enqueue(q, value);
                break;
            case 2:
                dequeue(q);
                break;
            case 3:
                print_queue(q);
                break;
            case 4:
                printf("Exiting program.\n");
                free_queue(q);
                free(q);
                return 0;
            default:
                printf("Invalid option!\n");
        }
    }
    
    return 0;
}
