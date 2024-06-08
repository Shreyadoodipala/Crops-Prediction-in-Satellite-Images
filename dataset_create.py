import os
import numpy as np
import shutil
import pandas as pd

# Base directory containing subdirectories with npz files (current directory)
base_dir = '.'

# Directory where the selected npz files will be copied to
target_base_dir = 'path/to/dataset'

# List of directories to exclude
exclude_dirs = ['1178', '1181', '1295', '1296', '1300', '1525', '168', '1783', '1855', '1856', '1920', '1923', '1924', '2374', '2377']  

csv_path = 'path/to/sickle_dataset_tabular.csv'
df = pd.read_csv(csv_path)

# Desired array shapes
desired_shapes = [(12, 12), (11, 12), (12, 11)]
desired_labels = ['Banyan', 'Betelwine', 'Blackgram', 'Coconut', 'Cotton', 'Eucalyptus', 'Green gram', 'Groundnut', 'Mixed plantation', 'Palm tree', 'Sesame', 'Sugarcane']

# Ensure the target base directory exists
os.makedirs(target_base_dir, exist_ok=True)

# Function to check if any array in an npz file matches the desired shapes
def has_desired_shape(file_path, shapes):
    npz_file = np.load(file_path)
    for array_name in npz_file.files:
        if npz_file[array_name].shape in shapes:
            return True
    return False

# Traverse the base directory
for index, row in df.iterrows():
    dir_name = str(row['UNIQUE_ID']) 
    crop_name = row['CROP']     
    
    if dir_name in exclude_dirs:
        continue
    
    current_dir = os.path.join(base_dir, dir_name)
    if not os.path.exists(current_dir):
        continue
    
    npz_files = [f for f in os.listdir(current_dir) if f.endswith('.npz')]

    selected_files = []
    for npz_file in npz_files:
        file_path = os.path.join(current_dir, npz_file)
        if has_desired_shape(file_path, desired_shapes):
            selected_files.append(npz_file)

    if selected_files:
        # Create target directory
        target_dir = os.path.join(target_base_dir, os.path.relpath(current_dir, base_dir))
        os.makedirs(target_dir, exist_ok=True)

        # Copy selected files
        for npz_file in selected_files:
            src_path = os.path.join(current_dir, npz_file)
            dst_path = os.path.join(target_dir, npz_file)
            if src_path != dst_path:
                shutil.copy(src_path, dst_path)

print("Files copied successfully.")
