from common.make import include, src
import os

for lib in os.listdir              ("./package/boost/libs"):
    if os.path.isdir              (f"./package/boost/libs/{lib}/include"):
        include(name=f"boost", dir=f"./package/boost/libs/{lib}/include")
    if os.path.isdir              (f"./package/boost/libs/{lib}/src"):
        src    (name=f"boost", dir=f"./package/boost/libs/{lib}/src", src_to_include=f"boost/{lib}/src")

for lib in os.listdir              ("./package/boost/libs/numeric"):
    if os.path.isdir              (f"./package/boost/libs/numeric/{lib}/include"):
        include(name=f"boost", dir=f"./package/boost/libs/numeric/{lib}/include")
    if os.path.isdir              (f"./package/boost/libs/numeric/{lib}/src"):
        src    (name=f"boost", dir=f"./package/boost/libs/numeric/{lib}/src", src_to_include=f"boost/numeric/{lib}/src")