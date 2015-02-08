import os
import subprocess

communities_dir = os.listdir('find/fixtures')

for directory in sorted(communities_dir):
    files = os.listdir('find/fixtures/%s' % directory)
    letter = directory[-1]
    subprocess.call(['python', 'manage.py', 'syncdb', '--database=db_%s' % letter])
    for f in sorted(files):
        full_path = 'find/fixtures/%s/%s' % (directory, f)
        print full_path
        subprocess.call(['python', 'manage.py', 'loaddata', full_path, '--database=db_%s' % letter])
        subprocess.call(['rm', full_path])

