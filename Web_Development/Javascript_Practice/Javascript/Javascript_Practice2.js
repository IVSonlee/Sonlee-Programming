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
    /*Javascript strings are primitive and immutable: All string methods produce a new string without altering the original string.

    String length
    String charAt()
    String charCodeAt()
    String codePointAt()
    String concat()
    String at()
    String [ ]
    String slice()
    String substring()
    String substr()
    String toUpperCase()
    String toLowerCase()
    String isWellFormed()
    String toWellFormed()
    String trim()
    String trimStart()
    String trimEnd()
    String padStart()
    String padEnd()
    String repeat()
    String replace()
    String replaceAll()
    String split() */
    {
        let sample_string1 = "Javascript Length and Extracting String Characters";

        document.getElementById('javascript5').innerHTML = `I will get the length: ${sample_string1.length} and I will be using charAt ${sample_string1.charAt(0)}.Lastly will be charCodeAt: 
        ${sample_string1.charCodeAt(0)}`;
        //The length property returns the length of a string:
        //The charAt() method returns the character at a specified index (position) in a string:
        //The charCodeAt() method returns the code of the character at a specified index in a string:The method returns a UTF-16 code (an integer between 0 and 65535).

        let code_point = `I will get the code point: ${sample_string1.codePointAt(0)} and I will use the method at(): ${sample_string1.at(-3)}`;
        //The at() method is a new addition to JavaScript.It allows the use of negative indexes while charAt() do not.

        document.getElementById('javascript6').innerHTML = code_point;

        let sample_string2 = "I am using an at() method";

        document.getElementById('javascript7').innerHTML = `I am using an at() method again: ${sample_string2.charAt(sample_string2.length - 5)} and a Property access: ${sample_string2[2]}`;
        /*Property access might be a little unpredictable:

        It makes strings look like arrays (but they are not)
        If no character is found, [ ] returns undefined, while charAt() returns an empty string.
        Propert access is read only, but str[0] = "A" gives no error in "sloppy mode". */
    }
    {
        const sample_string4 = "JS String concat()";
        const num = sample_string4.charCodeAt(1);

        document.getElementById('javascript9').innerHTML = sample_string4.concat(" ", num) + "<br>I will be using slice(): " + sample_string4.slice(0,9) + 
        `<br>I will be using slice() in negative index ${sample_string4.slice(-8,-2)} and substring(): ${sample_string4.substring(-3,9)}`;
        //The concat() method can be used instead of the plus operator. 
        //slice() extracts a part of a string and returns the extracted part in a new string.The method takes 2 parameters: start position, and end position (end not included).
        //substring() is similar to slice().The difference is that start and end values less than 0 are treated as 0 in substring().If you omit the second parameter, substring() will slice out the rest of the string.
    }
    {
        let sample_string1 = "JS String Methods";
        let substr1 = sample_string1.substr(3,6);//substr() is similar to slice().The difference is that the second parameter specifies the length of the extracted part.


        document.getElementById('javascript10').innerHTML = "I am using substr(): " + substr1 + " substr() with omitted 2nd parameter: " + sample_string1.substr(10) + 
        `<br>Using toUpperCase(): ${sample_string1.toUpperCase()} <br> Using toLowerCase(): ${sample_string1.toLowerCase()}<br> Using isWellFormed(): ${sample_string1.isWellFormed()}`;
        //If you omit the second parameter, substr() will slice out the rest of the string.If the first parameter is negative, the position counts from the end of the string.
        //A string is converted to upper case with toUpperCase():
        //The isWellFormed() method returns true if a string is well formed.Otherwise it returns false.A string is not well formed if it contains lone surrogates.
        //A lone surrogate is a Unicode surrogate code point that is not part of a valid surrogate pair used to represent characters in UTF-16 encoding.

        let sample_string5 = "          I will be using a lone surrogate \uD500 \uD700         ";
        let get_string_length = sample_string5.length;
        let trim_string = sample_string5.trim();
        let trim_start = sample_string5.trimStart();
        let trim_end = sample_string5.trimEnd();

        document.getElementById('javascript11').innerHTML = `Using a lone toWellFormed(): ${sample_string5.toWellFormed()}.This is the length of the string without trim(): ${get_string_length}` + 
        `<br>After using trim() the length: ${trim_string.length} <br>Using trimStart() this will be the length: ${trim_start.length} for trimEnd() the length: ${trim_end.length}`;
        //The String method toWellFormed() returns a new string where all "lone surrogates" are replaced with the Unicode replacement character (U+FFFD).
        //The trim() method removes whitespace from both sides of a string:
        //ECMAScript 2019 added the String method trimStart() to JavaScript.The trimStart() method works like trim(), but removes whitespace only from the start of a string.
        //The trimEnd() method works like trim(), but removes whitespace only from the end of a string.
    }
    {
        let padstart1 = "10";
        padstart1 = padstart1.padStart(14,"*");//The padStart() method pads a string from the start.It pads a string with another string (multiple times) until it reaches a given length.
        //The padStart() method is a string method.To pad a number, convert the number to a string first.
        
        let padend = "H";
        padend = padend.padEnd(4,"i");//The padEnd() method pads a string from the end.It pads a string with another string (multiple times) until it reaches a given length.

        let repeat = "Javascript Repeat";

        document.getElementById('javascript12').innerHTML = "I am using padstart(): " + padstart1 + `<br>I am using padEnd(): ${padend}` + `<br>I am using a repeat() method: ${repeat.repeat(2)}`;
        /*The repeat() method returns a string with a number of copies of a string.The repeat() method returns a new string.The repeat() method does not change the original string. 
        
        Syntax
        string.repeat(count)*/
    }
    {
        let replacing = document.getElementById('javascript13').innerHTML = "This is a JS replacing() replacing()";
        let replaceall = "HTML CSS Javascript React javascript Javascript";
        
        document.getElementById('javascript13').innerHTML = replacing.replace("replacing()", "replace") + "<br>" + replacing.replace(/REPLACING/i, "replace") + '<br>' 
        + replacing.replace(/replacing()/g, "replace");
        /*The replace() method replaces a specified value with another value in a string:
        By default, the replace() method replaces only the first match:
        By default, the replace() method is case sensitive. Writing MICROSOFT (with upper-case) will not work:
        To replace case insensitive, use a regular expression with an /i flag (insensitive):
        To replace all matches, use a regular expression with a /g flag (global match):*/

        document.getElementById('javascript14').innerHTML = `I will be using replaceAll(): ${replaceall.replaceAll("Javascript", "replaceAll")}`;

        replaceall = replaceall.replaceAll(/Javascript/g, "Global flag");
        replaceall = replaceall.replaceAll(/javascript/g, "Global Flag");/*The replaceAll() method allows you to specify a regular expression instead of a string to be replaced.
        If the parameter is a regular expression, the global flag (g) must be set, otherwise a TypeError is thrown. */

        document.getElementById('javascript15').innerHTML = "replaceAll in global flag" + replaceall;
    }
    {
        const split1 = "I don\'t know what to feel anymore";
        const arr1 = split1.split("");//If the parameter is (""), the returned array will be an array of single characters:
        const arr2 = split1.split(" ");//If the parameter is (" "), the returned array will be an array of words:
        const arr3 = split1.split()//If the separator is omitted, the returned array will contain the whole string in index [0].

        let emojis = "😀😃😄😁😆";

        const segmenter = new Intl.Segmenter("en",{granularity : "grapheme"});//Intl.Segmenter keeps them together safely.
        const arr4 = Array.from(segmenter.segment(emojis)).map(s => s.segment);

        document.getElementById('javascript16').innerHTML = `Javascript String split(): ${JSON.stringify(arr1)} , ${JSON.stringify(arr2)} <br>
        I will be using Intl.Segmenter ${JSON.stringify(arr4)}`;

    }
    {
        let sample1 = "I will be using indexof()";

        document.getElementById('javascript17').innerText = `Using indexOf(): ${sample1.indexOf("indexof")} \n Using lastIndexOf(): ${sample1.lastIndexOf("e",18)}
        \n Using starting position for the search: ${sample1.indexOf("i",4)}`;
        //The indexOf() method returns the index (position) of the first occurrence of a string in a string, or it returns -1 if the string is not found:
        //The lastIndexOf() method returns the index of the last occurrence of a specified text in a string:
        //The lastIndexOf() methods searches backwards (from the end to the beginning), meaning: if the second parameter is 15, the search starts at position 15, and searches to the beginning of the string.
        //Both indexOf(), and lastIndexOf() return -1 if the text is not found:
    }
}