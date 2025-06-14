import os
import datetime

def get_file_metadata(directory):
    """
    Gathers metadata about files in a given directory.
    """
    files_metadata = []
    for filename in os.listdir(directory):
        if filename == "README.md":
            continue
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                stat = os.stat(filepath)
                files_metadata.append({
                    'name': filename,
                    'size': stat.st_size,
                    'modified_time': datetime.datetime.fromtimestamp(stat.st_mtime)
                })
            except OSError as e:
                print(f"Error accessing file {filepath}: {e}")
    return files_metadata

def create_or_update_readme(directory, template):
    """
    Creates or updates the README.md file in a given directory.
    """
    readme_path = os.path.join(directory, "README.md")
    files_metadata = get_file_metadata(directory)

    # Generate the new content for the README
    file_list_str = "\n".join([f"- {meta['name']} (Size: {meta['size']} bytes, Last Modified: {meta['modified_time']:%Y-%m-%d %H:%M:%S})" for meta in files_metadata])
    new_content = template.format(
        directory_name=os.path.basename(directory),
        file_count=len(files_metadata),
        file_list=file_list_str
    )

    if not os.path.exists(readme_path):
        print(f"Creating README.md in {directory}")
        try:
            with open(readme_path, "w") as f:
                f.write(new_content)
        except IOError as e:
            print(f"Error writing to {readme_path}: {e}")
    else:
        try:
            readme_mtime = os.path.getmtime(readme_path)
            should_update = False
            for root, _, files in os.walk(directory):
                for name in files:
                    if name == "README.md":
                        continue
                    file_path = os.path.join(root, name)
                    if os.path.getmtime(file_path) > readme_mtime:
                        should_update = True
                        break
                if should_update:
                    break
            
            if should_update:
                print(f"Updating README.md in {directory}")
                with open(readme_path, "w") as f:
                    f.write(new_content)
        except OSError as e:
            print(f"Error accessing file stats in {directory}: {e}")

def main(root_dir, template):
    """
    Main function to scan directories and manage README.md files.
    """
    print(f"Starting to scan subdirectories in: {root_dir}")
    try:
        for item in os.listdir(root_dir):
            dir_path = os.path.join(root_dir, item)
            if os.path.isdir(dir_path):
                create_or_update_readme(dir_path, template)
    except FileNotFoundError:
        print(f"Error: The root directory '{root_dir}' does not exist.")
    except OSError as e:
        print(f"Error scanning directory {root_dir}: {e}")
    print("Script finished.")

if __name__ == "__main__":
    # Define the root directory to scan. Change this to your target directory.
    # For example: "C:/Users/YourUser/Documents/Projects" or "/home/user/projects"
    ROOT_DIRECTORY = "." 

    # Define your README template.
    # You can use placeholders that will be replaced by the script:
    # {directory_name} - The name of the subdirectory
    # {file_count} - The number of files in the directory (excluding README.md)
    # {file_list} - A list of files and their metadata
    README_TEMPLATE = """
# {directory_name}

This directory contains **{file_count}** files.

## Files

{file_list}

---
*This README was auto-generated.*
"""

    main(ROOT_DIRECTORY, README_TEMPLATE)
