import os
from constants import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            
            
            if len(content) == MAX_CHARS:
                return content + f' [...File "{file_path}" truncated at 10000 characters]'

            return content

    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
       

    
schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads and returns the content of a file at a given path, relative to the working directory. The content is truncated to a maximum of MAX_CHARS. The operation is constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema( 
                    type=types.Type.STRING,
                    description="The path to the file to read, relative to the working directory.",
                ),
            },
            required=["file_path"], 
        ),
    )