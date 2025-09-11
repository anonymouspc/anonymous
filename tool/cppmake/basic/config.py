import argparse
import os
import warnings

# Settings
os.chdir(f"{os.path.dirname(__file__)}/../../..")
os.environ["LANG"] = "C"
warnings.filterwarnings("ignore", "coroutine .* was never awaited")

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--type",           choices=["debug", "release", "size"], default="debug"       )
parser.add_argument("--compiler",                                             default=""            )
parser.add_argument("--parallel",       type=lambda n: int(n),                default=os.cpu_count())
parser.add_argument("--update-package", action="store_true",                  default=False         )
parser.add_argument("--verbose",        action="store_true",                  default=False         )
parser.add_argument("--dry-run",        action="store_true",                  default=False         )
config = parser.parse_args()
