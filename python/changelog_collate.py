import subprocess
import os
try:
    import yaml
except ImportError:
    subprocess.check_call(['pip3', 'install', 'PyYAML'])
    subprocess.check_call(['pip', 'install', 'PyYAML'])
    import yaml


def getPubspecVersion(file_path):
    with open(file_path, 'r') as file:
        pubspecData = yaml.safe_load(file)
        version = pubspecData.get('version')
        return version


def searchDirectory(directory):
    mdFiles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                mdFiles.append(os.path.join(root, file))
    return mdFiles


def collateFileContent(filePaths):
    contents = []
    for filePath in filePaths:
        with open(filePath, 'r') as file:
            contents.append(file.read())
    return contents


def deleteFiles(filePaths):
    for filePath in filePaths:
        os.remove(filePath)


def prependLines(filePath, lines):
    with open(filePath, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(lines + content)


version = getPubspecVersion('pubspec.yaml')
print(f"Version: {version}")

mdFiles = searchDirectory('changes')
collatedContent = collateFileContent(mdFiles)
deleteFiles(mdFiles)

lines = '## ' + version + '\n\n' + '\n'.join(collatedContent) + '\n\n'

prependLines('CHANGELOG.md', lines)

print('Successfully Collated Changes')
