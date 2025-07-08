export module anonymous.basic.device;
export import anonymous.basic.device.cpu;
export import anonymous.basic.device.pmr;
export import anonymous.basic.device.system;
export import anonymous.basic.device.tbb;
#ifdef CUDA
    export import anonymous.basic.device.cuda;
#endif
#ifdef OPENCL
    export import anonymous.basic.device.opencl;
#endif
#ifdef ROCM
    export import anonymous.basic.device.rocm;
#endif
#ifdef VULKAN
    export import anonymous.basic.device.vulkan;
#endif

