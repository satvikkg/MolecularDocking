import os

schrodinger_path = '/opt/schrodinger2024-1'
processors = 60

grid_folder_path = "/"
database_path = "/"
output_path = "/"

if os.path.exists(output_path) != True:
    print(f'Output Path Does Not Exist. Creating new path at {output_path}.')
    os.mkdir(output_path)

for grid_file in os.listdir(grid_folder_path):
    job_name = f'glide_SP_{os.path.splitext(grid_file)[0]}'
    job_path = f'{output_path}/{job_name}'

    if os.path.exists(job_path) != True:
        os.mkdir(job_path)
    else:
        print(f'{job_path}: Exists.')

    glide_inp_options = [
    'FORCEFIELD OPLS4\n',
    f'GRIDFILE {grid_folder_path}/{grid_file}\n',
    f'LIGANDFILE {database_path}\n',
    'PRECISION SP\n',
    ]

    glide_inp_file = f'{output_path}/{job_name}/{job_name}.in'
    f = open(glide_inp_file, 'w')
    f.writelines(glide_inp_options)
    f.close()

    glide_queue_file = f'{output_path}/glide_queue_job.sh'
    f = open(glide_queue_file, 'a')
    f.write(f'cd {output_path}/{job_name}\n')
    f.write(f'echo "Running job: {job_name}"\n')
    f.write(f'{schrodinger_path}/glide {glide_inp_file} -OVERWRITE -adjust -HOST localhost:{processors} -TMPLAUNCHDIR -WAIT\n')
    f.write(f'echo "{job_name} completed."\n')
    f.close()