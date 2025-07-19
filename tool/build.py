from common.error   import BuildError
from file.module    import Module
from file.object    import Object
from file.package   import Package
from file.source    import Source
import asyncio

if __name__ == "__main__":
    async def build():
        open(".log", 'w')
        await Object("main")
        await asyncio.gather(*[package.build  () for package in Package.pool.values()])
        await asyncio.gather(*[module .compile() for module  in Module .pool.values()])
        await asyncio.gather(*[source .compile() for source  in Source .pool.values()])
        await asyncio.gather(*[object .link   () for object  in Object .pool.values()])

    try:
        asyncio.run(build())
    except BuildError as e:
        print(e, end="", file=open(".log", 'a'))
        exit(-1)
    except KeyboardInterrupt as e:
        exit(-1)
    except:
        raise
        