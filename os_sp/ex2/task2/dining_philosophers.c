#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <semaphore.h>
#include <sys/stat.h>

#define N 5
#define ROUNDS 3

sem_t *chopsticks[N];
sem_t *room_sem;

void philosopher(int id) {
    int left = id;
    int right = (id + 1) % N;
    int round;
    srand(getpid());

    for (round = 1; round <= ROUNDS; round++) {
        printf("Philosopher %d is thinking\n", id);
        fflush(stdout);
        sleep(rand() % 2 + 1);

        sem_wait(room_sem);

        sem_wait(chopsticks[left]);
        printf("Philosopher %d picked up left chopstick %d\n", id, left);
        fflush(stdout);

        sem_wait(chopsticks[right]);
        printf("Philosopher %d picked up right chopstick %d\n", id, right);
        fflush(stdout);

        printf("Philosopher %d is eating (round %d)\n", id, round);
        fflush(stdout);
        sleep(rand() % 2 + 1);

        sem_post(chopsticks[right]);
        sem_post(chopsticks[left]);
        sem_post(room_sem);

        printf("Philosopher %d finished eating and released chopsticks\n", id);
        fflush(stdout);
    }

    exit(0);
}

int main() {
    int i;
    pid_t pids[N];
    char room_name[64];
    char chop_name[N][64];

    snprintf(room_name, sizeof(room_name), "/dp_room_%d", getpid());
    room_sem = sem_open(room_name, O_CREAT | O_EXCL, 0666, 4);
    sem_unlink(room_name);

    for (i = 0; i < N; i++) {
        snprintf(chop_name[i], sizeof(chop_name[i]), "/dp_chop_%d_%d", i, getpid());
        chopsticks[i] = sem_open(chop_name[i], O_CREAT | O_EXCL, 0666, 1);
        sem_unlink(chop_name[i]);
    }

    for (i = 0; i < N; i++) {
        pids[i] = fork();
        if (pids[i] == 0) {
            philosopher(i);
        }
    }

    for (i = 0; i < N; i++) {
        waitpid(pids[i], NULL, 0);
    }

    sem_close(room_sem);
    for (i = 0; i < N; i++) {
        sem_close(chopsticks[i]);
    }

    return 0;
}