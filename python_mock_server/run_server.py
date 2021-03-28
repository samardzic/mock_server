import os
import sys
import subprocess
import mock_server

# The following names have currently been registered: 'posix', 'nt', 'java'.
print(os.name)

port = "9005"
directory = "json_files"
runCommand = "ls"

# AIX='aix', Linux='linux', Windows='win32', Windows/Cygwin='cygwin', macOS='darwin'
print("This is OS definition: ", sys.platform)

if sys.platform.startswith('darwin'):
    # Mac FreeBSD-specific code here...
    print("This is MacOS based system.")

elif sys.platform.startswith('linux'):
    # Linux-specific code here...
    print("This is Linux based system.")
    subprocess.run(['ls -la'], shell=True)
    os.system(f'gnome-terminal -x mock-server --dir={directory} --port={port}')

elif sys.platform.startswith('win32'):
    # Windows-specific code here...
    print("This is Windows based system.")
    os.system(f'start /b mock-server --dir {directory} --port {port}')
    subprocess.run(["powershell", "-Command", runCommand], capture_output=True)

else:
    print("Sorry, we don't currently have support for the " + sys.platform + "OS")
