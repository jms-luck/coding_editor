import streamlit as st

# Supported languages
languages = {
    "Python": "python",
    "Java": "java",
    "C": "c",
    "C++": "cpp"
}

st.title("Multi-language Code Editor")

# Language selection buttons
selected_lang = st.radio("Select Language", list(languages.keys()), horizontal=True)

# Default code snippets for each language
default_code = {
    "Python": "# Write your Python code here\n",
    "Java": "// Write your Java code here\npublic class Main {\n    public static void main(String[] args) {\n        \n    }\n}",
    "C": "// Write your C code here\n#include <stdio.h>\n\nint main() {\n    \n    return 0;\n}",
    "C++": "// Write your C++ code here\n#include <iostream>\n\nint main() {\n    \n    return 0;\n}"
}

# Code editor
code = st.text_area(
    f"Code Editor ({selected_lang})",
    value=default_code[selected_lang],
    height=300,
    key=selected_lang
)


# Show selected language and code
# st.write(f"**Selected Language:** {selected_lang}")
# st.code(code, language=languages[selected_lang])