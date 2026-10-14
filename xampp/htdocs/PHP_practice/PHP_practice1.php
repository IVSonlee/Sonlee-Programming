<!DOCTYPE html>
<head>

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
    ?>
</body>