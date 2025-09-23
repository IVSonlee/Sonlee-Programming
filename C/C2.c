#include<stdio.h>
#include<string.h>
#include<stdbool.h>

int main()
{
    char fullname[50];// When working with strings in scanf(), you must specify the size of the string/array

    printf("Enter your fullname: ");
    fgets(fullname, sizeof(fullname), stdin);
    /*That's why, when working with strings, we often use the fgets() function to read a line of text. Note that you must include the following arguments: 
    the name of the string variable, sizeof(string_name), and stdin*/

    printf("\nFullname: %s", fullname);

    int password; 

    printf("Enter your password: ");
    scanf("%i",&password);

    printf("\nPassword inserted: %i", password);//To get user input, you can use the scanf() function:
    /*The scanf() function takes two arguments: the format specifier of the variable (%d in the example above) and the reference operator (&myNum), 
    which stores the memory address of the variable.*/

    char middle_initial;
    int age;

    printf("\n\nEnter your middle initial and age: ");
    scanf(" %c %i", &middle_initial, &age);//The scanf() function also allow multiple inputs

    printf("\nYour middle initial is %c and your age is %i and here is the memory address of your middle initial %p and age %p", middle_initial, age,&middle_initial,&age);
        /*When a variable is created in C, a memory address is assigned to the variable.

        The memory address is the location of where the variable is stored on the computer.

        When we assign a value to the variable, it is stored in this memory address.

        To access it, use the reference operator (&), and the result represents where the variable is stored*/

    printf("\n\n");

    /*A pointer is a variable that stores the memory address of another variable as its value.

    A pointer variable points to a data type (like int) of the same type, and is created with the * operator.*/

    int pointer = 30;
    int* pointer2 = &pointer;//Use the & operator to store the memory address
    //A pointer variable points to a data type (like int) of the same type, and is created with the * operator.

    printf("This is in int: %i this one is using a pointer format specifier %p, while the this one will output the memory address with the pointer %p", pointer,pointer,pointer2);

    printf("\n\nThis is a derefercence: %i", *pointer2);//You can also get the value of the variable the pointer points to, by using the * operator (the dereference operator):

    int pointer_array[5] = {1,2,3,4,5};

    int count;

    for (count = 0; count <= sizeof(pointer_array[count] - 1); count++)
    {
        printf("\n%i", &pointer_array[count]);
    }
    
    printf("\n\n%i %i %i\n\n", *pointer_array, *(pointer_array + 1), *(pointer_array + 2));// you can use the * operator to access it:
    //To access the rest of the elements in myNumbers, you can increment the pointer/array (+1, +2, etc)

    char pointer_char[7] = {'P','O','I','N','T','E','R'};

    char* char_address = pointer_char;

    int start = 0;

    while (start < sizeof(pointer_char))
    {
        printf("%c\n",*(pointer_char + start));
        start++;
    }
    
    


    return 0;
}
