export module anonymous:basic.device.cpu.impl.iterator.transform_iterator;
import                 :basic.device.cpu.decl;
import                 :basic.concepts;
import        std;

export namespace anonymous
{
    template < class iterator, class function >
    class cpu::transform_iterator
    {
        public: // Typedef
            using iterator_category = common_type<typename std::iterator_traits<iterator>::iterator_category,std::random_access_iterator_tag>;
            using value_type        = remove_cvref<invoke_result<function,typename std::iterator_traits<iterator>::value_type>>;
            using reference         = invoke_result<function,typename std::iterator_traits<iterator>::reference>;
            using difference_type   = std::iterator_traits<iterator>::difference_type;

        private: // Data
            iterator iter = iterator();
            function func = function();

        public: // Core
            constexpr transform_iterator ( )                          requires default_initializable<iterator> and default_initializable<function> = default;
            constexpr transform_iterator ( iterator )                 requires default_initializable<function>;
            constexpr transform_iterator ( iterator, function );

        public: // Member
            constexpr reference operator *  ( )                 const;
            constexpr reference operator [] ( difference_type ) const requires random_access_iterator<iterator>;

        public: // Access
            constexpr iterator base      ( ) const;
            constexpr function transform ( ) const;
    };

    template < class iterator, class function > constexpr bool                                                 operator ==  ( cpu::template transform_iterator<iterator,function>,  cpu::template transform_iterator<iterator,function> ) requires equalable             <iterator>;
    template < class iterator, class function > constexpr compare_result                  <iterator,iterator>  operator <=> ( cpu::template transform_iterator<iterator,function>,  cpu::template transform_iterator<iterator,function> ) requires comparable            <iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>  operator +   ( cpu::template transform_iterator<iterator,function>,  iterator_difference_type        <iterator>          ) requires random_access_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>  operator +   ( iterator_difference_type        <iterator>,           cpu::template transform_iterator<iterator,function> ) requires random_access_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>  operator -   ( cpu::template transform_iterator<iterator,function>,  iterator_difference_type        <iterator>          ) requires random_access_iterator<iterator>;
    template < class iterator, class function > constexpr iterator_difference_type        <iterator>           operator -   ( cpu::template transform_iterator<iterator,function>,  cpu::template transform_iterator<iterator,function> ) requires random_access_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>& operator +=  ( cpu::template transform_iterator<iterator,function>&, iterator_difference_type        <iterator>          ) requires random_access_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>& operator -=  ( cpu::template transform_iterator<iterator,function>&, iterator_difference_type        <iterator>          ) requires random_access_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>& operator ++  ( cpu::template transform_iterator<iterator,function>&                                                      ) requires bidirectional_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>  operator ++  ( cpu::template transform_iterator<iterator,function>&, int                                                 ) requires bidirectional_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>& operator --  ( cpu::template transform_iterator<iterator,function>&                                                      ) requires bidirectional_iterator<iterator>;
    template < class iterator, class function > constexpr cpu::template transform_iterator<iterator,function>  operator --  ( cpu::template transform_iterator<iterator,function>&, int                                                 ) requires bidirectional_iterator<iterator>;



    template < class iterator, class function > 
    constexpr cpu::transform_iterator<iterator,function>::transform_iterator ( iterator init_iter )
        requires default_initializable<function>
        extends iter ( init_iter )
    {
        
    }

    template < class iterator, class function > 
    constexpr cpu::transform_iterator<iterator,function>::transform_iterator ( iterator init_iter, function init_func )
        extends iter ( init_iter ),
                func ( init_func )
    {
        
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function>::reference cpu::transform_iterator<iterator,function>::operator * ( ) const
    {
        return func(*iter);
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function>::reference cpu::transform_iterator<iterator,function>::operator [] ( difference_type offset ) const
        requires random_access_iterator<iterator>
    {
        return func(iter[offset]);
    }

    template < class iterator, class function >
    constexpr iterator cpu::transform_iterator<iterator,function>::base ( ) const
    {
        return iter;
    }

    template < class iterator, class function >
    constexpr function cpu::transform_iterator<iterator,function>::transform ( ) const
    {
        return func;
    }

    template < class iterator, class function > 
    constexpr bool operator == ( cpu::template transform_iterator<iterator,function> left, cpu::template transform_iterator<iterator,function> right )
        requires equalable<iterator>
    {
        return left.base() == right.base();
    }

    template < class iterator, class function >
    constexpr compare_result<iterator,iterator> operator <=> ( cpu::template transform_iterator<iterator,function> left, cpu::template transform_iterator<iterator,function> right )
        requires comparable<iterator>
    {
        return left.base() <=> right.base();
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function> operator + ( cpu::template transform_iterator<iterator,function> left, iterator_difference_type<iterator> right )
        requires random_access_iterator<iterator>
    {
        return cpu::template transform_iterator<iterator,function>(left.base() + right, left.transform());
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function> operator + ( iterator_difference_type<iterator> left, cpu::template transform_iterator<iterator,function> right )
        requires random_access_iterator<iterator>
    {
        return cpu::template transform_iterator<iterator,function>(left + right.base(), right.transform());
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function> operator - ( cpu::template transform_iterator<iterator,function> left, iterator_difference_type<iterator> right )
        requires random_access_iterator<iterator>  
    {
        return cpu::template transform_iterator<iterator,function>(left.base() - right, left.transform());
    }

    template < class iterator, class function >
    constexpr iterator_difference_type<iterator> operator - ( cpu::template transform_iterator<iterator,function> left, cpu::template transform_iterator<iterator,function> right )
        requires random_access_iterator<iterator>
    {
        return left.base() - right.base();
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function>& operator += ( cpu::template transform_iterator<iterator,function>& left, std::iter_difference_t<iterator> right )
        requires random_access_iterator<iterator>
    {
        return left = cpu::template transform_iterator<iterator,function>(left.base() + right, std::move(left.transform()));
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function>& operator -= ( cpu::template transform_iterator<iterator,function>& left, std::iter_difference_t<iterator> right )
        requires random_access_iterator<iterator>
    {
        return left = cpu::template transform_iterator<iterator,function>(left.base() - right, std::move(left.transform()));
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function>& operator ++ ( cpu::template transform_iterator<iterator,function>& left )
        requires bidirectional_iterator<iterator>
    {
        auto tmp = left.base();
        ++tmp;
        return left = cpu::template transform_iterator<iterator,function>(std::move(tmp), std::move(left.transform()));
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function> operator ++ ( cpu::template transform_iterator<iterator,function>& left, int )
        requires bidirectional_iterator<iterator>
    {
        auto tmp = left;
        ++left;
        return tmp;
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function>& operator -- ( cpu::template transform_iterator<iterator,function>& left )
        requires bidirectional_iterator<iterator>
    {
        auto tmp = left.base();
        --tmp;
        return left = cpu::template transform_iterator<iterator,function>(std::move(tmp), std::move(left.transform()));
    }

    template < class iterator, class function >
    constexpr cpu::template transform_iterator<iterator,function> operator -- ( cpu::template transform_iterator<iterator,function>& left, int )
        requires bidirectional_iterator<iterator>
    {
        auto tmp = left;
        --left;
        return tmp;
    }  
}