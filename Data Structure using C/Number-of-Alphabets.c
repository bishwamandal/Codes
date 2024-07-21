#include <stdio.h>

/**
 * This program counts the number of alphabets in a given string.
 */

int main() {
    char str[100];
    int i = 0, count = 0;
    printf("Enter a string: ");
    gets(str);
    while (str[i] != '\0') {
        if (str[i] >= 'a' && str[i] <= 'z' || str[i] >= 'A' && str[i] <= 'Z') {
            count++;
        }
        i++;
    }
    printf("Number of alphabets in string is: %d", count);
    return 0;
}