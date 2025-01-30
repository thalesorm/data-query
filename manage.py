import subprocess
import sys
import os

def run(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    
    python_path = os.path.abspath("src")
    os.environ["PYTHONPATH"] = python_path

    if sys.argv[1] == 'install':
        run('python -m venv venv && .\\venv\\Scripts\\activate && pip install -r requirements.txt')
    elif sys.argv[1] == 'start':
        run('.\\venv\\Scripts\\activate && python src\\main.py')
    elif sys.argv[1] == 'test':
        run('.\\venv\\Scripts\\activate && pytest tests')
    else:
        print('Comando inválido. Use install, start ou test.')
