# Source https://gist.github.com/simonw/091b765a071d1558464371042db3b959
# Modified by prune.pillone@etu.unice.fr

## to run the script you need to put the path to the git root
import subprocess
import re
import os
import sys

leading_4_spaces = re.compile('^    ')

keywords = ["localization", "l10n", "i18n", "internationalization", "translate", "translation", "weblate"]

def getName():
    list = sys.argv[1].split("/")
    filename = "output_" + list[len(list)-2] + ".txt"
    return filename

def get_commits():
    lines = subprocess.check_output(
        ['git', 'log'], stderr=subprocess.STDOUT
    ).split('\n')
    commits = []
    current_commit = {}

    def save_current_commit():
        title = current_commit['message'][0]
        message = current_commit['message'][1:]
        if message and message[0] == '':
            del message[0]
        current_commit['title'] = title
        current_commit['message'] = '\n'.join(message)
        commits.append(current_commit)

    for line in lines:
        if not line.startswith(' '):
            if line.startswith('commit '):
                if current_commit:
                    save_current_commit()
                    current_commit = {}
                current_commit['hash'] = line.split('commit ')[1]
            else:
                try:
                    key, value = line.split(':', 1)
                    current_commit[key.lower()] = value.strip()
                except ValueError:
                    pass
        else:
            current_commit.setdefault(
                'message', []
            ).append(leading_4_spaces.sub('', line))
    if current_commit:
        save_current_commit()
    return commits

def get_Files(commit):
    number = 0
    files = subprocess.check_output(
        ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit['hash']], stderr=subprocess.STDOUT).split(
        '\n')
    for file in files:
        # print(file)
        number += 1
    outputFile.write(commit['hash'] + "->" + commit['title'] + " : " + commit['message'] + " = " + str(number) + "\n")

outputFile = open(getName(), 'w')
os.chdir(sys.argv[1])
commits = get_commits()

for commit in commits:
    # print(commit['title'])
    # print(commit['message'])
    # print(commit['hash'])
    found = 0
    for word in keywords:
        if found == 0 and (word in commit['message'] or word in commit['title']):
            get_Files(commit)
            found = 1

outputFile.close()
