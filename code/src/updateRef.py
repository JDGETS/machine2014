import os
import sys

def visit(folder):
    for fn in os.listdir(folder):
        filename = os.path.join(folder, fn)
        _, ext = os.path.splitext(fn)
        if os.path.isdir(filename):
            folders.append(filename)
            visit(filename)
        elif ext.lower() == '.py':
            files.append(filename)

files = []
folders = []

visit('.')

print '<ItemGroup>'
for fn in files:
    print '  <Compile Include="' + fn + '"/>'
print '</ItemGroup>'

if folders:
    print '<ItemGroup>'
    for fn in folders:
        print '  <Folder Include="' + fn + '\\"/>'
    print '</ItemGroup>'
    sys.read()