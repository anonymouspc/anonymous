import cppmake

async def build():
    await cppmake.cmake(
        name="clblast",
        dir="./package/clblast",
        args=[
            "-DBUILD_SHARED_LIBS=false",
            "-DSAMPLES=false",
            "-DCLIENTS=false",
            "-DTESTS=false",
            "-DCUBLAS=false",
            "-DNETLIB=false",
            "-DOPENCL=true",
            "-DCUDA=false",
        ]
    )

"""
>>> cat ./package/clblast/CMakeLists.txt | grep option
option(OVERRIDE_MSVC_FLAGS_TO_MT "Override compiler flags for MSVC to build with a static runtime (/MT instead of /MD)" ON)
option(BUILD_SHARED_LIBS "Build a shared (ON) or static library (OFF)" ON)
option(SAMPLES "Enable compilation of the examples" OFF)
option(TUNERS "Enable compilation of the tuners" ON)
option(CLIENTS "Enable compilation of the clients to test and compare performance" OFF)
option(TESTS "Enable compilation of the correctness tests" OFF)
option(CUBLAS "Enables performance comparison against cuBLAS on NVIDIA GPUs" OFF)
# The optional Netlib API for CLBlast
option(NETLIB "Enable compilation of the CBLAS Netlib API" OFF)
option(NETLIB_PERSISTENT_OPENCL "Makes OpenCL device and context in the CBLAS Netlib API static" OFF)
option(AMD_SI_EMPTY_KERNEL_WORKAROUND "Enables workaround for bug in AMD Southern Island GPUs" OFF)
option(OPENCL "Build CLBlast with an OpenCL API (default)" ON)
option(CUDA "Build CLBlast with a CUDA API (beta)" OFF)
option(VERBOSE "Compile in argv.verbose mode for additional diagnostic messages" OFF)
# Section for the performance tests (i.e. the client). These compare against optionally a reference
"""