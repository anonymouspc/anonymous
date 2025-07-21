from common.config import type
from common.log    import log
import shutil

if __name__ == "__main__":
    open(".log", 'w')
    shutil.rmtree(f"./bin/{type}/module", ignore_errors=True)
    shutil.rmtree(f"./bin/{type}/source", ignore_errors=True)