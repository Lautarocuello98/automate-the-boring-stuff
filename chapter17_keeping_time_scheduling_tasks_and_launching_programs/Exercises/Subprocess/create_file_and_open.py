import subprocess

# create a file
with open("report.txt", "w") as f:
    f.write("Report generated successfully.")

# open it automatically
subprocess.Popen(['start', 'report.txt'], shell=True)
