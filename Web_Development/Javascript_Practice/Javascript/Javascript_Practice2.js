function function1()
{
    //A JavaScript string is zero or more characters written inside quotes.
    {
        let single_quotes = 'This is a single quote string';
        let double_quotes = "This is a double quote string";//You can use single or double quotes:
        let template_strings = `This is a "template" string`;//You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
        //Templates were introduced with ES6 (JavaScript 2016).Templates are strings enclosed in backticks (`This is a template string`).Templates allow single and double quotes inside a string:
        let template_string2 = 
        `Template strings allow
        multiple lines this is 
        a sample of it`;//Templates are strings enclosed in backticks (`This is a template string`).Templates allow multiline strings:
        let length_string = single_quotes.length;//To find the length of a string, use the built-in length property:

        document.getElementById('javascript1').innerHTML = single_quotes + ", " + double_quotes + ", " + template_strings + "To find the length of the string: " + //
        length_string + "<br>I'll be using \'single quote\', \"double quote\", \\backslash\\" + 
        "<br>" + template_string2;

        //For readability, programmers often like to avoid long code lines.A safe way to break up a statement is after an operator:

        /*
        Code	Result	Description
        \'	    '	    Single quote
        \"	    "	    Double quote
        \\	    \	    Backslash 
        
        \b	Backspace
        \f	Form Feed
        \n	New Line
        \r	Carriage Return
        \t	Horizontal Tabulator
        \v	Vertical Tabulator*/
    }
    {
        let a = 'This one is a string';
        let b = new String("This one will be an object because of the keyword new");
        let c = new String("Object2");
        //Do not create String objects.The new keyword complicates the code and slows down execution speed.String objects can produce unexpected results:

        document.getElementById('javascript2').innerHTML = typeof(a) + " " + typeof(b) + " Let\'s use the == operator: " + (a==b) + "but if we use ===: " + (a === b) + 
        "<br> I will be using both objects in == operator: " + (b == c) + " for === operator: " + (b===c);
    }
    {
        let word1 = "interpolation";
        let word2 = word1.length;
        let word3 = "JS";

        let num1 = 100;

        let interpolate = `This is a ${word3} ${word1} with a word length of ${word2}`;
        /*Template Strings allow variables in strings.

        Template strings provide an easy way to interpolate variables in strings.

        Syntax
        ${...} */

        let expression_substitution = `\tThis is a expression substitution ${(num1 * (word2 / 4)).toFixed(2)}`;//Template Strings allow interpolation of expressions in strings:

        document.getElementById('javascript3').innerHTML = interpolate + expression_substitution;
    }
    {
        let div1 = "I\'ll be using HTML templates";
        let array1 = ["Index 0",1,2,3,4,true,undefined];

        let html_template = `<h3>${div1}</h3><ul>`;

        for(const loop of array1)
        {
            html_template += `<li>${loop}</li>`;
        }
        html_template += `</ul>`;

        document.getElementById('javascript4').innerHTML = html_template;
    }
}