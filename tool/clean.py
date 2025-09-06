import cppmake

async def clean():
    cppmake.remove_dir(f"./bin/{cppmake.config.type}/module")
    cppmake.remove_dir(f"./bin/{cppmake.config.type}/source")

cppmake.main(clean())