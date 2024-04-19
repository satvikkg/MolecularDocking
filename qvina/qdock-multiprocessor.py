import os
import time
from joblib import Parallel, delayed

st = time.time()
cpu = 4
receptor_path = '/home/administrator/Downloads/qvina/test4/super'
ligands_dir = '/home/administrator/Downloads/qvina/test4/super/ligands'

def test2(path, lpath, ligand):
  ligname = os.path.splitext(ligand)[0]
  dpath = f'{lpath}/docking'
  if not os.path.exists(dpath):
    os.mkdir(dpath)
  os.system(f'/home/administrator/Downloads/qvina/qvina2.1 --receptor {path}/protein.pdbqt --ligand {lpath}/{ligand} --config {path}/config.txt --out {dpath}/{ligname}_docked.pdbqt --log {dpath}/{ligname}_log.txt')


job = Parallel(n_jobs=cpu, timeout=None)(delayed(test2)(receptor_path, ligands_dir, lig) for lig in os.listdir(ligands_dir))

print(f'Time taken for docking {len(os.listdir(ligands_dir))} is {(time.time()-st)/60}min.')
