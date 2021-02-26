import subprocess

cmd_list = ["python3", "main.py", "-i", "data/input.json", "-o", "data/output.json"]

try:
    subprocess.run(cmd_list)
    print("Success: output.json created into the data folder.")
except Exception as e:
    print("Failed:", str(e))