import os

def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:

        contents = os.listdir(target_dir)
    
        str_contents = ""
        for obj in contents:
                file_path = os.path.join(target_dir,obj)
                str_contents += f"- {obj}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}\n"
            
        return str_contents
    except Exception as e:
        return f"Error listing files: {e}"
    
               
               
    
       



    
      


    
   
