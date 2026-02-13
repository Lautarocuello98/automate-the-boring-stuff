import subprocess
import time

# Inform the user that Notepad will be opened
print("Opening notepad...", flush=True)

# Launch Notepad as a separate process
proc = subprocess.Popen("C:\\Windows\\System32\\notepad.exe")

# Wait a moment before checking the process status
time.sleep(2)

print("Checking if still running...", flush=True)

# poll() returns None if the process is still running
if proc.poll() is None:
    print("Notepad is still open.", flush=True)
else:
    print("Notepad already closed.", flush=True)

print("Waiting until you close the notepad...", flush=True)

# wait() blocks the script until the process finishes
proc.wait()

# After the process finishes, execution continues here
print("Notepad closed.", flush=True)

# poll() now returns the exit code of the process
print("Exit code:", proc.poll(), flush=True)
