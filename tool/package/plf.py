from common.make import include

async def build():
    await include(
        name="plf",
        file="./package/plf/plf_hive.h"
    )