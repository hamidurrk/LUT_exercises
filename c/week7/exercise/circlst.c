#include <stdlib.h>

typedef struct Node
{
    int          iData;
    struct Node* pNext;
} Node;

typedef struct
{
    Node*  pHead;
    size_t n;
} CircularList;

void InitList(CircularList* pList)
{
    pList->pHead = NULL;
    pList->n = 0;
}

void FreeList(CircularList* pList)
{
    if (pList->pHead == NULL) {
        return;
    }
    
    Node* current = pList->pHead;
    Node* temp;
    
    do {
        temp = current;
        current = current->pNext;
        free(temp);
    } while (current != pList->pHead);
    
    pList->pHead = NULL;
    pList->n = 0;
}

void InsertEnd(CircularList* pList, const int iValue)
{
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->iData = iValue;
    
    if (pList->pHead == NULL) {
        new_node->pNext = new_node;
        pList->pHead = new_node;
    } else {
        Node* last = pList->pHead;
        while (last->pNext != pList->pHead) {
            last = last->pNext;
        }
        
        last->pNext = new_node;
        new_node->pNext = pList->pHead;
    }
    
    pList->n++;
}

float ComputeAverage(const CircularList* pList)
{
    if (pList->pHead == NULL || pList->n == 0) {
        return 0.0f;
    }
    
    int sum = 0;
    Node* current = pList->pHead;
    
    do {
        sum += current->iData;
        current = current->pNext;
    } while (current != pList->pHead);
    
    return (float)sum / pList->n;
}

size_t DeleteLt(CircularList* pList, const int iValue)
{
    size_t deleted_count = 0;
    
    if (pList->pHead == NULL) {
        return 0;
    }
    
    Node* current = pList->pHead;
    Node* prev = NULL;
    
    Node* last = pList->pHead;
    while (last->pNext != pList->pHead) {
        last = last->pNext;
    }
    
    prev = last;
    
    size_t count = pList->n;
    for (size_t i = 0; i < count; i++) {
        Node* next = current->pNext;
        
        if (current->iData < iValue) {
            if (pList->n == 1) {
                free(current);
                pList->pHead = NULL;
                pList->n = 0;
                return deleted_count + 1;
            }
            
            if (current == pList->pHead) {
                pList->pHead = next;
            }
            
            prev->pNext = next;
            free(current);
            deleted_count++;
            pList->n--;
            current = next;
        } else {
            prev = current;
            current = next;
        }
    }
    
    return deleted_count;
}
