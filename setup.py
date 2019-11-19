import subprocess
subprocess.check_call(["python3", '-m', 'pip', 'install', 'Flask']) # install Flask
subprocess.check_call(["python3", '-m', 'pip', 'install', 'psutil']) # install psutil for process management