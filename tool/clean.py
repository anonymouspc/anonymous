import cppmake

async def clean():
    cppmake.remove_dir(f"./binary/{cppmake.config.type}/module")
    cppmake.remove_dir(f"./binary/{cppmake.config.type}/source")

cppmake.main(clean())