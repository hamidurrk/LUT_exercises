#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[50];
    float score;
} Student;

float average(Student** students, size_t n) {
    float sum = 0.0;
    for (size_t i = 0; i < n; i++) {
        sum += students[i]->score;
    }
    return sum / n;
}

int main() {
    int num_students;
    
    printf("Enter the number of students: ");
    scanf("%d", &num_students);
    
    Student** students = (Student**)malloc(num_students * sizeof(Student*));
    
    for (int i = 0; i < num_students; i++) {
        Student *new_student = (Student*)malloc(sizeof(Student));
        
        printf("Enter name for student %d: ", i + 1);
        scanf("%s", new_student->name);
        
        printf("Enter score for student %d: ", i + 1);
        scanf("%f", &new_student->score);
        
        students[i] = new_student;
    }
    
    printf("\n");
    
    float avg = average(students, num_students);
    printf("The average score of %d students is: %.2f\n", num_students, avg);
    
    for (int i = 0; i < num_students; i++) {
        free(students[i]);
    }
    free(students);
    
    return 0;
}
