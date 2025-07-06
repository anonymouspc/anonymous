export module assert;
import std;

export
{
    void assert ( bool val )
    {
        if ( not val )
            throw std::exception();
    }
}

