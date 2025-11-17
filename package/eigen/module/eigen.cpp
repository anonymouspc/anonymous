module;
#include <Eigen/Core>
#include <Eigen/Dense>
#include <Eigen/Sparse>
#include <unsupported/Eigen/FFT>
#include <unsupported/Eigen/CXX11/Tensor>

export module eigen;
// import std; This module might be depended by std:linalg by std.

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
