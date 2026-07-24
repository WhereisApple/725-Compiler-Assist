from analyzer import explain_error
from suggestions import analyze_python, analyze_c


def generate_response(code, language, question):

    question = question.lower()

    if "explain" in question:

        return (
            "This is a "
            + language
            + " program.\n\n"
            + "I can explain its logic step by step."
        )

    elif "improve" in question or "suggest" in question:

        if language == "python":

            suggestions = analyze_python(code)

        else:

            suggestions = analyze_c(code)

        if not suggestions:

            return "Your code looks good."

        response = "Suggestions:\n\n"

        for item in suggestions:

            response += "• " + item + "\n"

        return response

    else:

        return (
            "Ask me to:\n"
            "- Explain code\n"
            "- Suggest improvements\n"
            "- Explain compiler errors"
        )