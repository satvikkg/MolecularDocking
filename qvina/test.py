import os
#import shlex, subprocess
from joblib import Parallel, delayed

def qdock(path):
  args = shlex.split(f'/home/administrator/Downloads/qvina/qvina2.1 --receptor {path}/protein.pdbqt --ligand {path}/Z15502965.pdbqt --out {path}/docked.pdbqt --log {path}/results.txt --config {path}/config.txt')
  p = subprocess.Popen(args)
  
#qdock('/home/administrator/Downloads/qvina/test4/super')

def test(path):
  os.system(f'/home/administrator/Downloads/qvina/qvina2.1 --receptor {path}/protein.pdbqt --ligand {path}/Z15502965.pdbqt --out {path}/docked.pdbqt --log {path}/results.txt --config {path}/config.txt')
  
#test('/home/administrator/Downloads/qvina/test4/super')

def test2(path, lpath, ligand):
  ligname = os.path.splitext(ligand)[0]
  dpath = f'{lpath}/docking'
  if not os.path.exists(dpath):
    os.mkdir(dpath)
  os.system(f'/home/administrator/Downloads/qvina/qvina2.1 --receptor {path}/protein.pdbqt --ligand {lpath}/{ligand} --config {path}/config.txt --out {dpath}/{ligname}_docked.pdbqt --log {dpath}/{ligname}_log.txt')

'''
for lig in os.listdir('/home/administrator/Downloads/qvina/test4/super/ligands'):
  test2('/home/administrator/Downloads/qvina/test4/super', '/home/administrator/Downloads/qvina/test4/super/ligands', lig)
'''

job = Parallel(n_jobs=4, timeout=None)(delayed(test2)('/home/administrator/Downloads/qvina/test4/super', '/home/administrator/Downloads/qvina/test4/super/ligands', lig) for lig in os.listdir('/home/administrator/Downloads/qvina/test4/super/ligands'))
