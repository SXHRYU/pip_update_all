import os
import subprocess
import sys
os.system('pip list')

output = subprocess.run("pip list", capture_output=True).stdout
output = str(output).split(' ')

while True:
    try:
        for i in range(len(output)):
            if output[i] == '':
                output.remove(output[i])
        if '' not in output:
            break
    except IndexError:
        pass
output = ' '.join(output).replace('-', '')
output = output.lstrip("b'Package Version \r\n")
output = output.replace("\\r", '').replace('\\n', ' ')
output = output.split(' ')
try:
    for i in range(len(output)):
        if output[i] == '' or '.' in output[i]:
            output.remove(output[i])
    # if '' not in output:
    #     break
except IndexError:
    pass
output.remove(output[0])
output.remove(output[len(output)-1])
print('','All your pip packages:', sep= '\n')
print(*output, sep=';\n')

print('', 'Upgrading...', sep='\n')
for i in range(len(output)):
    os.system(f'echo Upgrading: {output[i]}...')
    os.system(f'pip install {output[i]} --upgrade')
    os.system('echo ______________________________')
