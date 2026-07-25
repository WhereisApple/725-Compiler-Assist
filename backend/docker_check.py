import shutil


def docker_available():

    return shutil.which("docker") is not None