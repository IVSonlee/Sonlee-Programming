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

        arithmetic = arithmetic_arrays[0] + arithmetic_arrays[4] - arithmetic_arrays[2] * arithmetic_arrays[1] / arithmetic_arrays[2] ** arithmetic_arrays[1];/*The numbers (in an arithmetic operation) are 
        called operands.The operation (to be performed between the two operands) is defined by an operator. */
        increment = arithmetic

        increment++;/*The increment operator (++) increments numbers. */

        decrement = increment;
        decrement--;/*The decrement operator (--) decrements numbers. */
    }
    document.getElementById('javascript26').innerHTML = "1 + 5 - 3 * 2 / 3 ** 2 = " + arithmetic + " This one is increment and decrement: " + increment + " and " + decrement;    
}
/*  */