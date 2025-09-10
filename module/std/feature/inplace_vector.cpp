export module std:feature.inplace_vector;
import           :compiler;

export namespace std::inline feature
{
    template < class type, size_t len >
    class inplace_vector
        extends public vector<type>
    {

    };
}
