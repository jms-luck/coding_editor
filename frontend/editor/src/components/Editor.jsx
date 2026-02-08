import Editor from "@monaco-editor/react";

export default function CodeEditor({ code, setCode }) {
  return (
    <Editor
      height="70vh"
      language="python"
      theme="vs-dark"
      value={code}
      onChange={(value) => setCode(value)}
    />
  );
}
