from error_engine import find_error


def explain_error(error, language):

    result = find_error(
        error,
        language
    )


    data = result["message"]


    return f"""

Error Explanation:

{data['explanation']}


Possible Cause:

{data['cause']}


Suggested Fix:

{data['fix']}

"""