from common.make import include, format
import os
import re

async def build():
    await include(
        name="stdexec",
        dir="./package/stdexec/include"
    )
    await format(
        name="stdexec"
    )