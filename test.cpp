#include <cstdint>
#include <vector>

template < class T >
concept has_a = requires { typename T::a; };

constexpr bool b = has_a<std::uint8_t>;