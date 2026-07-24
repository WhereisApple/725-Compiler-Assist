from error_db import PYTHON_ERRORS, C_ERRORS


def find_error(error, language):

    error = error.lower()


    if language.lower() == "c":

        database = C_ERRORS

    else:

        database = PYTHON_ERRORS



    # Check more specific errors first
    # Example:
    # "was never closed" before "syntaxerror"

    sorted_errors = sorted(
        database.items(),
        key=lambda item: len(item[0]),
        reverse=True
    )



    for key, data in sorted_errors:

        if key in error:

            return {

                "matched": True,

                "message": data

            }



    return {

        "matched": False,

        "message": {

            "explanation":
            "Unknown compiler error.",

            "cause":
            "The error is not available in the current error database.",

            "fix":
            "Check the compiler output and review the code near the reported line.",

            "solution":
            "Add this error pattern to improve future suggestions."

        }

    }