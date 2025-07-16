export module anonymous:basic.device.cpu.impl.linalg.eigen;
import                 :basic.device.cpu.impl.linalg.detail.map;
import                 :basic.device.cpu.decl;
import        eigen;

export namespace anonymous
{
    constexpr void cpu::linalg::unary_plus ( const auto right, auto output )
    {
        eigen_map(output).noalias() = + eigen_map<typename decltype(output)::value_type>(right);
    }

    constexpr void cpu::linalg::unary_minus ( const auto right, auto output )
    {
        eigen_map(output).noalias() = - eigen_map<typename decltype(output)::value_type>(right);
    }

    constexpr void cpu::linalg::plus ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left) + eigen_map<typename decltype(output)::value_type>(right);
    }

    constexpr void cpu::linalg::minus ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left) - eigen_map<typename decltype(output)::value_type>(right);
    }

    constexpr void cpu::linalg::left_scale ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = left * eigen_map(right);
    }

    constexpr void cpu::linalg::right_scale ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left) * right;
    }

    constexpr void cpu::linalg::multiply ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left) * eigen_map<typename decltype(output)::value_type>(right);
    }

    constexpr void cpu::linalg::divide ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left) / right;
    }

    constexpr void cpu::linalg::plus_equal ( auto left, const auto right )
    {
        eigen_map(left) += eigen_map<typename decltype(left)::value_type>(right);
    }

    constexpr void cpu::linalg::minus_equal ( auto left, const auto right )
    {
        eigen_map(left) -= eigen_map<typename decltype(left)::value_type>(right);
    }

    constexpr void cpu::linalg::right_scale_equal ( auto left, const auto right )
    {
        eigen_map(left) *= right;
    }

    constexpr void cpu::linalg::multiply_equal ( auto left, const auto right )
    {
        eigen_map(left) *= eigen_map<typename decltype(left)::value_type>(right);
    }

    constexpr void cpu::linalg::divide_equal ( auto left, const auto right )
    {
        eigen_map(left) /= right;
    }

    constexpr void cpu::linalg::convolve ( const auto left, const auto right, auto output )
    {
        eigen_map<typename decltype(output)::value_type,eigen_map_tensor>(output) = eigen_map<typename decltype(output)::value_type,eigen_map_tensor>(left).convolve(eigen_map<typename decltype(output)::value_type,eigen_map_tensor>(right), eigen_make_convolve_full_dims<left.rank()>());
    }

    constexpr void cpu::linalg::cross ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left).cross(eigen_map<typename decltype(output)::value_type>(right));
    }

    constexpr void cpu::linalg::dot ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left).dot(eigen_map<typename decltype(output)::value_type>(right));
    }

    constexpr void cpu::linalg::fft ( const auto vector, auto output )
    {
        auto output_map = eigen_map(output);
        Eigen::FFT<typename decltype(output)::value_type::value_type>().fwd(output_map, eigen_map(vector));
    }

    constexpr void cpu::linalg::ifft ( const auto vector, auto output )
    {
        auto output_map = eigen_map(output);
        Eigen::FFT<typename decltype(output)::value_type::value_type>().inv(output_map, eigen_map(vector));
    }

    constexpr void cpu::linalg::tensor ( const auto left, const auto right, auto output )
    {
        eigen_map(output).noalias() = eigen_map<typename decltype(output)::value_type>(left) * eigen_map<typename decltype(output)::value_type>(right).transpose();
    }
}