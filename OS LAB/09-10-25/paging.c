#include <stdio.h>

int main() {
    int pageTable[50], n, i, logicalAddr, pageNo, offset, frameNo, physicalAddr;
    int pageSize;

    printf("Enter number of pages: ");
    scanf("%d", &n);
    printf("Enter page size (in bytes): ");
    scanf("%d", &pageSize);

    printf("Enter the page table (frame number for each page):\n");
    for(i = 0; i < n; i++) {
        printf("Page %d → Frame: ", i);
        scanf("%d", &pageTable[i]);
    }

    printf("\nEnter a logical address (page number and offset):\n");
    printf("Page Number: ");
    scanf("%d", &pageNo);
    printf("Offset: ");
    scanf("%d", &offset);

    frameNo = pageTable[pageNo];
    physicalAddr = frameNo * pageSize + offset;

    printf("\nLogical Address → (Page: %d, Offset: %d)", pageNo, offset);
    printf("\nPhysical Address → %d\n", physicalAddr);

    return 0;
}
