<!DOCTYPE html>
<head>
    <style>
        body
        {
            background-color: rgb(150, 150, 180);
        }
    </style>
</head>
<body>
    <?php 
       echo phpversion();//To check your php version you can use the phpversion() function:
       
       /*A PHP script is executed on the server, and the plain HTML result is sent back to the browser.A PHP script can be placed anywhere in the document.
        A PHP script starts with </??>:The default file extension for PHP files is .php.A PHP file normally contains some HTML tags and some PHP scripting code.*/

        echo "<br>This is an echo function<br>";//echo function to output some text on a web page:

        ECHO "PHP keywords(if,else,echo,etc), classes, functions, and user defined fucntions are not case sensitive";

        $language = "PHP";
        $Language = "php";
        echo "<br><br>Variable names are case sensitive $language and $Language are different";//all variable names are case-sensitive!

        #This one also is a single line comment

        /*Variables are "containers" for storing information.

        A variable can have a short name (like $x and $y) or a more descriptive name ($age, $carname, $total_volume).

        Rules for PHP variables:

        A variable must start with the $ sign, followed by the name of the variable
        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive ($age and $AGE are two different variables) */

        echo "<br><br>Output variables using " . $language . " language";

        $value1 = 20;
        $value2 = 10;

        echo "<br>Output using the sum of two variables: ". $value1 + $value2 . "<br><br>";

        /*PHP supports the following data types:

        string (text values)
        int (whole numbers)
        float (decimal numbers)
        bool (true or false)
        array (multiple values)
        object (stores data as objects)
        null (empty variable)
        resource (references external resources)
        mixed (any value) */

        var_dump(21);
        var_dump("Iverson");
        var_dump(21.00);
        var_dump(false);
        var_dump([10,14,2026]);
        var_dump(NULL);

        $a = $b = $c = $language;

        echo "<br><br>Assign Multiple Values: $a $b $c";

        /*PHP variables can be declared anywhere in the PHP code.

        The scope of a variable is the part of the script where the variable can be referenced/used.

        PHP has three different variable scopes:

        global
        local
        static */

        $global_var = "This is a global variable<br>";#A variable declared outside a function has a GLOBAL SCOPE and can only be accessed outside a function:

        function function_local()
        {
            $local_var = "<br>This will be only accessed inside<br>";
            echo $local_var;
        }
        function_local();/*A variable declared within a function has a LOCAL SCOPE and can only be accessed within that function.Local variables are created when the 
        function is called and are destroyed when the function finishes executing */

        echo $global_var;

        function function_static()
        {
            $array1 = [1,2,3,4,5];
            static $static_var = 0;
            $compute = $static_var + $array1[$static_var];
            $static_var++;
            echo "This is a static scope: ". $compute . "<br>";
        }
        function_static();
        function_static();
        function_static();

        /*Normally, when a function finishes executing, all of its variables are deleted. However, sometimes we want a local variable NOT to be deleted. We need it for a 
        further job. To achieve this, use the static keyword when you first declare the variable.Then, each time the function is called, that variable will have the value 
        from the last time the function was called.Note: The variable is still local to the function. */

        function function2()
        {
            global $value1, $value2;#The global keyword is used to access a global variable from within a function.To do this, use the global keyword before the variables (inside the function):
            $value2 = ($value1 - $value2) - 5;
        }
        function2();

        echo "<br>Using a global keyword to access a global variable within a function: $value2 <br>";

        $value3 = 30;
        $value4 = 40;

        function function3()
        {
            $GLOBALS['value2'] = ($GLOBALS['value4'] - $GLOBALS['value3']) - $GLOBALS['value2'];/*PHP also stores all global variables in an array called $GLOBALS[index]. The index holds the name of the variable. 
            This array is also accessible from within functions and can be used to update global variables directly. */
        }
        function3();

        echo "Using GLOBALS Superglobal (value4 - value3) - value2 = $value2 <br><br>";

        /*With PHP, there are two basic ways to output data to the screen: echo and print.

        The differences are small:

        echo has no return value, while print has a return value of 1 so it can be used in expressions
        echo can take multiple parameters, while print can take only one argument
        echo is marginally faster than print */

        $programming_language = ["HTML","CSS","Javascript","Python","PHP","MySQL"];

        echo ("Echo can be used with or without parenthesis<br> <b>I am using a HTML markup language here using bold</b>"); #The echo function can be used with or without parentheses: echo or echo().
        #The following example shows how to output text with the echo command (notice that the text can contain HTML markup)

        echo "<br><br>Difference using double and single quotes \t\$\" $programming_language[0]";
        echo '<br>\\If I use single quotes I cannot insert the variable inside this string and it only support few escape characters \'\\ '. $programming_language[0];

        /*Strings are surrounded by quotes, but there is a difference between single and double quotes in PHP.When using double quotes, variables can be inserted to the string as in the example above.
        When using single quotes, variables have to be inserted using the . operator, like this: 
        
        Differences between Single and Double Quotes
        Feature	                    Single Quotes	                                            Double Quotes
        Variable interpolation	    No - variables like $x are output literally	                Yes - variables are replaced with their values
        Escape sequences	        Only \' and \\ are supported	                            Supports many, like: \n, \t, \r, \$, \"
        Performance	                Slightly faster (PHP does not need to parse the content)	Slightly slower (PHP must scan for variables and escape sequences)
        Readability	                Cleaner for simple, constant strings	                    More readable for strings with many variables (do not need to use the concatenation operator (.))*/

        echo "<br><br>";

        $changing_value = "Changing Value";
        var_dump($changing_value);

        echo "<br>";

        $changing_value = true;
        var_dump($changing_value);

        echo "<br>";

        $changing_value = (string) $changing_value;#If you want to change the data type of an existing variable, but not by changing the value, you can use casting.Casting allows you to change data type on variables
        var_dump($changing_value);

        echo "<br><br>I am using a strlen() function: ". strlen($programming_language[1]);
        echo "<br>I am using a str_word_count() function: ". str_word_count("This is a word count");

        $string1 = "Using str_contains()";
        echo '<br>I am using a str_contains to check for a specific substring: ';

        var_dump(str_contains($string1,"r"));/*The str_contains() function checks if a string contains a specific substring.Tip: The str_contains() function is only available in PHP 8.0 and later. For older 
        versions, use the strpos() function.If a match is found, the function returns a boolean true. If no match is found, it will return a boolean false. */

        echo '<br>I will be using strpos() function: '. strpos($string1,"contains");

    ?>
</body>