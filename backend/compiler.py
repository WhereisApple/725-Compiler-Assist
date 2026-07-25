from docker_executor import run_python, run_c
from local_executor import run_python_local, run_c_local
from docker_check import docker_available


def run_python_code(code):

    if docker_available():

        return run_python(code)

    return run_python_local(code)


def run_c_code(code):

    if docker_available():

        return run_c(code)

    return run_c_local(code)