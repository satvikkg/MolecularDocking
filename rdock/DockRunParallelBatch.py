import os, re, time, subprocess
from joblib import Parallel, delayed

ligands_dir = '/mnt/storage/RANAR_RDOCK/batchligs'
receptors_paths = "/mnt/storage/RANAR_RDOCK/Jobs/Batch_check/Batch"

def rDockParallel(ligandfile, ligands_dir, receptor_path, output_path, receptors_paths, folder):
   outfilename = f'{output_path}/{os.path.splitext(ligandfile)[0]}'
   os.system(f'cd {receptors_paths}/{folder} && rbdock -i {ligands_dir}/{ligandfile} -o {outfilename}-out -r {receptor_path} -p dock.prm -n 1 -allH')

for folder in os.listdir(receptors_paths):
    receptor_path = f'{receptors_paths}/{folder}/{folder}.prm'
    output_path = f'{receptors_paths}/{folder}/outputParallel'
    #print(receptor_path, output_path)

    if os.path.exists(output_path) != True:
        os.mkdir(output_path)
    else:
        print('Output path exists')
                
    start_time = time.time()
    ParallelRun = Parallel(n_jobs=16)(delayed(rDockParallel)(ligand_file, ligands_dir, receptor_path, output_path, receptors_paths, folder) for ligand_file in os.listdir(ligands_dir))
    print(f'Time Taken: {time.time() - start_time}')