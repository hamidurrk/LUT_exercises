#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <semaphore.h>
#include <sys/stat.h>

#define BUFFER_SIZE 5
#define NUM_PRODUCERS 2
#define NUM_CONSUMERS 2
#define ITEMS_PER_PRODUCER 5

typedef struct {
    int buffer[BUFFER_SIZE];
    int in;
    int out;
} SharedBuffer;

SharedBuffer *shared;
sem_t *mutex_sem;
sem_t *empty_sem;
sem_t *full_sem;

void producer(int id) {
    int i, item;
    srand(getpid());

    for (i = 1; i <= ITEMS_PER_PRODUCER; i++) {
        item = id * 100 + i;

        sem_wait(empty_sem);
        sem_wait(mutex_sem);

        shared->buffer[shared->in] = item;
        printf("Producer %d produced %d at index %d\n", id, item, shared->in);
        fflush(stdout);
        shared->in = (shared->in + 1) % BUFFER_SIZE;

        sem_post(mutex_sem);
        sem_post(full_sem);

        sleep(rand() % 2 + 1);
    }

    exit(0);
}

void consumer(int id) {
    int item;
    srand(getpid());

    while (1) {
        sem_wait(full_sem);
        sem_wait(mutex_sem);

        item = shared->buffer[shared->out];
        printf("Consumer %d consumed %d from index %d\n", id, item, shared->out);
        fflush(stdout);
        shared->out = (shared->out + 1) % BUFFER_SIZE;

        sem_post(mutex_sem);
        sem_post(empty_sem);

        if (item == -1) {
            break;
        }

        sleep(rand() % 2 + 1);
    }

    exit(0);
}

int main() {
    int i;
    pid_t producers[NUM_PRODUCERS], consumers[NUM_CONSUMERS];
    char mutex_name[64], empty_name[64], full_name[64];

    shared = mmap(NULL, sizeof(SharedBuffer), PROT_READ | PROT_WRITE,
                  MAP_SHARED | MAP_ANONYMOUS, -1, 0);

    shared->in = 0;
    shared->out = 0;

    snprintf(mutex_name, sizeof(mutex_name), "/pc_mutex_%d", getpid());
    snprintf(empty_name, sizeof(empty_name), "/pc_empty_%d", getpid());
    snprintf(full_name, sizeof(full_name), "/pc_full_%d", getpid());

    mutex_sem = sem_open(mutex_name, O_CREAT | O_EXCL, 0666, 1);
    empty_sem = sem_open(empty_name, O_CREAT | O_EXCL, 0666, BUFFER_SIZE);
    full_sem = sem_open(full_name, O_CREAT | O_EXCL, 0666, 0);

    sem_unlink(mutex_name);
    sem_unlink(empty_name);
    sem_unlink(full_name);

    for (i = 0; i < NUM_PRODUCERS; i++) {
        producers[i] = fork();
        if (producers[i] == 0) {
            producer(i + 1);
        }
    }

    for (i = 0; i < NUM_CONSUMERS; i++) {
        consumers[i] = fork();
        if (consumers[i] == 0) {
            consumer(i + 1);
        }
    }

    for (i = 0; i < NUM_PRODUCERS; i++) {
        waitpid(producers[i], NULL, 0);
    }

    for (i = 0; i < NUM_CONSUMERS; i++) {
        sem_wait(empty_sem);
        sem_wait(mutex_sem);

        shared->buffer[shared->in] = -1;
        printf("Parent inserted termination item -1 at index %d\n", shared->in);
        fflush(stdout);
        shared->in = (shared->in + 1) % BUFFER_SIZE;

        sem_post(mutex_sem);
        sem_post(full_sem);
    }

    for (i = 0; i < NUM_CONSUMERS; i++) {
        waitpid(consumers[i], NULL, 0);
    }

    sem_close(mutex_sem);
    sem_close(empty_sem);
    sem_close(full_sem);
    munmap(shared, sizeof(SharedBuffer));

    return 0;
}