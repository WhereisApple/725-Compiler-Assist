from docker_executor import run_in_docker


def run_python(code):

    return run_in_docker(

        "python:3.12",

        "python /code/{filename}",

        code,

        ".py"

    )


def run_c(code):

    return run_in_docker(

        "gcc:latest",

        "gcc /code/{filename} -o /code/program && /code/program",

        code,

        ".c"

    )