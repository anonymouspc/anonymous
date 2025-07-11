from common.config import type
import shutil

if __name__ == "__main__":
    try:  shutil.rmtree(f"./bin/{type}/module")
    except: pass