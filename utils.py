import os
import subprocess
from tex_templates.tex_const import PREAMBULE, END, TMP_OUTPUT

def is_tex_valid(text):
    with open(TMP_OUTPUT + 'tmp.tex','w+') as f:
        f.write(PREAMBULE + '\n' + text + END)

    cmd = ['pdflatex', '-interaction', 'nonstopmode', TMP_OUTPUT + 'tmp.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    os.unlink( TMP_OUTPUT + 'tmp.tex')
    try:
        os.unlink('tmp.pdf')
    except OSError:
        pass
    os.unlink('tmp.log')
    os.unlink('tmp.aux')

    if not retcode == 0:
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 


