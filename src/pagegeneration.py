import os
import shutil
from markdownhelper import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = None
    template = None

    if os.path.exists(from_path):
        with open(from_path, 'r') as file:
            markdown = file.read()
    else:
        print(f"Cannot find markdown file at path: {from_path}")
        return None

    if os.path.exists(from_path):
        with open(template_path, 'r') as file:
            template = file.read()
    else:
        print(f"Cannot find template file at path: {template_path}")
        return None
    
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    file_name = os.path.join(dest_path, "index.html")

    with open(file_name, 'w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_contents = None
    if os.path.exists(dir_path_content):
        dir_contents = os.listdir(dir_path_content)
    if dir_contents:
        for item in dir_contents:
            file_path = os.path.join(dir_path_content, item)
            new_dest_path = os.path.join(dest_dir_path, item)
            if os.path.isfile(file_path) and item.endswith(".md"):
                generate_page(file_path, template_path, dest_dir_path, basepath)
            else:
                generate_pages_recursive(file_path, template_path, new_dest_path, basepath)


def copystatic(source, destination):
    if os.path.exists(destination): # clear out destination to make room for new files
        shutil.rmtree(destination)
    os.mkdir(destination)

    source_copy = None
    if os.path.exists(source):     
        source_copy = os.listdir(source)
        for path in source_copy:
            file_path_source = os.path.join(source, path)
            file_path_destination = os.path.join(destination, path)
            if os.path.isfile(file_path_source):
                #print(f"COPYING {file_path_source} TO THE DESTINATION {file_path_destination}") #for debugging
                shutil.copy(file_path_source, file_path_destination)
            else:
                os.mkdir(file_path_destination) # destination may not be availible, create it
                copystatic(file_path_source, file_path_destination) #no files left at this level, we must go deeper