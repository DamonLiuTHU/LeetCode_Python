import os
import os.path as osp
from shutil import copyfile


root_dir = './imgs'

def dfs(root_dir):
    for files in os.listdir(root_dir):
        abs_path = osp.join(root_dir,files)
        if osp.isdir(abs_path):
            dfs(abs_path)
        elif abs_path.endwith('jpg') and 'example' in abs_path:
            copyfile(abs_path, './examples')


dfs(root_dir)