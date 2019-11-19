# this module can spawn child process, an instance of a running program
import subprocess
# this methods are old one
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# run replaces the above methods
# subprocess.run(["ls", "-l"])
#
completed = subprocess.run(["python", "python_standard_library_ex/other.py"],
                           capture_output=True,
                           shell=True,
                           text=True)
#print(type(subprocess.run(["dir", "/w"], shell=True)))
print("args", completed.args)  # give array with the command we used
# if is 0 there are not errors, any other value than 0 indicates errors
print("return code", completed.returncode)
print("stderr", completed.stderr)  # standard error, None indicate no error
# standard output, None indicate we are not catching the output
print("stdout", completed.stdout)
