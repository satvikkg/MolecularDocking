import os, re, time, subprocess
from joblib import Parallel, delayed

ligands_dir = '/'
receptor_path = '/'
output_path = '/'

if os.path.exists(output_path) != True:
    os.mkdir(output_path)
else:
    print('Output path exists')
    

def rDockParallel(ligandfile, ligands_dir, receptor_path, output_path):
    outfilename = f'{output_path}/{os.path.splitext(ligandfile)[0]}'
    rDockCommand = f'rbdock -i {ligands_dir}/{ligandfile} -o {outfilename}-out -r {receptor_path} -p dock.prm -n 1 -allH'
    commandlist = re.split('\s+', rDockCommand)
    runCommand = subprocess.run(commandlist, capture_output=False)
    
start_time = time.time()
ParallelRun = Parallel(n_jobs=8)(delayed(rDockParallel)(x, ligands_dir, receptor_path, output_path) for x in os.listdir(ligands_dir))
print(f'Time Taken: {time.time() - start_time}')


 
