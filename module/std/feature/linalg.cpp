module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif

export module std.feature:linalg;

export namespace std
{
    namespace linalg
    {
        template < class layout >                class layout_transpose;
        template < class scale, class accessor > class scaled_accessor;
        template < class accessor >              class conjugated_accessor;
    }
}