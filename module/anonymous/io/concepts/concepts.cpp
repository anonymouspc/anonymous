export module anonymous:io.concepts.concepts;

export namespace anonymous
{
    template < class type >
    concept reader = 
        requires { requires ( type& t, char* c, size_t s ) { t.read(c, s) } -> integral; }

}