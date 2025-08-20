from common.config     import argv
from common.filesystem import remove_dir
import asyncio

async def clean():
    await remove_dir(f"./bin/{argv.type}/module")
    await remove_dir(f"./bin/{argv.type}/source")

if __name__ == "__main__":
    asyncio.run(clean())