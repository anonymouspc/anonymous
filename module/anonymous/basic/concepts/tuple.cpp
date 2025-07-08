export module anonymous.basic.concepts:tuple;
import        std;

export namespace anonymous
{
    template < class type >            constexpr int tuple_size    = std::tuple_size<type>::value;
    template < int index, class type > using         tuple_element = std::tuple_element<(index>=0) ? size_t(index-1) : size_t(index+int(std::tuple_size<type>::value)),type>::type;
}