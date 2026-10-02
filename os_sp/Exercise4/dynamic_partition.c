#include <stdio.h>
#include <string.h>

#define MAX_FREE 50
#define MAX_JOBS 20
#define MAX_NAME 20

typedef struct {
    int start;
    int size;
} FreeBlock;

typedef struct {
    char name[MAX_NAME];
    int start;
    int size;
    int allocated;
} JobAlloc;

typedef struct {
    FreeBlock free_list[MAX_FREE];
    int free_count;
    JobAlloc jobs[MAX_JOBS];
    int job_count;
} MemoryState;

typedef struct {
    int type;
    char job[MAX_NAME];
    int size;
} Operation;

enum { ALLOCATE = 1, RELEASE = 2 };

void init_state(MemoryState *state) {
    state->free_count = 1;
    state->free_list[0].start = 0;
    state->free_list[0].size = 640;
    state->job_count = 0;
}

int find_job(MemoryState *state, const char *name) {
    int i;
    for (i = 0; i < state->job_count; i++) {
        if (strcmp(state->jobs[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}

int create_job(MemoryState *state, const char *name) {
    int idx = state->job_count;
    strcpy(state->jobs[idx].name, name);
    state->jobs[idx].start = -1;
    state->jobs[idx].size = 0;
    state->jobs[idx].allocated = 0;
    state->job_count++;
    return idx;
}

void print_free_list(MemoryState *state) {
    int i;
    if (state->free_count == 0) {
        printf("Free list: empty\n");
        return;
    }

    printf("Free list:\n");
    for (i = 0; i < state->free_count; i++) {
        printf("  Block %d -> start = %d KB, size = %d KB\n",
               i + 1,
               state->free_list[i].start,
               state->free_list[i].size);
    }
}

void merge_free_blocks(MemoryState *state) {
    int i, j;

    for (i = 0; i < state->free_count - 1; i++) {
        for (j = i + 1; j < state->free_count; j++) {
            if (state->free_list[i].start > state->free_list[j].start) {
                FreeBlock temp = state->free_list[i];
                state->free_list[i] = state->free_list[j];
                state->free_list[j] = temp;
            }
        }
    }

    i = 0;
    while (i < state->free_count - 1) {
        int end_current = state->free_list[i].start + state->free_list[i].size;
        if (end_current == state->free_list[i + 1].start) {
            state->free_list[i].size += state->free_list[i + 1].size;
            for (j = i + 1; j < state->free_count - 1; j++) {
                state->free_list[j] = state->free_list[j + 1];
            }
            state->free_count--;
        } else {
            i++;
        }
    }
}

void insert_free_block(MemoryState *state, int start, int size) {
    state->free_list[state->free_count].start = start;
    state->free_list[state->free_count].size = size;
    state->free_count++;
    merge_free_blocks(state);
}

void allocate_from_block(MemoryState *state, int free_index, const char *job_name, int size) {
    int job_idx = find_job(state, job_name);
    int alloc_start = state->free_list[free_index].start;

    if (job_idx == -1) {
        job_idx = create_job(state, job_name);
    }

    state->jobs[job_idx].start = alloc_start;
    state->jobs[job_idx].size = size;
    state->jobs[job_idx].allocated = 1;

    if (state->free_list[free_index].size == size) {
        int i;
        for (i = free_index; i < state->free_count - 1; i++) {
            state->free_list[i] = state->free_list[i + 1];
        }
        state->free_count--;
    } else {
        state->free_list[free_index].start += size;
        state->free_list[free_index].size -= size;
    }
}

void alloc_first_fit(MemoryState *state, const char *job_name, int size) {
    int i;
    for (i = 0; i < state->free_count; i++) {
        if (state->free_list[i].size >= size) {
            allocate_from_block(state, i, job_name, size);
            printf("%s allocates %d KB successfully\n", job_name, size);
            return;
        }
    }
    printf("%s allocation of %d KB failed\n", job_name, size);
}

void alloc_best_fit(MemoryState *state, const char *job_name, int size) {
    int i;
    int best = -1;

    for (i = 0; i < state->free_count; i++) {
        if (state->free_list[i].size >= size) {
            if (best == -1 ||
                state->free_list[i].size < state->free_list[best].size ||
                (state->free_list[i].size == state->free_list[best].size &&
                 state->free_list[i].start < state->free_list[best].start)) {
                best = i;
            }
        }
    }

    if (best != -1) {
        allocate_from_block(state, best, job_name, size);
        printf("%s allocates %d KB successfully\n", job_name, size);
    } else {
        printf("%s allocation of %d KB failed\n", job_name, size);
    }
}

void release_memory(MemoryState *state, const char *job_name) {
    int idx = find_job(state, job_name);
    if (idx == -1 || state->jobs[idx].allocated == 0) {
        printf("%s release failed\n", job_name);
        return;
    }

    insert_free_block(state, state->jobs[idx].start, state->jobs[idx].size);
    printf("%s releases %d KB successfully\n", job_name, state->jobs[idx].size);

    state->jobs[idx].allocated = 0;
    state->jobs[idx].start = -1;
    state->jobs[idx].size = 0;
}

void simulate(const char *title, int use_best_fit, Operation ops[], int n) {
    MemoryState state;
    int i;

    init_state(&state);

    printf("\n================ %s ================\n", title);
    printf("Initial state:\n");
    print_free_list(&state);

    for (i = 0; i < n; i++) {
        printf("\nStep %d: ", i + 1);
        if (ops[i].type == ALLOCATE) {
            printf("%s applies for %d KB\n", ops[i].job, ops[i].size);
            if (use_best_fit) {
                alloc_best_fit(&state, ops[i].job, ops[i].size);
            } else {
                alloc_first_fit(&state, ops[i].job, ops[i].size);
            }
        } else {
            printf("%s releases %d KB\n", ops[i].job, ops[i].size);
            release_memory(&state, ops[i].job);
        }
        print_free_list(&state);
    }
}

int main() {
    Operation ops[] = {
        {ALLOCATE, "job1", 130},
        {ALLOCATE, "job2", 60},
        {ALLOCATE, "job3", 100},
        {RELEASE,  "job2", 60},
        {ALLOCATE, "job4", 200},
        {RELEASE,  "job3", 100},
        {RELEASE,  "job1", 130},
        {ALLOCATE, "job5", 140},
        {ALLOCATE, "job6", 60},
        {ALLOCATE, "job7", 50},
        {RELEASE,  "job6", 60}
    };

    int n = sizeof(ops) / sizeof(ops[0]);

    simulate("First-Fit", 0, ops, n);
    simulate("Best-Fit", 1, ops, n);

    return 0;
}