export module anonymous:basic.device;
export import          :basic.device.cpu;
export import          :basic.device.pmr;
export import          :basic.device.system;
export import          :basic.device.tbb;
#ifdef ENABLE_CUDA
export import          :basic.device.cuda;
#endif
#ifdef ENABLE_OPENCL
export import          :basic.device.opencl;
#endif
