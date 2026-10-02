#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define VM_PAGE 7
#define PM_PAGE 4
#define TOTAL_INSERT 18

typedef struct
{
    int vmn;
    int pmn;
    int exist;
    int time;
} vpage_item;

vpage_item page_table[VM_PAGE];
vpage_item *ppage_bitmap[PM_PAGE];
int vpage_arr[TOTAL_INSERT] = {1, 2, 3, 4, 2, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6};

void init_data()
{
    int i;
    for (i = 0; i < VM_PAGE; i++)
    {
        page_table[i].vmn = i + 1;
        page_table[i].pmn = -1;
        page_table[i].exist = 0;
        page_table[i].time = -1;
    }

    for (i = 0; i < PM_PAGE; i++)
    {
        ppage_bitmap[i] = NULL;
    }
}

void print_frames()
{
    int i;
    printf("Frames: ");
    for (i = 0; i < PM_PAGE; i++)
    {
        if (ppage_bitmap[i] == NULL)
            printf("[ ] ");
        else
            printf("[%d] ", ppage_bitmap[i]->vmn);
    }
    printf("\n");
}

int find_free_frame()
{
    int i;
    for (i = 0; i < PM_PAGE; i++)
    {
        if (ppage_bitmap[i] == NULL)
            return i;
    }
    return -1;
}

void load_page_into_frame(int frame, int vpage_index, int current_time)
{
    ppage_bitmap[frame] = &page_table[vpage_index];
    ppage_bitmap[frame]->exist = 1;
    ppage_bitmap[frame]->pmn = frame;
    ppage_bitmap[frame]->time = current_time;
}

void remove_page_from_frame(int frame)
{
    ppage_bitmap[frame]->exist = 0;
    ppage_bitmap[frame]->pmn = -1;
    ppage_bitmap[frame]->time = -1;
}

void FIFO()
{
    int sum = 0;
    int missing_page_count = 0;
    int current_time = 0;

    printf("\nFIFO page replacement\n");

    while (sum < TOTAL_INSERT)
    {
        int page = vpage_arr[sum];
        int idx = page - 1;

        printf("Access page %d: ", page);

        if (page_table[idx].exist == 0)
        {
            int free_frame = find_free_frame();
            int victim_frame = 0;
            int i;

            missing_page_count++;
            printf("Page fault. ");

            if (free_frame != -1)
            {
                load_page_into_frame(free_frame, idx, current_time);
            }
            else
            {
                int min_time = ppage_bitmap[0]->time;
                for (i = 1; i < PM_PAGE; i++)
                {
                    if (ppage_bitmap[i]->time < min_time)
                    {
                        min_time = ppage_bitmap[i]->time;
                        victim_frame = i;
                    }
                }

                remove_page_from_frame(victim_frame);
                load_page_into_frame(victim_frame, idx, current_time);
            }
        }
        else
        {
            printf("Hit. ");
        }

        print_frames();
        current_time++;
        sum++;
    }

    printf("The number of page faults of FIFO is: %d\n", missing_page_count);
    printf("Page fault rate: %.4f\n", missing_page_count / (float)TOTAL_INSERT);
    printf("The number of replacements: %d\n", missing_page_count > PM_PAGE ? missing_page_count - PM_PAGE : 0);
    printf("Replacement rate: %.4f\n", (missing_page_count > PM_PAGE ? missing_page_count - PM_PAGE : 0) / (float)TOTAL_INSERT);
}

void LRU()
{
    int sum = 0;
    int missing_page_count = 0;
    int current_time = 0;

    printf("\nLRU page replacement\n");

    while (sum < TOTAL_INSERT)
    {
        int page = vpage_arr[sum];
        int idx = page - 1;

        printf("Access page %d: ", page);

        if (page_table[idx].exist == 0)
        {
            int free_frame = find_free_frame();
            int victim_frame = 0;
            int i;

            missing_page_count++;
            printf("Page fault. ");

            if (free_frame != -1)
            {
                load_page_into_frame(free_frame, idx, current_time);
            }
            else
            {
                int min_time = ppage_bitmap[0]->time;
                for (i = 1; i < PM_PAGE; i++)
                {
                    if (ppage_bitmap[i]->time < min_time)
                    {
                        min_time = ppage_bitmap[i]->time;
                        victim_frame = i;
                    }
                }

                remove_page_from_frame(victim_frame);
                load_page_into_frame(victim_frame, idx, current_time);
            }
        }
        else
        {
            printf("Hit. ");
            page_table[idx].time = current_time;
        }

        print_frames();
        current_time++;
        sum++;
    }

    printf("The number of page faults of LRU is: %d\n", missing_page_count);
    printf("Page fault rate: %.4f\n", missing_page_count / (float)TOTAL_INSERT);
    printf("The number of replacements: %d\n", missing_page_count > PM_PAGE ? missing_page_count - PM_PAGE : 0);
    printf("Replacement rate: %.4f\n", (missing_page_count > PM_PAGE ? missing_page_count - PM_PAGE : 0) / (float)TOTAL_INSERT);
}

int next_use_time(int current_index, int vmn)
{
    int i;
    for (i = current_index + 1; i < TOTAL_INSERT; i++)
    {
        if (vpage_arr[i] == vmn)
            return i;
    }
    return 1000000;
}

void OPT()
{
    int sum = 0;
    int missing_page_count = 0;

    printf("\nOPT page replacement\n");

    while (sum < TOTAL_INSERT)
    {
        int page = vpage_arr[sum];
        int idx = page - 1;

        printf("Access page %d: ", page);

        if (page_table[idx].exist == 0)
        {
            int free_frame = find_free_frame();
            int victim_frame = 0;
            int i;

            missing_page_count++;
            printf("Page fault. ");

            if (free_frame != -1)
            {
                load_page_into_frame(free_frame, idx, 0);
            }
            else
            {
                int farthest = next_use_time(sum, ppage_bitmap[0]->vmn);

                for (i = 1; i < PM_PAGE; i++)
                {
                    int t = next_use_time(sum, ppage_bitmap[i]->vmn);
                    if (t > farthest)
                    {
                        farthest = t;
                        victim_frame = i;
                    }
                }

                remove_page_from_frame(victim_frame);
                load_page_into_frame(victim_frame, idx, 0);
            }
        }
        else
        {
            printf("Hit. ");
        }

        print_frames();
        sum++;
    }

    printf("The number of page faults of OPT is: %d\n", missing_page_count);
    printf("Page fault rate: %.4f\n", missing_page_count / (float)TOTAL_INSERT);
    printf("The number of replacements: %d\n", missing_page_count > PM_PAGE ? missing_page_count - PM_PAGE : 0);
    printf("Replacement rate: %.4f\n", (missing_page_count > PM_PAGE ? missing_page_count - PM_PAGE : 0) / (float)TOTAL_INSERT);
}

int main()
{
    int a;
    printf("Please choose page replacement algorithm: 1.FIFO  2.LRU  3.OPT  0.quit\n");

    do
    {
        scanf("%d", &a);
        switch (a)
        {
        case 1:
            init_data();
            FIFO();
            break;
        case 2:
            init_data();
            LRU();
            break;
        case 3:
            init_data();
            OPT();
            break;
        case 0:
            break;
        default:
            printf("Invalid choice\n");
        }
    } while (a != 0);

    return 0;
}