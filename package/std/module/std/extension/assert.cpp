module;
#include <cassert>

export module std:extension.assert;

export
{
    void __assert__ ( bool value )
    {
        assert(value);
    }

    #undef assert
    inline void assert ( bool value )
    {
        __assert__(value);
    }
}