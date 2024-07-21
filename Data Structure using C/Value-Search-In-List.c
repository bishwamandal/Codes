#include <stdio.h>

/**
 * This program allows the user to enter 5 numbers and then searches for a given number in the list.
 * If the number is found, it prints the index at which it is found.
 * If the number is not found, it prints a message indicating that.
 */

int main() {
    int a[5], i, s;
    printf("Enter 5 numbers: ");
    for (i = 0; i < 5; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("Enter a number to search: ");
    scanf("%d", &s);
    for (i = 0; i < 5; i++)
    {
        if (s == a[i])
        {
            break;
        }
    }
    if (i < 5) {
        printf("Number found at index %d\n", i);
    }
    else {
        printf("Number not found.\n");
    }
    return 0;
}