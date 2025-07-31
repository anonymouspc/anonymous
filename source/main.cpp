import std;
import anonymous;

template < class... types >
int func ( )
{
    if constexpr ( sizeof...(types) < 100 )
        if constexpr ( sizeof...(types) % 2 == 0 )
            return func<types...,int>();
        else
            return func<types...,std::string>();
    else
        std::terminate();
}

int main ( )
{
    assert(false && false);
}