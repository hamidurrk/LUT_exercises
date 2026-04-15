#include <stdio.h>
#include <stdlib.h>
#include <semaphore.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>

int main()
{
    int i;
    sem_t *hei = sem_open("/hei", O_CREAT, 0666, 1);
    sem_t *hong = sem_open("/hong", O_CREAT, 0666, 0);

    if (hei == SEM_FAILED || hong == SEM_FAILED) {
        perror("sem_open");
        exit(1);
    }

    for (i = 1; i <= 9; i++) {
        sem_wait(hong);
        printf("Black moves: step %d\n", i);
        fflush(stdout);
        sleep(1);
        sem_post(hei);
    }

    sem_close(hei);
    sem_close(hong);

    return 0;
}