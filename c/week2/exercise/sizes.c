#include <stdio.h>

int main(){
    unsigned char a;
    char b;
    int c;
    unsigned int d;
    long e;
    unsigned long f;
    long long g;
    unsigned long long h;
    float i;
    double j;
    long double k;
    int* l;
    long long* m;
    float* n;
    double* o;

    printf("unsigned char is %zu bytes\n", sizeof(a));
    printf("char is %zu bytes\n", sizeof(b));
    printf("int is %zu bytes\n", sizeof(c));
    printf("unsigned int is %zu bytes\n", sizeof(d));
    printf("long is %zu bytes\n", sizeof(e));
    printf("unsigned long is %zu bytes\n", sizeof(f));
    printf("long long is %zu bytes\n", sizeof(g));
    printf("unsigned long long is %zu bytes\n", sizeof(h));
    printf("float is %zu bytes\n", sizeof(i));
    printf("double is %zu bytes\n", sizeof(j));
    printf("long double is %zu bytes\n", sizeof(k));
    printf("int* is %zu bytes\n", sizeof(l));
    printf("long long* is %zu bytes\n", sizeof(m));
    printf("float* is %zu bytes\n", sizeof(n));
    printf("double* is %zu bytes\n", sizeof(o));

    return 0;
}