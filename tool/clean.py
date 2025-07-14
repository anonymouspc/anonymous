from common.config import type
import shutil

if __name__ == "__main__":
    try:  shutil.rmtree(f"./binary/{type}/module")
    except: pass