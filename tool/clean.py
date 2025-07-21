from common.config import argv
import shutil

if __name__ == "__main__":
    open(".log", 'w')
    shutil.rmtree(f"./bin/{argv.type}/module", ignore_errors=True)
    shutil.rmtree(f"./bin/{argv.type}/source", ignore_errors=True)