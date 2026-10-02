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

    for (i = 1; i <= 10; i++) {
        sem_wait(hei);
        printf("Red moves: step %d\n", i);
        fflush(stdout);
        sleep(1);

        if (i == 10) {
            printf("Red wins. Black loses.\n");
            fflush(stdout);
            break;
        }

        sem_post(hong);
    }

    sem_close(hei);
    sem_close(hong);
    sem_unlink("/hei");
    sem_unlink("/hong");

    return 0;
}