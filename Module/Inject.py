import pyinjector
import psutil

# Define the target executable and the DLL to inject
target_process_name = "Dungeons-Win64-Shipping.exe"
dll_path = "unlock.dll"

# Find the process ID (PID) of the target application
def find_process_by_name(process_name):
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None

# Get the PID of the target process
pid = find_process_by_name(target_process_name)

if pid:
    try:
        # Inject the DLL into the target process
        pyinjector.inject(pid, dll_path)
        print(f"Successfully injected {dll_path} into process {target_process_name} (PID: {pid})")
    except Exception as e:
        print(f"Failed to inject the DLL: {e}")
else:
    print(f"Process {target_process_name} not found.")
