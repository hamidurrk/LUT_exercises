#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAXJOB 50

typedef struct node
{
    int number;
    int reach_time;
    int need_time;
    int privilege;
    float excellent;
    int start_time;
    int wait_time;
    int visited;
    bool isreached;
} job;

job jobs[MAXJOB];
int quantity;

void initial_jobs()
{
    int i;
    for (i = 0; i < MAXJOB; i++)
    {
        jobs[i].number = 0;
        jobs[i].reach_time = 0;
        jobs[i].need_time = 0;
        jobs[i].privilege = 0;
        jobs[i].excellent = 0;
        jobs[i].start_time = 0;
        jobs[i].wait_time = 0;
        jobs[i].visited = 0;
        jobs[i].isreached = false;
    }
    quantity = 0;
}

void reset_jinfo()
{
    int i;
    for (i = 0; i < quantity; i++)
    {
        jobs[i].excellent = 0;
        jobs[i].start_time = 0;
        jobs[i].wait_time = 0;
        jobs[i].visited = 0;
        jobs[i].isreached = false;
    }
}

void update_reached(int current_time)
{
    int i;
    for (i = 0; i < quantity; i++)
    {
        if (jobs[i].visited == 0 && jobs[i].reach_time <= current_time)
            jobs[i].isreached = true;
        else
            jobs[i].isreached = false;
    }
}

int findminjob(job jobs[], int count)
{
    int minloc = -1;
    int i;
    for (i = 0; i < count; i++)
    {
        if (jobs[i].visited == 0 && jobs[i].isreached)
        {
            if (minloc == -1 || jobs[i].need_time < jobs[minloc].need_time ||
                (jobs[i].need_time == jobs[minloc].need_time && jobs[i].reach_time < jobs[minloc].reach_time))
            {
                minloc = i;
            }
        }
    }
    return minloc;
}

int findrearlyjob(job jobs[], int count)
{
    int rearlyloc = -1;
    int i;
    for (i = 0; i < count; i++)
    {
        if (jobs[i].visited == 0)
        {
            if (rearlyloc == -1 || jobs[i].reach_time < jobs[rearlyloc].reach_time ||
                (jobs[i].reach_time == jobs[rearlyloc].reach_time && jobs[i].number < jobs[rearlyloc].number))
            {
                rearlyloc = i;
            }
        }
    }
    return rearlyloc;
}

int findhrrnjob(job jobs[], int count, int current_time)
{
    int loc = -1;
    int i;
    float best_ratio = -1.0f;
    for (i = 0; i < count; i++)
    {
        if (jobs[i].visited == 0 && jobs[i].isreached)
        {
            float ratio = (float)(current_time - jobs[i].reach_time + jobs[i].need_time) / jobs[i].need_time;
            jobs[i].excellent = ratio;
            if (loc == -1 || ratio > best_ratio ||
                (ratio == best_ratio && jobs[i].reach_time < jobs[loc].reach_time))
            {
                best_ratio = ratio;
                loc = i;
            }
        }
    }
    return loc;
}

int findhighpriorityjob(job jobs[], int count)
{
    int loc = -1;
    int i;
    for (i = 0; i < count; i++)
    {
        if (jobs[i].visited == 0 && jobs[i].isreached)
        {
            if (loc == -1 || jobs[i].privilege > jobs[loc].privilege ||
                (jobs[i].privilege == jobs[loc].privilege && jobs[i].reach_time < jobs[loc].reach_time))
            {
                loc = i;
            }
        }
    }
    return loc;
}

void readJobdata()
{
    FILE *fp;
    char fname[50];
    int i;

    printf("please input job data file name\n");
    scanf("%49s", fname);

    fp = fopen(fname, "r");
    if (fp == NULL)
    {
        printf("error, open file failed\n");
        return;
    }

    while (fscanf(fp, "%d %d %d %d",
                  &jobs[quantity].number,
                  &jobs[quantity].reach_time,
                  &jobs[quantity].need_time,
                  &jobs[quantity].privilege) == 4)
    {
        quantity++;
    }

    fclose(fp);

    printf("\nOriginal job data\n");
    printf("-------------------------------------------------------------\n");
    printf("jobID\tarrival\tneed\tpriority\n");
    for (i = 0; i < quantity; i++)
    {
        printf("%d\t%d\t%d\t%d\n",
               jobs[i].number,
               jobs[i].reach_time,
               jobs[i].need_time,
               jobs[i].privilege);
    }
}

void FCFS()
{
    int i, loc;
    int current_time;
    int total_waittime = 0;
    int total_turnaround = 0;

    loc = findrearlyjob(jobs, quantity);
    current_time = jobs[loc].reach_time;

    printf("\nFCFS result\n");
    printf("---------------------------------------------------------------------\n");
    printf("jobID\tarrival\tneed\tstart\twait\tturnaround\n");

    for (i = 0; i < quantity; i++)
    {
        loc = findrearlyjob(jobs, quantity);

        if (jobs[loc].reach_time > current_time)
            current_time = jobs[loc].reach_time;

        jobs[loc].start_time = current_time;
        jobs[loc].wait_time = jobs[loc].start_time - jobs[loc].reach_time;

        printf("%d\t%d\t%d\t%d\t%d\t%d\n",
               jobs[loc].number,
               jobs[loc].reach_time,
               jobs[loc].need_time,
               jobs[loc].start_time,
               jobs[loc].wait_time,
               jobs[loc].wait_time + jobs[loc].need_time);

        total_waittime += jobs[loc].wait_time;
        total_turnaround += jobs[loc].wait_time + jobs[loc].need_time;

        current_time += jobs[loc].need_time;
        jobs[loc].visited = 1;
    }

    printf("total waiting time: %d\n", total_waittime);
    printf("total turnaround time: %d\n", total_turnaround);
    printf("average waiting time: %.2f\n", (float)total_waittime / quantity);
    printf("average turnaround time: %.2f\n", (float)total_turnaround / quantity);
}

void SJFschdulejob(job jobs[], int count)
{
    int finished = 0;
    int loc;
    int current_time;
    int total_waittime = 0;
    int total_turnaround = 0;

    loc = findrearlyjob(jobs, count);
    current_time = jobs[loc].reach_time;

    printf("\nSJF result\n");
    printf("---------------------------------------------------------------------\n");
    printf("jobID\tarrival\tneed\tstart\twait\tturnaround\n");

    while (finished < count)
    {
        update_reached(current_time);
        loc = findminjob(jobs, count);

        if (loc == -1)
        {
            loc = findrearlyjob(jobs, count);
            current_time = jobs[loc].reach_time;
            update_reached(current_time);
            loc = findminjob(jobs, count);
        }

        jobs[loc].start_time = current_time;
        jobs[loc].wait_time = jobs[loc].start_time - jobs[loc].reach_time;

        printf("%d\t%d\t%d\t%d\t%d\t%d\n",
               jobs[loc].number,
               jobs[loc].reach_time,
               jobs[loc].need_time,
               jobs[loc].start_time,
               jobs[loc].wait_time,
               jobs[loc].wait_time + jobs[loc].need_time);

        total_waittime += jobs[loc].wait_time;
        total_turnaround += jobs[loc].wait_time + jobs[loc].need_time;

        current_time += jobs[loc].need_time;
        jobs[loc].visited = 1;
        finished++;
    }

    printf("total waiting time: %d\n", total_waittime);
    printf("total turnaround time: %d\n", total_turnaround);
    printf("average waiting time: %.2f\n", (float)total_waittime / count);
    printf("average turnaround time: %.2f\n", (float)total_turnaround / count);
}

void HRRFschdulejob()
{
    int finished = 0;
    int loc;
    int current_time;
    int total_waittime = 0;
    int total_turnaround = 0;

    loc = findrearlyjob(jobs, quantity);
    current_time = jobs[loc].reach_time;

    printf("\nHRRN result\n");
    printf("--------------------------------------------------------------------------------\n");
    printf("jobID\tarrival\tneed\tstart\twait\tturnaround\tresponse_ratio\n");

    while (finished < quantity)
    {
        update_reached(current_time);
        loc = findhrrnjob(jobs, quantity, current_time);

        if (loc == -1)
        {
            loc = findrearlyjob(jobs, quantity);
            current_time = jobs[loc].reach_time;
            update_reached(current_time);
            loc = findhrrnjob(jobs, quantity, current_time);
        }

        jobs[loc].start_time = current_time;
        jobs[loc].wait_time = jobs[loc].start_time - jobs[loc].reach_time;
        jobs[loc].excellent = (float)(jobs[loc].wait_time + jobs[loc].need_time) / jobs[loc].need_time;

        printf("%d\t%d\t%d\t%d\t%d\t%d\t\t%.2f\n",
               jobs[loc].number,
               jobs[loc].reach_time,
               jobs[loc].need_time,
               jobs[loc].start_time,
               jobs[loc].wait_time,
               jobs[loc].wait_time + jobs[loc].need_time,
               jobs[loc].excellent);

        total_waittime += jobs[loc].wait_time;
        total_turnaround += jobs[loc].wait_time + jobs[loc].need_time;

        current_time += jobs[loc].need_time;
        jobs[loc].visited = 1;
        finished++;
    }

    printf("total waiting time: %d\n", total_waittime);
    printf("total turnaround time: %d\n", total_turnaround);
    printf("average waiting time: %.2f\n", (float)total_waittime / quantity);
    printf("average turnaround time: %.2f\n", (float)total_turnaround / quantity);
}

void HPF(job jobs[])
{
    int finished = 0;
    int loc;
    int current_time;
    int total_waittime = 0;
    int total_turnaround = 0;

    loc = findrearlyjob(jobs, quantity);
    current_time = jobs[loc].reach_time;

    printf("\nPriority Scheduling result\n");
    printf("---------------------------------------------------------------------\n");
    printf("jobID\tarrival\tneed\tpriority\tstart\twait\tturnaround\n");

    while (finished < quantity)
    {
        update_reached(current_time);
        loc = findhighpriorityjob(jobs, quantity);

        if (loc == -1)
        {
            loc = findrearlyjob(jobs, quantity);
            current_time = jobs[loc].reach_time;
            update_reached(current_time);
            loc = findhighpriorityjob(jobs, quantity);
        }

        jobs[loc].start_time = current_time;
        jobs[loc].wait_time = jobs[loc].start_time - jobs[loc].reach_time;

        printf("%d\t%d\t%d\t%d\t\t%d\t%d\t%d\n",
               jobs[loc].number,
               jobs[loc].reach_time,
               jobs[loc].need_time,
               jobs[loc].privilege,
               jobs[loc].start_time,
               jobs[loc].wait_time,
               jobs[loc].wait_time + jobs[loc].need_time);

        total_waittime += jobs[loc].wait_time;
        total_turnaround += jobs[loc].wait_time + jobs[loc].need_time;

        current_time += jobs[loc].need_time;
        jobs[loc].visited = 1;
        finished++;
    }

    printf("total waiting time: %d\n", total_waittime);
    printf("total turnaround time: %d\n", total_turnaround);
    printf("average waiting time: %.2f\n", (float)total_waittime / quantity);
    printf("average turnaround time: %.2f\n", (float)total_turnaround / quantity);
}

int main()
{
    initial_jobs();
    readJobdata();

    reset_jinfo();
    FCFS();

    reset_jinfo();
    SJFschdulejob(jobs, quantity);

    reset_jinfo();
    HRRFschdulejob();

    reset_jinfo();
    HPF(jobs);

    return 0;
}