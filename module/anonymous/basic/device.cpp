export module anonymous:basic.device;
export import          :basic.device.cpu;
export import          :basic.device.pmr;
export import          :basic.device.system;
export import          :basic.device.tbb;
#ifdef CUDA
    export import          :basic.device.cuda;
#endif
#ifdef OPENCL
    export import          :basic.device.opencl;
#endif
#ifdef ROCM
    export import          :basic.device.rocm;
#endif
#ifdef VULKAN
    export import          :basic.device.vulkan;
#endif

