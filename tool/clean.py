from common.config import type
import shutil

if __name__ == "__main__":
    shutil.rmtree(f"./bin/{type}/module", ignore_errors=True)
    shutil.rmtree(f"./bin/{type}/source", ignore_errors=True)