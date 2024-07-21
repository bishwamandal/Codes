#include <stdio.h>
#include <string.h>

/**
 * This program checks whether a given string is a palindrome or not.
 * A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
 * The program takes a string as input, reverses it, and then compares it with the original string.
 * If the reversed string is the same as the original string, it is a palindrome.
 * Otherwise, it is not a palindrome.
 */

int main() {
    char s1[20], s2[20];
    int val;
    
    printf("Enter a string: ");
    gets(s1);
    strcpy(s2, s1);
    strrev(s1);
    printf("Reversed string is: %s\n", s1);

    val = strcmp(s1, s2);
    if (val == 0)
    {
        printf("String is palindrome.\n");
    }
    else
    {
        printf("String is not palindrome.\n");
    }
    return 0;
}