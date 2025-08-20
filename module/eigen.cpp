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
import        std;

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

// template < bool lhs_inner_dim_contiguous,
//            bool rhs_inner_dim_conitguous,
//            bool rhs_inner_dim_reordered,
//            int  Alignment,
//            bool use_output_kernel,
//            class Derived >
// export using type = 
// TensorContractionInputMapper<
//   typename std::remove_const<
//     typename std::conditional<
//       (static_cast<int>(Eigen::TensorContractionEvaluatorBase<Derived>::Layout)
//          == static_cast<int>(Eigen::ColMajor)),
//       typename Eigen::internal::traits<T>::LeftArgType,
//       typename Eigen::internal::traits<T>::RightArgType
//     >::type::Scalar
//   >::type,                                    // Scalar_

//   typename Eigen::TensorContractionOp<
//     typename Eigen::internal::traits<T>::Indices,
//     typename Eigen::internal::traits<T>::LeftArgType,
//     typename Eigen::internal::traits<T>::RightArgType,
//     typename Eigen::internal::traits<T>::OutputKernelType
//   >::Index,                                   // Index

//   1,                                          // side

//   Eigen::TensorEvaluator<
//     typename std::conditional<
//       (static_cast<int>(Eigen::TensorContractionEvaluatorBase<Derived>::Layout)
//          == static_cast<int>(Eigen::ColMajor)),
//       typename Eigen::internal::traits<T>::LeftArgType,
//       typename Eigen::internal::traits<T>::RightArgType
//     >::type,
//     typename Eigen::internal::traits<T>::Device
//   >,                                          // Tensor

//   std::array<
//     typename Eigen::TensorContractionOp<
//       typename Eigen::internal::traits<T>::Indices,
//       typename Eigen::internal::traits<T>::LeftArgType,
//       typename Eigen::internal::traits<T>::RightArgType,
//       typename Eigen::internal::traits<T>::OutputKernelType
//     >::Index,
//     (Eigen::TensorContractionEvaluatorBase<Derived>::LDims 
//      - Eigen::TensorContractionEvaluatorBase<Derived>::ContractDims)
//   >,                                          // nocontract_t

//   std::array<
//     typename Eigen::TensorContractionOp<
//       typename Eigen::internal::traits<T>::Indices,
//       typename Eigen::internal::traits<T>::LeftArgType,
//       typename Eigen::internal::traits<T>::RightArgType,
//       typename Eigen::internal::traits<T>::OutputKernelType
//     >::Index,
//     Eigen::TensorContractionEvaluatorBase<Derived>::ContractDims
//   >,                                          // contract_t

//   lhs_packet_size,                            // packet_size
//   lhs_inner_dim_contiguous,                   // inner_dim_contiguous
//   false,                                      // inner_dim_reordered
//   lhs_alignment                               // Alignment
// >;