module;
#undef in
#if defined(_WIN32) or defined(__linux__)
    #include <CL/cl.h>
#elifdef __MACH__
    #include <OpenCL/opencl.h>
#endif

export module opencl;

export
{
    
}