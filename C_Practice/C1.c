#include<stdio.h>//is a header file library that lets us work with input and output functions, such as printf()
#include<stdbool.h>//In C, the bool type is not a built-in data type, like int or char. It was introduced in C99, and you must import the following header file to use it
#include<string.h>//C also has many useful string functions, which can be used to perform certain operations on strings.To use them, you must include the <string.h> header file in your program

int main() //This is called a function. Any code inside its curly brackets {} will be executed.
{
    printf("Welcome to C Programming\n\n");//printf is a function used to output/print text to the screen
    
    //The newline character (\n) is called an escape sequence, and it forces the cursor to change its position to the beginning of the next line on the screen
    
    printf("This is the second printf statement");

    int a = 2025;//int - stores integers (whole numbers), without decimals, such as 123 or -123

    int b;

    b = 2026;

    float decimal = 100.0;// stores floating point numbers, with decimals, such as 19.99 or -19.99
    
    char letter = 'I';//stores single characters, such as 'a' or 'B'. Characters are surrounded by single quotes

    printf("\n\nMy name is %cverson I created this code at year %d",letter, a);
    /*Format specifiers are used together with the printf() function to tell the compiler what type of data the variable is storing. It is basically a placeholder for the variable value.
    A format specifier starts with a percentage sign %, followed by a character.
    To combine both text and a variable, separate them with a comma inside the printf() function:*/

    printf("\n\n My name is %c%c%c%c%c%c%c and I make this code at year %d", 'I','v','e','r','s','o','n', 2025);
    //You can also just print a value without storing it in a variable, as long as you use the correct format specifier:

    b=2004;//If you assign a new value to an existing variable, it will overwrite the previous value:

    printf("\n\n %d", b);

    b = a;//You can also assign the value of one variable to another

    printf("\n\n %d", b);

    int c;

    c = b;//Or copy values to empty variables:

    printf("\n\n %d", c);

    int sum = a + b + c;//To add a variable to another variable, you can use the + operator:

    printf("\n\nThis is the result of variable sum = %d", sum);

    int d = 10, e = 20, f = 30;//To declare more than one variable of the same type, use a comma-separated list

    printf("\n\n%d", d + e + f);

    d = e = f = 30;//You can also assign the same value to multiple variables of the same type:

    printf("\n\nHere is the result if you assign the same value to multiple variables = %d", d + e + f);

    double decimal2 = 20.00;//Stores fractional numbers, containing one or more decimals. Sufficient for storing 15 decimal digits 8 bytes

    printf("\n\n Here are the format specifiers %lf %c %d %f", decimal2, letter, a, decimal);

    char number1 = 50; //Alternatively, if you are familiar with ASCII, you can use ASCII values to display certain characters.

    printf("\n\nThis is an ASCII value %c", number1);

    double scientific = 10e3;/*you can write very large or very small floating-point numbers using scientific notation.
    This is done using the letter e (or E), which stands for "times 10 to the power of".*/
    float scientific2 = 20e4;

    printf("\n\nThis is the shorter way for writing numbers %lf and %f. While this one is for decimal precision %.2lf", scientific, scientific2, scientific + scientific2);
    //If you want to remove the extra zeros (set decimal precision), you can use a dot (.) followed by a number that specifies how many digits that should be shown after the decimal point:

    printf("\n\nThis is the sizeof the variable that you are using %zu + %zu = %zu", sizeof(scientific), sizeof(scientific2), sizeof(scientific) + sizeof(scientific2));
    //To actually get the size (in bytes) of a data type or variable, use the sizeof operator:
    //Note that we use the %zu format specifier to print the result, instead of %d. This is because the compiler expects the sizeof operator

    float implicit_conversion = 10;//Implicit conversion is done automatically by the compiler when you assign a value of one type to another.

    printf("\n\nThis is a implicit conversion %f", implicit_conversion);

    int explicit_conversion = (int) implicit_conversion;//Explicit conversion is done manually by placing the type in parentheses () in front of the value.

    printf("\n\nThis is a explicit conversion %i", explicit_conversion);

    const int unchangeable = implicit_conversion / explicit_conversion;
    //If you don't want others (or yourself) to change existing variable values, you can use the const keyword. This will declare the variable as "constant", which means unchangeable and read-only:
    //When you declare a constant variable, it must be assigned with a value:

    printf("\n\nThe value will remain unchangeable %i", unchangeable);

    char letter1 = 120, letter2 = 60;

    int add = (int) letter1 + (int) letter2;//+	    Addition	Adds together two values

    printf("\n\nAdd: %i", add);

    int subtract = letter1 - letter2;//-    Subtraction	    Subtracts one value from another

    printf("\nSubtract: %i", subtract);

    printf("\nMultiply: %.2lf", (double) letter1 * (double) letter2);//*	Multiplication	Multiplies two values

    printf("\n\nDivision: %i and here is the remainder %i", letter1 / letter2, letter1 % letter2);
    // /	Division	Divides one value by another
    // %	Modulus	    Returns the division remainder

    float number2 = 30.00;

    printf("\n\nThis is an increment %.2f ", ++number2);//++	Increment	Increases the value of a variable by 1
    printf(" and this one is a decrement %.2f", --number2);//--	Decrement	Decreases the value of a variable by 1

    char assignment_operator = 20;

    assignment_operator +=30;

    printf("\n\nUsing this += operator here is the result = %i", assignment_operator);
    printf("\nHere is the result using -= operator = %i",assignment_operator -= 10);
    printf("\nHere is the result using *= operator = %i",assignment_operator *= 2);
    printf("\nHere is the result using /= operator = %i",assignment_operator /= 2);
    printf("\nHere is the result using modulo operator = %i", assignment_operator %= 2);

    /*Comparison operators are used to compare two values (or variables). This is important in programming, because it helps us to find answers and make decisions.
    The return value of a comparison is either 1 or 0, which means true (1) or false (0).*/

    int num1 = 30, num2 = 30, num3 = 40;

    printf("\n\n%i == %i == %i", num1, num2, num1 == num2);//Returns 1 if the values are equal
    printf("\n%i != %i == %i",num1,num3, num1 != num3);//Returns 1 if the values are not equal
    printf("\n%i > %i == %i",num1 + num2, num2 + num3, num1 + num2 > num2 + num3);//Returns 1 if the first value is greater than the second value
    printf("\n%i < %i == %i",num1 + num2, num2 + num3, num1 + num2 < num2 + num3);//Returns 1 if the first value is less than the second value
    printf("\n%i >= %i == %i",num1 + num3, num2 + num3, num1 + num3 >= num2 + num3);//Returns 1 if the first value is greater than, or equal to, the second value
    printf("\n%i <= %i == %i",num1 + num3, num2 + num1, num1 + num3 <= num2 + num1);//Returns 1 if the first value is less than, or equal to, the second value


    //Logical operators are used to determine the logic between variables or values, by combining multiple conditions:

    printf("\n\nThis is an AND operator %i", num1 == num2 && num2 > num3 && num1 <= num2);//Returns 1 if both statements are true
    printf("\nThis is an OR operator %i", num1 == num2 || num2 > num3 || num1 <= num2);//Returns 1 if one of the statements is true
    printf("\nI used a reverse operator %i", num1 == num2 && !(num2 > num3) && num1 <= num2);//Reverse the result, returns 0 if the result is 1

    bool choice1 = true, choice2 = false;//A boolean variable is declared with the bool keyword and can take the values true or false:
    //1 (or any other number that is not 0) represents true 0 represents false
    //Therefore, you must use the %d format specifier to print a boolean value:

    printf("\n\n%i == %i = %i", choice1, choice2, choice1 == choice2);
    printf("\n%i != %i = %i", choice1, choice2, choice1 != choice2);
    printf("\n\n");

    /*C has the following conditional statements:
    Use if to specify a block of code to be executed, if a specified condition is true  
    Use else to specify a block of code to be executed, if the same condition is false    
    Use else if to specify a new condition to test, if the first condition is false 
    Use switch to specify many alternative blocks of code to be executed*/

    int grade = 92;
    int number3 = 75, number4 = 85, number5 = 95;
    double number6 = 99.9;    

    if(grade >= number3)//Note that if is in lowercase letters. Uppercase letters (If or IF) will generate an error.
    {
        printf("You got a passing grade difference between %i and %i = %i", number3, grade, number3 - grade);

        if (grade >= number3 && grade <= number4)
        {
            printf("\nYour grade is letter C");
        }
        else if (grade >= number4 && grade <= number5)
        {
            printf("\nYour grade is letter B");

            int difference1 = grade - number4, difference2 = number5 - grade;

            (difference1 > difference2) ? printf("\nYour grade is closer to %i", number5) : printf("\nYour grade is close to %i", number4);
        }
        else if (grade >= number5 && grade <= number6)
        {
            printf("\nYour grade is letter A");
        }
        else
        {
            printf("You got an outstanding score");
        }
    }
    else
    {
        printf("You Failed");
    }
    printf("\n\n");

    /*The switch expression is evaluated once
    The value of the expression is compared with the values of each case
    If there is a match, the associated block of code is executed
    The break statement breaks out of the switch block and stops the execution
    The default statement is optional, and specifies some code to run if there is no case match*/

    char day = 'W';

    switch (day)
    {
    case 'M':
        printf("Monday");
        break;
    case 'T':
        printf("Tuesday");
        break;
    case 'W':
        printf("Wednesday");
        break;
    case 'H':
        printf("Thursday");
        break;
    case 'F':
        printf("Friday");
        break;
    case 'S':
        printf("Saturday");
        break;
    case 'U':
        printf("Sunday");
        break;
    
    default:
        printf("Not available");
        break;
    }
    printf("\n\n");

    int row = 1, limit = 5;

    while (row <= limit)//The while loop loops through a block of code as long as a specified condition is true:
    {
        int column = 1;
        while (column <= row)
        {
            printf("%i ", column);
            column++;
        }
        row++;
        printf("\n");
    }

    printf("\n\n");

    /*do {
    // code block to be executed
    }
    while (condition);*/

    int row1 = 1;

    do //
    {
        double column1 = 20.00;
        int col1 = 1;
        do
        {
            printf("%.2lf ", column1);
            column1*=2;
            col1++;
        } while (col1 <= row1);
        row1++;
        printf("\n");
    } while (row1 <= limit);/*The do/while loop is a variant of the while loop. This loop will execute the code block once, 
    before checking if the condition is true, then it will repeat the loop as long as the condition is true.*/

    printf("\n\n");

    /*for (expression 1; expression 2; expression 3) {
    // code block to be executed
    }
    
    Expression 1 is executed (one time) before the execution of the code block.

    Expression 2 defines the condition for executing the code block.

    Expression 3 is executed (every time) after the code block has been executed.*/
    
    for (int a = 1; a <= 10; a++)//When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop:
    {
        int c = 0;
        int d = 1;
        for (int b = 1; b <= a; b++)
        {
            c+=d;
            printf("%i ", c);
            d++;
        }
        printf("\n");
    }

    printf("\n\n");

    for (int a = 1; a <= 10; a++)
    {
        int c = 0;
        int d = 1;
        for (int b = 1; b <= a; b++)
        {
            if (c % 7 == 0 && c > 0)
            {
                break;//The break statement can also be used to jump out of a loop.
            }
            c+=d;
            printf("%i ", c);
            d++;
        }
        printf("\n");
    }

    for (int a = 1; a <= 10; a++)
    {
        int c = 0;
        int d = 1;
        for (int b = 1; b <= a; b++)
        {
            if (c % 2 == 1)
            {
                continue;//The continue statement breaks one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop.
            }
            c+=d;
            printf("%i ", c);
            d++;
        }
        printf("\n");
    }

    float array[] = {0.1,0.15,0.3};/*To create an array, define the data type (like int) and specify the name of the array followed by square brackets [].
    To insert values to it, use a comma-separated list inside curly braces, and make sure all values are of the same data type:*/
    
    printf("\n\nThis is how you can access an array element: %.2f %.2f %.2f", array[0], array[1], array[2]);
    //To access an array element, refer to its index number.Array indexes start with 0: [0] is the first element. [1] is the second element, etc.

    array[1] = 0.13;//To change the value of a specific element, refer to the index number:

    printf("\n\nI change the value of array[1] : %.2f\n\n", array[1]);

    for (int e = 0; e < sizeof(array[2]) - 1; e++)//You can loop through the array elements with the for loop.To get the size of an array, you can use the sizeof operator:
    {
       printf("%.2f ", array[e]);
    }

    char letters[4];

    letters[0] = 'I',letters[1] = 'V', letters[2] = 'E', letters[3] = 'R'; //Another common way to create arrays, is to specify the size of the array, and add elements later:
    //It is important to note that all elements in an array must be of the same data type.

    //A 2D array is also known as a matrix (a table of rows and columns).

    double two_dimension[2][5] = {{1.0,2.5,3.0},{4.5,5.10,6.4}};//The first dimension represents the number of rows, while the second dimension represents the number of columns

    printf("\n\nThis is an example on how to access an element of a 2d array: %.2lf %.2lf %.2lf", two_dimension[0][0],two_dimension[0][1],two_dimension[0][2]);
    //To access an element of a two-dimensional array, you must specify the index number of both the row and column.

    two_dimension[0][1] = 2.0;//To change the value of an element, refer to the index number of the element in each of the dimensions

    printf("\n\nHere I changed the value of the 2d array: %.2lf\n\n", two_dimension[0][1]);

    int loop1[4][5] = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20}};

    int row2 = 0;
    
    while (row2 < sizeof(loop1) / 16 - 1)
    {
        for (int display = 0; display <= 4; display++)
        {
            printf("%i ", loop1[row2][display]);
        }
        row2++;
        printf("\n");
    }
    printf("\n");
    
    char three_dimension[2][3][3] = {{{'I','V','E'},{'R','S','O'},{'N','R','I'}} , {{'C','H','M'},{'O','N','D'},{'L','E','E'}}};
    //Multidimensional arrays are useful when your data is arranged in rows and columns, like a table, grid, or matrix.

    int count = 0;

    for (int g = 0; g <= 1; g++) {
        for (int h = 0; h <= 2; h++) {
            for (int f = 0; f <= 2; f++) {
                count++;

                // Print characters up to current count
                int printed = 0;
                for (int g2 = 0; g2 <= 1; g2++) {
                    for (int h2 = 0; h2 <= 2; h2++) {
                        for (int f2 = 0; f2 <= 2; f2++) {
                            printf("%c", three_dimension[g2][h2][f2]);
                            printed++;
                            if (printed == count)
                                goto next_line;
                        }
                    }
                }

                next_line:
                printf("\n");
            }
        }
    }

        

        //Strings are used for storing text/characters.
        /*Note that you have to use double quotes ("").To output the string, you can use the printf() function together 
        with the format specifier %s to tell C that we are now working with strings*/

    char string[] = "Hello this is a string";

    printf("\n\n%s", string);

    printf("\nThis is an example on accessing an array of a string: %c", string[1]);
        //Since strings are actually arrays in C, you can access a string by referring to its index number inside square brackets [].

    string[1] = 'a';//To change the value of a specific character in a string, refer to the index number, and use single quotes:

    printf("\n%s\n\n", string);

        for (int string_loop = 0; string_loop < sizeof(string) - 1; string_loop++)
        { 
            int string_char = 0;
            while (string_char <= string_loop)
            {
                printf("%c", string[string_char]);
                string_char++;
            }
            printf("\n");
        }
    
    char string_example[] = {'E','X','A','M','P','L','E','2','\0'};//You should also note that you can create a string with a set of characters
    /*Why do we include the \0 character at the end? This is known as the "null terminating character", and must be included when creating strings using this method. 
    It tells C that this is the end of the string.*/

    printf("\n%s", string_example);

    printf("\n\nThis is a single quote \' This is a double quote \" This is a backslash \\ This is a new line \n This is a \t tab lastly this is null \0");
    /*  \'	'	Single quote
        \"	"	Double quote
        \\	\	Backslash
        \n	New Line	
        \t	Tab	
        \0	Null*/

        char string_length[] = "This will measure the string length";
        char string_length2[] = "This will return the memory size";

        printf("\n\n%zu", strlen(string_length));//to get the length of a string, you can use the strlen() function
        printf("\n%zu", sizeof(string_length));/*we used sizeof to get the size of a string/array. Note that sizeof and strlen behaves differently, 
        as sizeof also includes the \0 character when counting*/

        printf("\n\nThis will return the memory size in bytes not the actual string length %zu", sizeof(string_length2));
        //It is also important that you know that sizeof will always return the memory size (in bytes), and not the actual string length:

        char letter3[15] = "Conca", letter4[] = "tenate";

        strcat(letter3,letter4);

        printf("\nI am using string concatenation %s", letter3);//To copy the value of one string to another, you can use the strcpy() function:

        char letter5[4] = "copy";
        char letter6[] = "strcpy";

        strcpy(letter5,letter6);

        printf("\nI will be using a %s", letter5);

        char letter7[] = "compare";
        char letter8[] = "compare";
        char letter9[] = "different";

        printf("\nThis will compare two strings %i, and this will be the result if it is different %i", strcmp(letter7,letter8), strcmp(letter8,letter9));
        //To compare two strings, you can use the strcmp() function.It returns 0 if the two strings are equal, otherwise a value that is not 0:

        

    return 0; //return 0 ends the main() function.
}


/* C is a general-purpose programming language that has been widely used for over 50 years.

C is very powerful; it has been used to develop operating systems, databases, applications, etc.

Every C statement ends with a semicolon ;

Do not forget to add the closing curly bracket } to actually end the main function.

To insert a new line, you can use the \n character:

Single-line comments start with two forward slashes (//).

Any text between // and the end of the line is ignored by the compiler (will not be executed).

Multi-line comments start with /* and ends with */

//Any text between /* and */ will be ignored by the compiler:

/*
Variables are containers for storing data values, like numbers and characters.

To create a variable, specify the type and assign it a value:

Syntax
type variableName = value;

The equal sign is used to assign a value to the variable.

The general rules for naming variables are:

Names can contain letters, digits and underscores
Names must begin with a letter or an underscore (_)
Names are case-sensitive (myVar and myvar are different variables)
Names cannot contain whitespaces or special characters like !, #, %, etc.
Reserved words (such as int) cannot be used as names

int	    2 or 4 bytes	Stores whole numbers, without decimals	                                                                1
float	4 bytes	        Stores fractional numbers, containing one or more decimals. Sufficient for storing 6-7 decimal digits	1.99
double	8 bytes	        Stores fractional numbers, containing one or more decimals. Sufficient for storing 15 decimal digits	1.99
char	1 byte	        Stores a single character/letter/number, or ASCII values	                                            'A'


%d or %i	int	
%f or %F	float	
%lf	double	
%c	char	
%s	Used for strings (text)

assignment operator (=)
Assignment operators are used to assign values to variables.

Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

*/