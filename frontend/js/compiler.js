async function runCode() {

    const code = getCode();

    const language =
        document.getElementById("language").value;


    const outputPanel =
        document.querySelector(".output .panel-content");


    outputPanel.innerText = "Running...";


    try {


        const response = await fetch(

            "http://725-compiler-assist-production.up.railway.app/run",

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    language: language,

                    code: code

                })

            }

        );


        const result =
            await response.json();




        if (result.stderr && result.stderr.trim() !== "") {


            outputPanel.innerText =
                result.stderr;



            const errorResponse =
                await fetch(

                    "http://725-compiler-assist-production.up.railway.app/explain_error",

                    {

                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json"

                        },


                        body: JSON.stringify({

                            error: result.stderr,

                            language: language

                        })

                    }

                );



            const explanation =
                await errorResponse.json();



            if (window.addMessage) {

                window.addMessage(

                    "🔴 Compiler Error Explanation:\n\n" +
                    explanation.explanation,

                    "bot"

                );

            }


        }

        else {


            outputPanel.innerText =
                result.stdout;


            if (window.addMessage) {

                window.addMessage(

                    "✅ Program executed successfully.",

                    "bot"

                );

            }

        }



    } catch (error) {


        console.error(error);


        outputPanel.innerText =
            "Backend connection failed.";


        if (window.addMessage) {

            window.addMessage(

                "⚠️ Cannot connect to compiler backend.",

                "bot"

            );

        }

    }

}



function stopCode() {

    console.log(
        "Stop will be added later."
    );

}