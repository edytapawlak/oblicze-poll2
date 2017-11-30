import os
import subprocess
from tex_templates.tex_const import PREAMBULE, END

def is_tex_valid(text):
    with open('tex_templates/cover.tex','w+') as f:
        f.write(PREAMBULE + '\n' + text + END)

    cmd = ['pdflatex', '-interaction', 'nonstopmode', 'tex_templates/cover.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    os.unlink('tex_templates/cover.tex')
    os.unlink('cover.log')
    os.unlink('cover.aux')

    if not retcode == 0:
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 


