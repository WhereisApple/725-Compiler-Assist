window.onload = function () {

    initEditor();

    const language = document.getElementById("language");

    language.addEventListener("change", function () {

        changeLanguage(this.value);

    });

    const buttons = document.querySelectorAll(".toolbar button");

    buttons[0].addEventListener("click", openFile);

    buttons[1].addEventListener("click", downloadCode);

    buttons[2].addEventListener("click", runCode);

    buttons[3].addEventListener("click", stopCode);

};

document
    .getElementById("analyzeBtn")
    .addEventListener(
        "click",
        analyzeCode
    );