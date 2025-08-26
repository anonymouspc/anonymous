export module test;

template < class type >
struct MakePointer
{

};

template < 
    int value, 
    template < class type > class MakePointer_ = MakePointer 
>
struct TensorContractionMapper
{

};

export
template < int value >
void func ( )
{
    const int a = 1;
    using Mapper = TensorContractionMapper<a>;
}

