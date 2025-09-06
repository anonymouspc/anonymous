import argparse
import os
import warnings

# Settings
os.chdir(f"{os.path.dirname(__file__)}/../../..")
os.environ["LANG"] = "en_US.UTF-8"
warnings.filterwarnings("ignore", "coroutine .* was never awaited")

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--type",           choices=["debug", "release", "size"],                     default="debug"       )
parser.add_argument("--compiler",                                                                 default=""            )
parser.add_argument("--parallel",       type=lambda n: int(n),                                    default=os.cpu_count())
parser.add_argument("--update-package", action="store_true",                                      default=False         )
group = parser.add_mutually_exclusive_group()
group .add_argument("--verbose",        action="store_true",                                      default=False         )
group .add_argument("--dry-run",        action="store_true",                                      default=False         )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-python",  action="store_true",                dest="enable_python", default=False         )
group .add_argument("--disable-python", action="store_false",               dest="enable_python", default=True          )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-opencl",  action="store_true",                dest="enable_opencl", default=False         )
group .add_argument("--disable-opencl", action="store_false",               dest="enable_opencl", default=True          )
group = parser.add_mutually_exclusive_group()
group .add_argument("--enable-cuda",    action="store_true",                dest="enable_cuda",   default=False         )
group .add_argument("--disable-cuda",   action="store_false",               dest="enable_cuda",   default=True          )
config = parser.parse_args()
