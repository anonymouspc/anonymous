from common.make import include, src

include(
    name="tbb",
    dir="./package/oneTBB/include"
)
src(
    name="tbb",
    dir="./package/oneTBB/src"
)
