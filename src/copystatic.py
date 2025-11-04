import os
import shutil

def copystatic(source_dir, destination_dir, initial=True):
    #print(f"source: {source_dir}, dest: {destination_dir}")

    if initial and os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    
    source_files = os.listdir(source_dir)
    #print(source_files)
    for file in source_files:
        file_path_src = os.path.join(source_dir, file)
        file_path_dst = os.path.join(destination_dir, file)
        #print(f"path src: {file_path_src}, path dst: {file_path_dst}, dst dir: {destination_dir}")
        if os.path.isfile(file_path_src):
            #print(file_path_src)
            shutil.copy(file_path_src, destination_dir)
        else:
            copystatic(file_path_src, file_path_dst, False)