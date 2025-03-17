from subprocess import check_output
import subprocess
check_output('pyinstaller --noconsole --onefile bydef_enc.py')
print('[+] Compiled successfully... locate the PE inside the dist folder... ta-da')