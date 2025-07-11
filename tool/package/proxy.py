from common.make import include, module

include(
    name="proxy",
    dir="./package/proxy/include"
)
module(
    name="proxy",
    file="./package/proxy/include/proxy/v4/proxy.ixx",
    replace={"proxy.v4": "proxy"}
)