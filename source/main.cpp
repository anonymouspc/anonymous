import cuda;
import thrust;
import std;

int main ( )
{
    auto v = thrust::device_vector<int>(10);
    thrust::fill(v.begin(), v.end(), 10);
    for ( const auto& val in v )
        std::cout << val << std::endl;
}