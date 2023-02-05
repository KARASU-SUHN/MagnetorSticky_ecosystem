#p2c
import subprocess
def executeCommand(projectName):
    command = 'echo {project} | ~/lookup/getValues -f p2c'.format(project=projectName)
    output = subprocess.Popen((command),shell=True).communicate()
    return output
with open('~/project.txt') as f:
    projectName = f.read()
    for line in projectName.split("\n"):
       commandOutput =  executeCommand(line)
       print(commandOutput)

#c2dat
import subprocess
def executeCommand(projectName):
    command = 'echo {project} | ~/lookup/getValues c2dat'.format(project=projectName)
    output = subprocess.Popen((command),shell=True).communicate()
    return output
with open('~/commits.txt') as f:
    projectName = f.read()
    for line in projectName.split("\n"):
       commandOutput =  executeCommand(line)
       print(commandOutput)