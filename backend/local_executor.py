import subprocess
import tempfile
import shutil
import os


def run_python_local(code):

    if shutil.which("python3") is None:

        return {
            "stdout": "",
            "stderr": "Python interpreter is not installed on this server."
        }

    with tempfile.NamedTemporaryFile(
        suffix=".py",
        delete=False,
        mode="w"
    ) as file:

        file.write(code)
        filename = file.name

    try:

        result = subprocess.run(

            ["python3", filename],

            capture_output=True,

            text=True,

            timeout=5

        )

        return {

            "stdout": result.stdout,

            "stderr": result.stderr

        }

    except subprocess.TimeoutExpired:

        return {

            "stdout": "",

            "stderr": "Execution timed out (5 seconds)."

        }

    except Exception as e:

        return {

            "stdout": "",

            "stderr": str(e)

        }

    finally:

        if os.path.exists(filename):
            os.remove(filename)



def run_c_local(code):

    if shutil.which("gcc") is None:

        return {

            "stdout": "",

            "stderr": "C compiler (gcc) is not installed on this server."

        }

    with tempfile.TemporaryDirectory() as temp:

        source = os.path.join(temp, "main.c")

        executable = os.path.join(temp, "program")

        with open(source, "w") as file:

            file.write(code)

        try:

            compile_result = subprocess.run(

                ["gcc", source, "-o", executable],

                capture_output=True,

                text=True,

                timeout=10

            )

            if compile_result.returncode != 0:

                return {

                    "stdout": "",

                    "stderr": compile_result.stderr

                }

            run_result = subprocess.run(

                [executable],

                capture_output=True,

                text=True,

                timeout=5

            )

            return {

                "stdout": run_result.stdout,

                "stderr": run_result.stderr

            }

        except subprocess.TimeoutExpired:

            return {

                "stdout": "",

                "stderr": "Execution timed out."

            }

        except Exception as e:

            return {

                "stdout": "",

                "stderr": str(e)

            }