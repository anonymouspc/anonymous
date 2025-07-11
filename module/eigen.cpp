module;
#undef in
#undef self
#ifdef __GNUC__
    #pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif
#include <Eigen/Core>
#include <Eigen/Dense>
#include <Eigen/Sparse>
#include <unsupported/Eigen/FFT>
#include <unsupported/Eigen/CXX11/Tensor>

export module eigen;
import std;

export namespace Eigen
{
    using Eigen::ColMajor;
    using Eigen::Dynamic;
    using Eigen::FFT;
    using Eigen::InnerStride;
    using Eigen::Map;
    using Eigen::Matrix;
    using Eigen::RowMajor;
    using Eigen::Stride;
    using Eigen::Tensor;
    using Eigen::TensorMap;
    using Eigen::Unaligned;
    using Eigen::Vector;
    using Eigen::operator<<;
}