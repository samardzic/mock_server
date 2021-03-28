import os
import subprocess


# def powerShellRun(runCommand):
#     subprocess.run(["powershell", "-Command", runCommand], capture_output=True)


port = "9005"
directory = "json_files"
os.system(f'start /b mock-server --dir {directory} --port {port}')

