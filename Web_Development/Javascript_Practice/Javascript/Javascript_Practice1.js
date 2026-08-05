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