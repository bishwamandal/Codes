#include <stdio.h>

/**
 * This program counts the number of vowels in a given string.
 */

int main() {
    char str[100];
    int i = 0, count = 0;
    printf("Enter a string: ");
    gets(str);
    while (str[i] != '\0') {
        if (str[i] == 'a' || str[i] == 'A' || str[i] == 'e' || str[i] == 'E'
            || str[i] == 'i' || str[i] == 'I' || str[i] == 'o' || str[i] == 'O'
            || str[i] == 'u' || str[i] == 'U') {
            count++;
        }
        i++;
    }
    printf("Number of vowels in string is: %d", count);
    return 0;
}