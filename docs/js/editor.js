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
        return "./monaco/vs/base/worker/workerMain.js";
    }
};

const languageMap = {
    python: "python",
    c: "cpp"
};

function initEditor() {
    require.config({
        paths: {
            vs: "monaco/vs"
        }
    });

    require([
        "vs/editor/editor.main"
    ], function () {
        editor = monaco.editor.create(document.getElementById("editor"), {
            value: templates.python,
            language: languageMap.python,
            theme: "vs-dark",
            automaticLayout: true,
            fontSize: 15,
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            roundedSelection: true,
            wordWrap: "on",
            tabSize: 4
        });

        editor.onDidChangeModelContent(() => {
            if (window.analyzeLiveCode) {
                window.analyzeLiveCode();
            }
        });
    });
}

function changeLanguage(language) {
    if (!editor) return;

    if (!templates[language]) {
        console.error("Template not found:", language);
        return;
    }

    const monacoLanguage = languageMap[language];
    if (!monacoLanguage) {
        console.error("Language not supported:", language);
        return;
    }

    monaco.editor.setModelLanguage(editor.getModel(), monacoLanguage);
    editor.setValue(templates[language]);
}

function getCode() {
    return editor ? editor.getValue() : "";
}

function setCode(code) {
    if (editor) editor.setValue(code);
}