export module anonymous:basic.execution.async;
import                 :basic.concepts;
import        std;

export namespace anonymous
{
    template < class type = void >
    class async
    {
        public: // Concept
            using sender_concept = std::execution::sender_t;

        public: // Constructor
            constexpr async ( std::execution::sender auto );

        public: // Conversion
            template < class type2 >          constexpr operator async<type2> ( ) const requires convertible_to  <type,type2>;
            template < class type2 > explicit constexpr operator async<type2> ( ) const requires constructible_to<type,type2>;
    };
}