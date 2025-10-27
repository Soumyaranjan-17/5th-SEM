#include <stdio.h>

int main() {
int n;
printf("Enter number of processes: ");
scanf("%d", &n);

int at[20], bt[20], ct[20], tat[20], wt[20];
float avgTAT = 0, avgWT = 0;

for (int i = 0; i < n; i++) {
    printf("Enter AT and BT for P%d: ", i + 1);
    scanf("%d%d", &at[i], &bt[i]);
}

int time = 0;
for (int i = 0; i < n; i++) {
    if (time < at[i]) time = at[i]; // wait for process arrival
    ct[i] = time + bt[i];
    time = ct[i];
    tat[i] = ct[i] - at[i];
    wt[i] = tat[i] - bt[i];
    avgTAT += tat[i];
    avgWT += wt[i];
}

printf("\n--- FCFS Scheduling ---\n");
printf("PID\tAT\tBT\tCT\tTAT\tWT\n");
for (int i = 0; i < n; i++) {
    printf("P%d\t%d\t%d\t%d\t%d\t%d\n",
           i + 1, at[i], bt[i], ct[i], tat[i], wt[i]);
}

printf("Average TAT = %.2f\n", avgTAT / n);
printf("Average WT = %.2f\n", avgWT / n);

return 0;
}

// OUTPUT:
// Enter number of processes: 4
// Enter AT and BT for P1: 0 5
// Enter AT and BT for P2: 1 3
// Enter AT and BT for P3: 2 8
// Enter AT and BT for P4: 3 6

// — FCFS Scheduling —
// PID AT BT CT TAT WT
// P1 0 5 5 5 0
// P2 1 3 8 7 4
// P3 2 8 16 14 6
// P4 3 6 22 19 13
// Average TAT = 11.25
// Average WT = 5.75