PYTHON_ERRORS = {

    "syntaxerror": {

        "explanation":
        "Python couldn't understand your code.",

        "cause":
        "Usually caused by missing brackets, quotes, colons, or incorrect syntax.",

        "fix":
        "Check the line mentioned in the error and correct the syntax.",

        "solution":
        "Review the statement structure and compare it with Python syntax rules."

    },


    "indentationerror": {

        "explanation":
        "Python uses indentation to define code blocks.",

        "cause":
        "Lines inside if, loops, functions, or classes are not aligned correctly.",

        "fix":
        "Make sure all code blocks use consistent indentation.",

        "solution":
        "Use 4 spaces for each indentation level."

    },


    "nameerror": {

        "explanation":
        "A variable or function is being used before it has been defined.",

        "cause":
        "The name may be misspelled or created after it is used.",

        "fix":
        "Create the variable first or check the spelling.",

        "solution":
        "Make sure every variable exists before accessing it."

    },


    "typeerror": {

        "explanation":
        "Python received incompatible data types.",

        "cause":
        "An operation was performed on values that cannot work together.",

        "fix":
        "Convert the values to compatible data types.",

        "solution":
        "Check the types using type() before performing operations."

    },


    "indexerror": {

        "explanation":
        "You tried accessing an element outside a list range.",

        "cause":
        "The requested index does not exist.",

        "fix":
        "Check the list length before accessing an index.",

        "solution":
        "Use valid indexes between 0 and length-1."

    },


    "keyerror": {

        "explanation":
        "The dictionary key does not exist.",

        "cause":
        "The requested key was not found in the dictionary.",

        "fix":
        "Check the key name or use get().",

        "solution":
        "Verify dictionary keys before accessing them."

    },


    "zerodivisionerror": {

        "explanation":
        "Division by zero is not allowed.",

        "cause":
        "A number was divided by 0.",

        "fix":
        "Check the denominator before dividing.",

        "solution":
        "Add a condition to prevent zero division."

    },


    "modulenotfounderror": {

        "explanation":
        "Python cannot find the imported module.",

        "cause":
        "The module may not be installed or the name is incorrect.",

        "fix":
        "Install the module or correct the import statement.",

        "solution":
        "Check your package installation."

    },


    "valueerror": {

        "explanation":
        "The value provided is invalid for the operation.",

        "cause":
        "The data type is correct but the value is not acceptable.",

        "fix":
        "Validate the input before using it.",

        "solution":
        "Add input checks before processing data."

    },


    "was never closed": {

        "explanation":
        "A bracket, parenthesis, or quote was opened but not closed.",

        "cause":
        "Python reached the end while expecting a closing symbol.",

        "fix":
        "Add the missing closing bracket or quote.",

        "solution":
        "Check all (), [], {}, and quotation marks."

    }

}



C_ERRORS = {

    "expected ';'": {

        "explanation":
        "A semicolon is missing at the end of a statement.",

        "cause":
        "C statements usually end with ';'.",

        "fix":
        "Add ';' at the end of the statement.",

        "solution":
        "Check the line before the compiler error."

    },


    "undeclared": {

        "explanation":
        "A variable is being used before declaration.",

        "cause":
        "The compiler does not know the variable type.",

        "fix":
        "Declare the variable before using it.",

        "solution":
        "Define variables near the beginning of the block."

    },


    "segmentation fault": {

        "explanation":
        "The program accessed invalid memory.",

        "cause":
        "Usually caused by invalid pointers or accessing freed memory.",

        "fix":
        "Check pointer values and array boundaries.",

        "solution":
        "Use debugging tools like gdb to locate memory errors."

    },


    "undefined reference": {

        "explanation":
        "The linker cannot find the required function.",

        "cause":
        "A function is missing its implementation or library.",

        "fix":
        "Include the required library or function definition.",

        "solution":
        "Check your header files and compiler flags."

    },


    "expected expression": {

        "explanation":
        "The compiler expected a valid expression.",

        "cause":
        "There is incomplete or incorrect syntax.",

        "fix":
        "Check the statement structure.",

        "solution":
        "Review operators, brackets, and values."

    },


    "redefinition": {

        "explanation":
        "A variable or function has already been declared.",

        "cause":
        "The same name was declared multiple times.",

        "fix":
        "Remove duplicate declarations.",

        "solution":
        "Use unique names or header guards."

    },


    "implicit declaration": {

        "explanation":
        "A function was used without being declared.",

        "cause":
        "The required header file may be missing.",

        "fix":
        "Include the correct header file.",

        "solution":
        "Add the required #include statement."

    }

}