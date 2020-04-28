import sys
import subprocess
# Python version
vsn=sys.version
print("Using Python version: {}".format(vsn.split("\n")[0]))
if vsn[0] != "3":
    print("You are currently not using Python3. Change your Python version from the configuration file.")

#FFMPEG version
ffmpeg = subprocess.check_output(["ffmpeg","-version"])
print(ffmpeg[0:20].decode("utf-8"))

#Check packages 
required=["lxml","pandas","pydub"]
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
for pckg in required:
	if pckg not in installed_packages:
		print("Missing package: {}".format(pckg))