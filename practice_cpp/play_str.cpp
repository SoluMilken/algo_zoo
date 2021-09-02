#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cstring>  // for std::strlen


char* concate_str(char* str1, char* str2)
{
    if ((str1 == NULL) && (str2 != NULL))
    {
        return str2;
    }

    if ((str1 != NULL) && (str2 == NULL))
    {
        return str1;
    }

    if ((str1 == NULL) && (str2 == NULL))
    {
        return NULL;
    }

    unsigned int str1_len, str2_len, total_len;
    int i, j;
    char* new_str;

    str1_len = std::strlen(str1);
    str2_len = std::strlen(str2);

    total_len = str1_len + str2_len - 1;
    new_str = new char[total_len];

    for (i = 0; i < str1_len; i++)
    {
        new_str[i] = str1[i];
    }

    std::cout << new_str << std::endl;

    for (i = 0; i < str2_len; i++)
    {
        j = i + str1_len;
        new_str[j] = str2[i];
    }
    return new_str;

}

int main(void) {
    // char input[80];
    // char copied[80];
    char a1[6] = "12312";
    char a2[4] = "777";
    char* output;

    output = concate_str(a1, a2);
    
    std::cout << output << std::endl;

    // puts("請輸入字串...");
    // fgets(input, sizeof(input) / sizeof(input[0]), stdin);

    // printf("%s\n", input);


    // std::cout << sizeof(input) << std::endl;
    // std::cout << std::strlen(input) << std::endl;

    // strcpy(copied, input);
    // printf("複製整個字串：%s\n", copied);

    // // 重設所有字元為空字元
    // memset(copied, '\0', sizeof(copied));

    // strncpy(copied, input, 4);
    // printf("複製部份字串：%s\n", copied);

    // return 0;
}