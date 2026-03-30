import os
import shutil

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