function openFile() {

    const input = document.createElement("input");

    input.type = "file";

    input.accept = ".py,.c,.txt";

    input.onchange = function (event) {

        const file = event.target.files[0];

        if (!file) return;

        const reader = new FileReader();

        reader.onload = function (e) {

            setCode(e.target.result);

            if (file.name.endsWith(".py")) {

                document.getElementById("language").value = "python";
                changeLanguage("python");
                setCode(e.target.result);

            }

            else if (file.name.endsWith(".c")) {

                document.getElementById("language").value = "c";
                changeLanguage("c");
                setCode(e.target.result);

            }

        };

        reader.readAsText(file);

    };

    input.click();

}


function downloadCode() {

    const language =
        document.getElementById("language").value;

    const extension =
        language === "python" ? "py" : "c";

    const filename =
        "program." + extension;

    const blob = new Blob(
        [getCode()],
        { type: "text/plain" }
    );

    const url =
        URL.createObjectURL(blob);

    const link =
        document.createElement("a");

    link.href = url;

    link.download = filename;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);

}