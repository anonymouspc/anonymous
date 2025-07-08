export module anonymous.basic.device.cpu:iterator.stride_iterator;
import                                  :common.cpu;
import        anonymous.basic.config;

export namespace anonymous
{
    template < class iterator >
    class cpu::stride_iterator
    {
        public: // Typedef
            using iterator_category = std::common_type_t<typename std::iterator_traits<iterator>::iterator_category,std::random_access_iterator_tag>;
            using value_type        = std::iterator_traits<iterator>::value_type;
            using reference         = std::iterator_traits<iterator>::reference;
            using pointer           = std::iterator_traits<iterator>::pointer;
            using difference_type   = std::iterator_traits<iterator>::difference_type;

        private: // Data
            iterator        iter = iterator();
            difference_type strd = difference_type();

        public: // Core
            constexpr stride_iterator ( )                           requires std::default_initializable<iterator> = default;
            constexpr stride_iterator ( iterator, difference_type );

        public: // Member
            constexpr reference operator *  ( )                 const;
            constexpr pointer   operator -> ( )                 const;
            constexpr reference operator [] ( difference_type ) const requires std::random_access_iterator<iterator>;

        public: // Access
            constexpr iterator        base   ( ) const;
            constexpr difference_type stride ( ) const;
    };

    template < class iterator > constexpr bool                                               operator ==  ( cpu::template stride_iterator<iterator>,  cpu::template stride_iterator<iterator> ) requires std::sentinel_for          <iterator,iterator>;
    template < class iterator > constexpr std::compare_three_way_result_t<iterator,iterator> operator <=> ( cpu::template stride_iterator<iterator>,  cpu::template stride_iterator<iterator> ) requires std::totally_ordered       <iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>           operator +   ( cpu::template stride_iterator<iterator>,  std::iter_difference_t       <iterator> ) requires std::random_access_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>           operator +   ( std::iter_difference_t       <iterator>,  cpu::template stride_iterator<iterator> ) requires std::random_access_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>           operator -   ( cpu::template stride_iterator<iterator>,  std::iter_difference_t       <iterator> ) requires std::random_access_iterator<iterator>;
    template < class iterator > constexpr std::iter_difference_t        <iterator>           operator -   ( cpu::template stride_iterator<iterator>,  cpu::template stride_iterator<iterator> ) requires std::random_access_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>&          operator +=  ( cpu::template stride_iterator<iterator>&, std::iter_difference_t       <iterator> ) requires std::random_access_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>&          operator -=  ( cpu::template stride_iterator<iterator>&, std::iter_difference_t       <iterator> ) requires std::random_access_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>&          operator ++  ( cpu::template stride_iterator<iterator>&                                          ) requires std::bidirectional_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>           operator ++  ( cpu::template stride_iterator<iterator>&, int                                     ) requires std::bidirectional_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>&          operator --  ( cpu::template stride_iterator<iterator>&                                          ) requires std::bidirectional_iterator<iterator>;
    template < class iterator > constexpr cpu::template stride_iterator <iterator>           operator --  ( cpu::template stride_iterator<iterator>&, int                                     ) requires std::bidirectional_iterator<iterator>;



    template < class iterator > 
    constexpr cpu::stride_iterator<iterator>::stride_iterator ( iterator init_iter, difference_type init_strd )
        extends iter ( init_iter ),
                strd ( init_strd )
    {
        
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>::reference cpu::stride_iterator<iterator>::operator * ( ) const
    {
        return *iter;
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>::pointer cpu::stride_iterator<iterator>::operator -> ( ) const
    {
        return iter;
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>::reference cpu::stride_iterator<iterator>::operator [] ( difference_type offset ) const
        requires std::random_access_iterator<iterator>
    {
        return iter[offset * strd];
    }

    template < class iterator >
    constexpr iterator cpu::stride_iterator<iterator>::base ( ) const
    {
        return iter;
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>::difference_type cpu::stride_iterator<iterator>::stride ( ) const
    {
        return strd;
    }

    template < class iterator > 
    constexpr bool operator == ( cpu::template stride_iterator<iterator> left, cpu::template stride_iterator<iterator> right )
        requires std::sentinel_for<iterator,iterator>
    {
        return left.base() == right.base();
    }

    template < class iterator >
    constexpr std::compare_three_way_result_t<iterator,iterator> operator <=> ( cpu::template stride_iterator<iterator> left, cpu::template stride_iterator<iterator> right )
        requires std::totally_ordered<iterator>
    {
        if constexpr ( debug )
        {
            if ( left.stride() != right.stride() )
                throw value_error("cannot compare stride_iterator: stride mismatches (with left.stride() = {}, right.stride() = {})", left.stride(), right.stride());
            if ( left.stride() == 0 )
                throw value_error("cannot compare stride_iterator: stride is zero (with left.stride() = {}, right.stride() = {})", left.stride(), right.stride());
        }

        return left.stride() >= 0 ? (left .base() <=> right.base()) :
                                    (right.base() <=> left .base());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator> operator + ( cpu::template stride_iterator<iterator> left, std::iter_difference_t<iterator> right )
        requires std::random_access_iterator<iterator>
    {
        return cpu::template stride_iterator<iterator>(left.base() + left.stride() * right, left.stride());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator> operator + ( std::iter_difference_t<iterator> left, cpu::template stride_iterator<iterator> right )
        requires std::random_access_iterator<iterator>
    {
        return cpu::template stride_iterator<iterator>(left * right.stride() + right.base(), right.stride());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator> operator - ( cpu::template stride_iterator<iterator> left, std::iter_difference_t<iterator> right )
        requires std::random_access_iterator<iterator>  
    {
        return cpu::template stride_iterator<iterator>(left.base() - left.stride() * right, left.stride());
    }

    template < class iterator >
    constexpr std::iter_difference_t<iterator> operator - ( cpu::template stride_iterator<iterator> left, cpu::template stride_iterator<iterator> right )
        requires std::random_access_iterator<iterator>
    {
        if constexpr ( debug )
        {
            if ( left.stride() != right.stride() )
                throw value_error("cannot compare stride_iterator: stride mismatches (with left.stride() = {}, right.stride() = {})", left.stride(), right.stride());
            if ( left.stride() == 0 )
                throw value_error("cannot compare stride_iterator: stride is zero (with left.stride() = {}, right.stride() = {})", left.stride(), right.stride());
        }

        return (left.base() - right.base()) / left.stride();
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>& operator += ( cpu::template stride_iterator<iterator>& left, std::iter_difference_t<iterator> right )
        requires std::random_access_iterator<iterator>
    {
        return left = cpu::template stride_iterator<iterator>(left.base() + right, left.stride());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>& operator -= ( cpu::template stride_iterator<iterator>& left, std::iter_difference_t<iterator> right )
        requires std::random_access_iterator<iterator>
    {
        return left = cpu::template stride_iterator<iterator>(left.base() - right, left.stride());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>& operator ++ ( cpu::template stride_iterator<iterator>& left )
        requires std::bidirectional_iterator<iterator>
    {
        if constexpr ( std::random_access_iterator<iterator> )
            return left = cpu::template stride_iterator<iterator>(left.base() + left.stride(), left.stride());
        else
            return left = cpu::template stride_iterator<iterator>([&] { auto iter = left.base(); std::advance(iter, left.stride()); return iter; } (), left.stride());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator> operator ++ ( cpu::template stride_iterator<iterator>& left, int )
        requires std::bidirectional_iterator<iterator>
    {
        auto tmp = left;
        ++left;
        return tmp;
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator>& operator -- ( cpu::template stride_iterator<iterator>& left )
        requires std::bidirectional_iterator<iterator>
    {
        if constexpr ( std::random_access_iterator<iterator> )
            return left = cpu::template stride_iterator<iterator>(left.base() - left.stride(), left.stride());
        else
            return left = cpu::template stride_iterator<iterator>([&] { auto iter = left.base(); std::advance(iter, -left.stride()); return iter; } (), left.stride());
    }

    template < class iterator >
    constexpr cpu::template stride_iterator<iterator> operator -- ( cpu::template stride_iterator<iterator>& left, int )
        requires std::bidirectional_iterator<iterator>
    {
        auto tmp = left;
        --left;
        return tmp;
    }
}