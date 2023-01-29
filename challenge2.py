import shlex
import subprocess
import json

def call_curl(curl):
    args = shlex.split(curl)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return json.loads(stdout.decode('utf-8'))


if __name__ == '__main__':
    curl = '''http://metadata.google.internal/computeMetadata/v1/instance/disks/" -H "Metadata-Flavor: Google'''
    output = call_curl(curl)
    print(output)
