import os
import shutil
from markdownhelper import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = None
    template = None
    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    file_name = os.path.join(dest_path, "index.html")

    with open(file_name, 'w') as file:
        file.write(template)


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