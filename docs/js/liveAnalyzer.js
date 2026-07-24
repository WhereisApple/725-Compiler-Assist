function analyzeLiveCode() {

    const code = getCode();

    const language =
        document.getElementById("language").value;


    const warnings = [];


    if (language === "python") {


        const opens =
            (code.match(/[\(\[\{]/g) || []).length;


        const closes =
            (code.match(/[\)\]\}]/g) || []).length;


        if (opens > closes) {

            warnings.push(
                "⚠ Possible missing closing bracket."
            );

        }


        const lines =
            code.split("\n");


        lines.forEach(line => {

            if (
                (
                    line.trim().startsWith("if") ||
                    line.trim().startsWith("for") ||
                    line.trim().startsWith("while") ||
                    line.trim().startsWith("def")
                )
                &&
                !line.includes(":")
            ) {

                warnings.push(
                    "⚠ Missing ':' after statement."
                );

            }

        });



        if (code.trim() === "") {

            warnings.push(
                "⚠ Editor is empty."
            );

        }

    }



    if (language === "c") {


        if (
            code.includes("printf") &&
            !code.includes("#include")
        ) {

            warnings.push(
                "⚠ printf used without stdio.h."
            );

        }


        const opens =
            (code.match(/\{/g) || []).length;


        const closes =
            (code.match(/\}/g) || []).length;


        if (opens !== closes) {

            warnings.push(
                "⚠ Missing closing curly bracket."
            );

        }

    }



    updateWarnings(warnings);

}

function updateWarnings(warnings) {


    const panel =
        document.getElementById(
            "liveWarnings"
        );

    if (warnings.length === 0) {

        panel.innerText =
            "✓ No warnings";

        return;

    }


    panel.innerText =
        warnings.join("\n");

}