import cppmake

async def build():
    await cppmake.include(
        name="plf",
        file="./package/plf/plf_hive.h"
    )