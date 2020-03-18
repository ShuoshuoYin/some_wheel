# to store the decision tree generated by tree.py
# using pickle module

import pickle

def store(tree_root, output_file_name):
    obj_string = pickle.dumps(tree_root)
    with open(output_file_name, 'ab') as f:
        f.write(obj_string)
        
def export(file_name):
    with open(file_name, 'rb') as f:
        try:
            obj = pickle.load(f)
            return obj
        except:
            print("wrong when loading obj")
            return None
         
