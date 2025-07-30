from common.config import argv
from common.logger import compile_output_logger
import shutil

if __name__ == "__main__":
    shutil.rmtree(f"./bin/{argv.type}/module", ignore_errors=True)
    shutil.rmtree(f"./bin/{argv.type}/source", ignore_errors=True)