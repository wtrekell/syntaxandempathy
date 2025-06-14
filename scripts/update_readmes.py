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


def main():
    """
    Main function to recursively scan ALL subdirectories and manage README.md files.
    """
    # The script now assumes the template file is in the same directory it is.
    script_dir = os.path.dirname(__file__)
    template_path = os.path.join(script_dir, 'readme_template.md')

    try:
        with open(template_path, 'r') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"FATAL: Template file not found at {template_path}")
        return
    
    # We start scanning from the repository root, which is one level above the 'scripts' directory.
    root_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
    print(f"Starting to recursively scan subdirectories in: {root_dir}")

    for dir_path, subdirs, _ in os.walk(root_dir):
        # Prevent descending into .git, .github, and the scripts folder itself.
        subdirs[:] = [d for d in subdirs if d not in ['.git', '.github', 'scripts']]

        if dir_path == root_dir:
            continue

        print(f"--- Processing: {dir_path} ---")
        create_or_update_readme(dir_path, template)
    
    print("Script finished.")


if __name__ == "__main__":
    main()
