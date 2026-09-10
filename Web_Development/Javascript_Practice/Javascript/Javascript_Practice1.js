/*External scripts are practical when the same code is used in many different web pages.

JavaScript files have the file extension .js.

To use an external script, put the name of the script file in the src (source) attribute of a <script> tag: 
You can place an external script reference in <head> or <body> as you like.

The script will behave as if it was located exactly where the <script> tag is located.*/

//This is a single line comment
/*This is multiple line comment */
function function3()
{
    document.getElementById('javascript6').style.background = 'rgb(60, 57, 105)';
    document.getElementById('javascript6').style.border = 'none';
    document.getElementById('javascript6').style.color = 'white';
    document.getElementById('javascript6').style.font = '700 16px monospace';
    document.getElementById('javascript6').style.padding = '15px';
}

function function4()
{
    let a = 20;
    let b = 4;
    let A, B, C;
    A = 'Full'; B = 'Stack'; C = A + ' ' + B + '' + ' Web Developer'; /*When separated by semicolons, multiple statements on one line are allowed: */
    let var1 = 2026;
    let var2 = 1;
    var1 = 2027;
    /*Variables are containers for storing data values.Variables must be identified with unique names. */

    let var3 = var1 - var2 /*JavaScript assignment operators (=) assign values to variables: 
    JavaScript uses arithmetic operators ( + - * / ) to compute values:*/

    let c = (a + 10) / b;
    let _underscore;
    const gender = 'Use constant variable if you dont want the value to be changed';//Always use const if the value should not be changed
    
    _underscore = 'Using first the underscore as the variable name is valid';

    document.getElementById('javascript10').innerText = 'Next year will be ' + var1 + ' I made this code at year: ' + var3;
    document.getElementById('javascript11').innerText = '(' + a + ' + ' + '10' + ')' + ' / ' + b + ' = ' + c;/*An expression is a combination of values, variables, and operators, which computes to a value. */
    document.getElementById('javascript12').innerText = 'I will be a ' + C;
    document.getElementById('javascript13').innerText = _underscore + ' and ' + gender;


    d = "20" + 2 + 6;
    e = 20 + 2 + "6";
    //If you put a number in quotes, the rest of the numbers will be treated as strings, and concatenated.

    document.getElementById('javascript14').innerText = '"20" + 2 + 6  = ' + d + ', while 20 + 2 + "6" = ' + e;

    d = 'Hoisting';//Variables defined with var are hoisted to the top and can be initialized at any time.Meaning: You can use the variable before it is declared:

    document.getElementById('javascript16').innerText = d + ': variables defined with var are hoisted to the top and can be initialized at any time.';

    const array1 = [1,2,3,4,5];
    const array2 = {six:6, seven:7, eight:8, nine:9, ten:10};

    array1[0] = 11.0;//You can change the elements of a constant array:
    array2.seven = 14;//You can change the properties of a constant object:

    document.getElementById('javascript17').innerText = 'array1 = ' + array1 + ' array2.seven = ' + array2.seven;
}
/*An identifier is the name you give to a variable.

Rules for identifiers:

Must start with a letter, _, or $
Can contain digits after the first character
Cannot be a reserved keyword (let, const, if, etc.)
Are case-sensitive 

JavaScript identifiers are case sensitive.

The variables lastName and lastname, are different variables:

Hyphens:

first-name, last-name, master-card, inter-city.

Hyphens are not allowed in JavaScript. They are reserved for subtractions.*/

function function5()
{
    let string = "String";//Strings are written with quotes. You can use single or double quotes:
    let number = 21.5;//All JavaScript numbers are stored as decimal numbers (floating point).Numbers can be written with, or without decimals:
    let exponential_notation1 = 5e5;
    let exponential_notation2 = 21e-3;//Extra large or extra small numbers can be written with scientific (exponential) notation:
    let bigint = BigInt(10000000000000);
    let boolean = false;
    let boolean2 = false;//JavaScript booleans can only have one of two values: true or falseThe boolean value of an expression is the basis for JavaScript comparisons.

    const object = {firstname:"Iverson Richmond",lastname:"Lee"};
    const array = [1,2,3,4,5];

    let undefined;//A variable without a value has the datatype undefined.A variable without a value also has the value undefined.
    let not_undefined = "";//An empty value has nothing to do with undefined.An empty string has both a legal value and a type.
    let null1;

    let symbol = Symbol();

    /*A JavaScript variable can hold 8 types of data:

    Type	    Description
    String	    A text of characters enclosed in quotes
    Number	    A number representing a mathematical value
    Bigint	    A number representing a large integer
    Boolean	    A data type representing true or false
    Object	    A collection of key-value pairs of data
    Undefined	A primitive variable with no assigned value
    Null	    A primitive value representing object absence
    Symbol	    A unique and primitive identifier */

    document.getElementById('javascript19').innerHTML = 'Here is the list of variables of every variable being used ' + typeof string + " " + typeof(number) + " " + typeof(bigint) + " " + 
    typeof(undefined) + " " + typeof(null1) ;
    //You can use the JavaScript typeof operator to find the type of a JavaScript variable.The typeof operator returns the type of a variable or an expression:
    document.getElementById('javascript20').innerHTML = (boolean == boolean2);
}

function function6()
{
    let number, number2;

    number = [1e2,2e3,3e4,4e5];

    subtraction_exponentiation = (number[0] ** 2) - 500;

    document.getElementById('javascript21').innerHTML = "Addition: " + number[0] + " + " + number[1] + " = " + (number[0] + number[1]) + " Multiplication " + number[1] + " * " + number[0] + " = " + 
    (number[1] * number[0]);//The Addition Operator (+) adds numbers:The Multiplication Operator (*) multiplies numbers:
    document.getElementById('javascript22').innerText = "Exponentiation and Subtraction: (" + number[0] + " ** 2)  - " + 500 + " = " + subtraction_exponentiation;
    //The subtraction operator (-) subtracts numbers.
    //The exponentiation operator (**) raises the first operand to the power of the second operand.

    /*
    Operator	Description
    +	        Addition
    -	        Subtraction
    *	        Multiplication
    **	        Exponentiation
    /	        Division
    %	        Modulus (Division Remainder)
    ++	        Increment
    --	        Decrement */

    let concatenate = "Concatenated" + " " + "strings"; //The + can also be used to add (concatenate) strings:

    document.getElementById('javascript23').innerText = concatenate += " using + sign" //The += assignment operator can also be used to add (concatenate) strings:
    
    number[0] += number[1];
    number[1] /= number[0];

    document.getElementById('javascript24').innerHTML = "I am using a Assignment Operator for addition and division:" + number[0] + ", " + number[1];

    /*Operator	Example	    Same As
        =	    x = y	    x = y
        +=	    x += y	    x = x + y
        -=	    x -= y	    x = x - y
        *=	    x *= y	    x = x * y
        /=	    x /= y	    x = x / y
        %=	    x %= y	    x = x % y
        **=	    x **= y	    x = x ** y */

    let a = "Comparison";
    var b = "Comparison";
    let value1 = 10;
    let value2 = 20;

    let comparison1 = (a == b) != (value2 > value1);
    {
        var comparison2 = ("Comparison" === b) <= ("A" < "B");
    }

    document.getElementById('javascript25').innerHTML = "Comparison1: " + comparison1 + " Inner Comparison2: " + comparison2;

    /*Operator	    Description	                        Example
        ==	        equal to	                        x == 5
        ===	        equal value and equal type	        x === 5
        !=	        not equal	                        x != 5
        !==	        not equal value or not equal type	x !== 5
        >	        greater than	                    x > 5
        <	        less than	                        x < 5
        >=	        greater than or equal to	        x >= 5
        <=	        less than or equal to	            x <= 5 
        
    Note that strings are compared alphabetically.*/
}
function function7()
{
    {
        var arithmetic_arrays = [1,2,3,4,5];
        var words = ["Front End Developer", "Backend Developer", "Fullstack Web Developer", "Senior Fullstack Web Developer",null,undefined, 0];

        arithmetic = arithmetic_arrays[0] + arithmetic_arrays[4] - arithmetic_arrays[2] * arithmetic_arrays[1] / arithmetic_arrays[2] ** arithmetic_arrays[1];/*The numbers (in an arithmetic operation) are 
        called operands.The operation (to be performed between the two operands) is defined by an operator. */
        increment = arithmetic

        increment++;/*The increment operator (++) increments numbers. */

        decrement = increment;
        decrement--;/*The decrement operator (--) decrements numbers. */
    }
    document.getElementById('javascript26').innerHTML = "1 + 5 - 3 * 2 / 3 ** 2 = " + arithmetic + " This one is increment and decrement: " + increment + " and " + decrement;
    document.getElementById('javascript27').innerHTML = "Lastly I am using Math.pow(x,y): " + Math.pow(arithmetic_arrays[2], arithmetic_arrays[1]);  //x ** y produces the same result as Math.pow(x,y):  

    arithmetic_arrays[4] **= arithmetic_arrays[4];
    arithmetic_arrays[3] /= arithmetic_arrays[1];

    words[0] += " is my first goal";//The Addition Assignment Operator Can also be used to add strings.

    document.getElementById('javascript28').innerHTML = "I am using Exponentiation Assignment Operator: " + arithmetic_arrays[4] + " Division Assignment Operator: " + arithmetic_arrays[3] +
    "Lastly using addition assignment operator for text: " + words[0];
    
    let logical_and1 = words[4] &&= "This will not display unless the first value is True";
    let logical_and2 = words[0] &&= "This is true because its just only an empty string";
    //The Logical AND assignment operator is used between two values.If the first value is true, the second value is assigned.

    let logical_or1 = arithmetic_arrays[0] ||= words[0];
    let logical_or2 = words[6] ||= words[4];
    //The Logical OR assignment operator is used between two values.If the first value is false, the second value is assigned.

    let nullish1 = words[5] ??= "It will display the second value";//If the first value is undefined or null, the second value is assigned.
    let nullish2 = words[6] ??= "It will display the first value";
    
    let spread_sample1 = "76234";
    /*Operator	Example	        Result
        &&=	    true &&= 10	    x = 10
        ||=	    false ||= 10	x = 10
        ??=	    null ??= 10	    x = 10 
        
    The 8 FALSY Values
        false	        The boolean keyword itself
         0	            The number zero
        -0	            Negative zero
        0n	            BigInt zero
        "", '', ``	    Any empty string
        null	        The absence of any value
         undefined	    A variable that has not been assigned a value
        NaN	            "Not-a-Number," usually the result of an invalid math operation
    
        These are TRUTHY

    "0"	    A string containing a zero is truthy because it is not empty
    "false"	The string "false" is truthy
    [ ]	    An empty array is truthy
    { }	    An empty object is truthy*/

    

    let max = Math.max(...spread_sample1);//The ... operator splits iterables into individual elements.

    let comparison1 = "10" < "5";//All the comparison operators above can also be used on strings: Note that strings are compared alphabetically:
    let comparison2 = true === 0;

    /*Comparing Different Types
    Comparing data of different types may give unexpected results.

    When comparing a string with a number, JavaScript will convert the string to a number when doing the comparison. An empty string converts to 0. A non-numeric string converts to NaN which is always false. */

    document.getElementById('javascript29').innerHTML = "I am using Logical AND operator: " + logical_and1 + " and " + logical_and2;
    document.getElementById('javascript30').innerHTML = "I am using Logical OR operator: " + logical_or1 + " and " + logical_or2;
    document.getElementById('javascript31').innerText = "I am using Nullish coalescing operator: " + nullish1 + " and " + nullish2;
    document.getElementById('javascript32').innerHTML = "I am using spread operator: " + max; 
    document.getElementById('javascript33').innerHTML = "I am using Comparison operator: " + comparison1 + " and " + comparison2;
}

function function8()
{
    condition_values = [true,false,null,undefined,"nested if",21]

    if (true !== "Not Equal value and type")
    {
        document.getElementById('javascript34').innerHTML = "I am using an if condition";//Use the JavaScript if statement to execute a block of code when a condition is true.
    }

    let nested_if = condition_values[1] ||= condition_values[4];

    if(condition_values[1] ||= condition_values[4] == "nested if")
    {
        if(typeof(condition_values[4] == typeof("is this a string")))
        document.getElementById('javascript35').innerHTML = "This is a " + nested_if;
    }//You can use an if statement inside another if statement:Nested if statements can make your code more complex.A better solution is to use the logical AND operator:

    if(null === undefined)
    {
        if_else_output = "This will be not executed";
    }
    else
    {
        if_else_output = "I am using a if else statement";
    }//Use the else statement to specify a block of code to be executed if a condition is false.

    document.getElementById('javascript36').innerText = if_else_output;

    let else_if;

    if(condition_values[4] > "not executed")
    {
        else_if = "This will be not executed it will based on the first letter if the same then it will base on the next letter";
    }
    else if(condition_values[4] <= "successful")//Use the else if statement to specify a new condition if the first is false.
    {
        else_if = "This will be executed using else if statement";
    }
    else
    {
        else_if = "This will be not executed";
    }

    document.getElementById('javascript37').innerHTML = else_if;

    var ternary1 = condition_values[0] &&= true ? "I am using ternary operator and it is True" : "Using ternary but its false";
    var ternary2 = false ? "This will not be executed because it is True" : "This will be executed since it False using ternary operator";
    //The conditional operator is a shorthand for writing conditional if...else statements.It is called a ternary operator because it takes three operands.

    /*Parameter	            Description
    condition	            Required.
                            The condition to be tested.
                            An expression that evaluates to true or false.
        ?	                Required.
                            The operator separating the condition from the expressions.
    expression1	            Required.
                            The value to return if the condition is true.
        :	                Required.
                            The operator separating the expressions.
    expression2	            Required.
                            The value to return if the condition is false.*/

    document.getElementById('javascript38').innerHTML = ternary1;
    document.getElementById('javascript39').innerHTML = ternary2;

    
    let day;
    const get_day = new Date().getDay();//The getDay() method returns the weekday as a number between 0 and 6.(Sunday=0, Monday=1, Tuesday=2 ..)

    switch(get_day)
    {
        case 0:
            day = "Sunday";
            break;//When JavaScript reaches a break keyword, it breaks out of the switch block.This will stop the execution inside the switch block.No more statements in the switch block will be executed.
            //It is not necessary to break the last case. The switch ends (breaks) there anyway.
        case 1:
            day = "Monday";
            break;
        case 2:
            day = "Tuesday";
            break;
        case 3:
            day = "Wedndesday";
            break;
        case 4:
            day = "Thursday";
            break;
        case 5:
            day = "Friday";
            break;
        case 6:
            day = "Saturday";
            break;
        default://The default keyword specifies a block of code to run if there is no case match.The default keyword is optional.The default can act as a fallback:
            day = "None of the numbers have a specific day";
    }
    /*Based on a condition, switch selects one or more code blocks to be executed.switch executes the code blocks that matches an expression.
    switch is often used as a more readable alternative to many if...else if...else statements, especially when dealing with multiple possible values. 
    
    The switch expression is evaluated once.
    The value of the expression is compared with the values of each case.
    If there is a match, the associated block of code is executed.
    If there is no match, no code is executed.*/

    document.getElementById('javascript40').innerHTML = "Currently I am using switch statement that determines the day: " + day;

    let val1 = 0;
    val1 += 30;
    let val1_output;

    switch(true)
    {
        case condition_values[2] ||= false == val1 > 31:
        case val1 % 6 == 0:
            val1_output = "This will be executed because two cases are true";
            break;
        case false:
        case true:
            val1_output = "This will be not executed because one is false and the other one is true";
            break;
        default:
            val1_output = "Nothing has matched";
    }

    document.getElementById('javascript41').innerHTML = val1_output;

    let start = 0;
    let count = "";

    while(start <= 10)
    {
        count += start;
        start++;

        if(start == 6)//You can use the Boolean() function to find out if an expression (or a variable) is true:
        {
            break;
        }
    }

    /*Booleans are extensively used in loops to determine conditions for looping.

    Description	    Example
    For loop	    for (i = 0; i < 5; i++)
    While loop	    while (i < 10)
    For in loop	    for (x in person)
    For of loop	    for (x of cars) */
    document.getElementById('javascript42').innerHTML = count;

    let js_logical = ["JS Logical AND", "JS Logical OR", "JS Logical NOT"];

    let js_logical_and, js_logical_or_not;

    if("b" > "a" && 10 === 10)//The && operator returns true if both expressions are true, otherwise false:
    {   
        js_logical_and = "I am using " + js_logical[0];
    }
    document.getElementById('javascript43').innerHTML = js_logical_and;

    var bool2 = false;

    if(bool2 ||= 1 || !(false))//The || operator returns true if one or both expressions are true, otherwise false: The NOT operator (!) returns true for false expressions and false for true expressions.
    {
        js_logical_or_not = "I am using " + js_logical[1] + " and " + js_logical[2];
    }

    document.getElementById('javascript44').innerHTML = js_logical_or_not;

    let nullish_coalescing = undefined ?? "I am using nullish coalescing operator";

    document.getElementById('javascript45').innerHTML = nullish_coalescing;
}