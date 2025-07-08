export module anonymous.basic.concepts:numbers;
import        std;

export namespace anonymous
{
    template < class type > concept integral       = std::signed_integral<type>;
    template < class type > concept floating_point = std::floating_point <type>;
    template < class type > concept numeric        = integral<type> or floating_point<type>;
}