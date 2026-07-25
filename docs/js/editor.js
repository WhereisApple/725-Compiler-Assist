let editor;

const templates = {

    python: `print("Welcome to 725 Compiler Assist!")`,

    c: `#include <stdio.h>

int main()
{
    printf("Welcome to 725 Compiler Assist!");
    return 0;
}`

};

self.MonacoEnvironment = {
    getWorkerUrl: function () {
        return "monaco/vs/base/worker/workerMain.js";
    }
};


function initEditor() {

    require.config({
        paths: {
            vs: "monaco/vs"
        }
    });


    require(["vs/editor/editor.main"], function () {

        editor = monaco.editor.create(

            document.getElementById("editor"),

            {

                value: templates.python,

                language: "python",

                theme: "vs-dark",

                automaticLayout: true,

                fontSize: 15,

                minimap: {

                    enabled: false

                },

                scrollBeyondLastLine: false,

                roundedSelection: true,

                wordWrap: "on",

                tabSize: 4

            }

        );


        editor.onDidChangeModelContent(() => {

            if (window.analyzeLiveCode) {

                window.analyzeLiveCode();

            }

        });

    });

}


function changeLanguage(language) {

    if (!editor) return;

    monaco.editor.setModelLanguage(

        editor.getModel(),

        language

    );

    editor.setValue(

        templates[language]

    );

}


function getCode() {

    if (!editor) return "";

    return editor.getValue();

}


function setCode(code) {

    if (!editor) return;

    editor.setValue(code);

}