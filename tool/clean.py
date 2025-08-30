import cppmake

async def clean():
    await cppmake.remove_dir("./bin/module")
    await cppmake.remove_dir("./bin/source")

cppmake.main(clean())