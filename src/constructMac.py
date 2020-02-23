
import os

def walkFile(file):
    pdbPaths = []
    macPaths = []
    for root, dirs, files in os.walk(file):
         for f in files:
            pdbPaths.append(os.path.join(root, f))
            macPaths.append(os.path.join(root, (f.split("."))[-2] + ".mac"))
    return pdbPaths, macPaths

S_protein = "/Users/csx/Downloads/bioInfo/pdbs/Sprotein/01.pdb"
save_path = "/Users/csx/Downloads/bioInfo/pdbs"

str = """open_receptor %s
open_ligand %s
display_hetero 0
cull_solvent
activate_docking
save_range 1 %s test pdb
button_active 1
translate 0.001 0.000
button_pick 1 30.0000 133.0000
button_active 0"""


pdbPath = "/Users/csx/Downloads/bioInfo/pdbs/ACE2"

pdbPaths,macPaths = walkFile(pdbPath)

for idx,pdbPath in enumerate(pdbPaths):
    macPath = macPaths[idx]
    macContent = str%(pdbPath, S_protein, save_path)
    with open(macPath, 'w') as file_object:
        file_object.write(macContent)
        file_object.close()





















