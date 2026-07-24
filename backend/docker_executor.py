import subprocess
import tempfile
import os


def run_in_docker(image, command, code, extension):

    try:

        with tempfile.TemporaryDirectory() as temp_dir:

            filename = "main" + extension

            file_path = os.path.join(
                temp_dir,
                filename
            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(code)


            result = subprocess.run(

                [
                    "docker",
                    "run",
                    "--rm",

                    "-v",
                    f"{temp_dir}:/code",

                    image,

                    "sh",
                    "-c",
                    command.format(filename=filename)

                ],

                capture_output=True,

                text=True,

                timeout=60

            )


            return {

                "stdout": result.stdout,

                "stderr": result.stderr

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