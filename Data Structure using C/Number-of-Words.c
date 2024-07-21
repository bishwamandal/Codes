#include <stdio.h>

/**
 * This program counts the number of words in a given string.
 */

int main() {
    char str[100];
    int i = 0, word = 0;
    printf("Enter a string: ");
    gets(str);
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i]==' ' && str[i+1]!=' ') {
            word++;
        }
    }
    printf("Number of words in string is: %d", word + 1);
    return 0;
}