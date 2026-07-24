const chatMessages =
    document.getElementById("chatMessages");


const chatInput =
    document.getElementById("chatInput");


const sendChat =
    document.getElementById("sendChat");



function addMessage(message, type) {

    const div = document.createElement("div");

    div.className = type + "-message";

    div.innerText = message;


    chatMessages.appendChild(div);


    chatMessages.scrollTop =
        chatMessages.scrollHeight;

}



sendChat.addEventListener(
    "click",
    async () => {


        const message =
            chatInput.value.trim();


        if (message === "")
            return;



        addMessage(
            message,
            "user"
        );


        chatInput.value = "";



        addMessage(
            "Thinking...",
            "bot"
        );



        try {


            const response = await fetch(
                "https://725-compiler-assist-production.up.railway.app/assistant",
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },


                    body: JSON.stringify({

                        code: getCode(),

                        language:
                            document.getElementById("language").value,

                        question: message

                    })

                }
            );



            const data =
                await response.json();



            chatMessages.lastChild.innerText =
                data.answer;



        }

        catch (error) {


            chatMessages.lastChild.innerText =
                "Could not connect to assistant.";

            console.error(error);

        }


    }
);



chatInput.addEventListener(
    "keypress",
    (event) => {

        if (event.key === "Enter") {

            sendChat.click();

        }

    }
);

window.addMessage = addMessage;

async function analyzeCode() {

    const code = getCode();

    const language =
        document.getElementById("language").value;


    if (window.addMessage) {

        window.addMessage(
            "🔍 Analyzing your code...",
            "bot"
        );

    }


    try {


        const response = await fetch(

            "https://725-compiler-assist-production.up.railway.app/analyze",

            {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body: JSON.stringify({

                    code: code,

                    language: language

                })

            }

        );


        const result =
            await response.json();



        if (window.addMessage) {

            window.addMessage(

                "✨ Code Review:\n\n" +
                result.analysis,

                "bot"

            );

        }


    }


    catch (error) {


        console.error(error);


        if (window.addMessage) {

            window.addMessage(

                "⚠️ Analysis failed.",

                "bot"

            );

        }

    }

}


window.analyzeCode = analyzeCode;