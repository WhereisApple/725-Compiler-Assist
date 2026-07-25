import re


def analyze_python(code):

    suggestions = []

    if "#" not in code:
        suggestions.append(
            "Consider adding comments to improve readability."
        )

    if re.search(r"\b[a-zA-Z]\b", code):
        suggestions.append(
            "Use more descriptive variable names instead of single letters."
        )

    if "\t" in code:
        suggestions.append(
            "Use four spaces instead of tabs for indentation."
        )

    if "range(len(" in code:
        suggestions.append(
            "Consider iterating directly over the list instead of using range(len())."
        )

    if code.count("print(") > 5:
        suggestions.append(
            "There are many print statements. Remove debugging prints before finalizing."
        )

    return suggestions


def analyze_c(code):

    suggestions = []

    if "//" not in code and "/*" not in code:
        suggestions.append(
            "Consider adding comments to explain important sections."
        )

    if "scanf(" in code:
        suggestions.append(
            "Check the return value of scanf() for safer input handling."
        )

    if "gets(" in code:
        suggestions.append(
            "Avoid gets(). Use fgets() instead because gets() is unsafe."
        )

    if "malloc(" in code and "free(" not in code:
        suggestions.append(
            "Memory allocated with malloc() should usually be freed."
        )

    if "printf(" in code and "\\n" not in code:
        suggestions.append(
            "Consider ending output with a newline (\\n)."
        )

    return suggestions