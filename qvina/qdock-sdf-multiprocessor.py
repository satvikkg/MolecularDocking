import os
import time
from joblib import Parallel, delayed

st = time.time()
cpu = 10
receptor_path = '/home/administrator/Downloads/qvina/test4/super'
ligands_dir = '/home/administrator/Downloads/qvina/test2/ligands'
pdbqt_dir = '/home/administrator/Downloads/qvina/test4/super/pdbqt'
results_dir = '/home/administrator/Downloads/qvina/test4/super/pdbqt/docking'

if not os.path.exists(pdbqt_dir):
  os.mkdir(pdbqt_dir)
  
if not os.path.exists(results_dir):
  os.mkdir(results_dir)
  
def qvina(path, lpath, dpath, pdbqtpath, ligand):
  ligname = os.path.splitext(ligand)[0]
  os.system(f'obabel -i sdf {ligands_dir}/{ligand} -o pdbqt -O {pdbqtpath}/{ligname}.pdbqt') 
  os.system(f'/home/administrator/Downloads/qvina/qvina2.1 --receptor {path}/protein.pdbqt --ligand {pdbqtpath}/{ligname}.pdbqt --config {path}/config.txt --out {dpath}/{ligname}_docked.pdbqt --log {dpath}/{ligname}_log.txt')


job = Parallel(n_jobs=cpu, timeout=None)(delayed(qvina)(receptor_path, ligands_dir, results_dir, pdbqt_dir, lig) for lig in os.listdir(ligands_dir))

print(f'Time taken for docking {len(os.listdir(ligands_dir))} is {(time.time()-st)/60}min.')
