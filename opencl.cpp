#include <CL/opencl.hpp>
#include <clblast.h>
#include <iostream>
#include <vector>
#include <chrono>

#define N 1024   // 矩阵大小 N×N

int main() {
    std::vector<float> A(N * N, 1.0f);
    std::vector<float> B(N * N, 2.0f);
    std::vector<float> C(N * N, 0.0f);

    // 选择 OpenCL 平台和设备
    std::vector<cl::Platform> platforms;
    cl::Platform::get(&platforms);
    auto platform = platforms[0];
    std::vector<cl::Device> devices;
    platform.getDevices(CL_DEVICE_TYPE_GPU, &devices);
    auto device = devices[0];
    cl::Context context(device);
    cl::CommandQueue queue(context, device);

    // 创建 buffer
    cl::Buffer dA(context, CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR, sizeof(float)*A.size(), A.data());
    cl::Buffer dB(context, CL_MEM_READ_ONLY | CL_MEM_COPY_HOST_PTR, sizeof(float)*B.size(), B.data());
    cl::Buffer dC(context, CL_MEM_READ_WRITE | CL_MEM_COPY_HOST_PTR, sizeof(float)*C.size(), C.data());

    const float alpha = 1.0f;
    const float beta  = 0.0f;

    auto start = std::chrono::high_resolution_clock::now();
    for(int i=0; i<10000; i++) {
        clblast::Gemm(
            clblast::Layout::kRowMajor,
            clblast::Transpose::kNo, clblast::Transpose::kNo,
            N, N, N,
            alpha,
            dA(), 0, N,
            dB(), 0, N,
            beta,
            dC(), 0, N,
            &queue(), nullptr
        );
    }
    queue.finish();
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "CLBlast: " << elapsed.count() << " sec\n";
}
