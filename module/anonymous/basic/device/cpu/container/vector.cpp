export module anonymous:basic.device.cpu:container.vector;
import                                  :container.detail.enum_bool;
import                                  :common.cpu;
import        std;

export namespace anonymous
{
    template < class type, class alloc >
    class cpu::vector
        extends public std::vector<type,alloc>
    {

    };

    template < class alloc >
    class cpu::vector<bool,alloc>
        extends public std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_alloc<enum_bool>>
    {
        public: // Typedef
            using value_type      =       bool;
            using reference       =       bool&;
            using const_reference = const bool&;
            using pointer         =       bool*;
            using const_pointer   = const bool*;
            using iterator        =       bool*;
            using const_iterator  = const bool*;

        public: // Core
            constexpr vector ( size_t, bool );
            constexpr vector ( std::initializer_list<bool> );

        public: // Member 
            constexpr iterator        begin       ( );
            constexpr const_iterator  begin       ( )             const;
            constexpr iterator        end         ( );
            constexpr const_iterator  end         ( )             const;
            constexpr pointer         data        ( );
            constexpr const_pointer   data        ( )             const;
            constexpr reference       front       ( );
            constexpr const_reference front       ( )             const;
            constexpr reference       back        ( );
            constexpr const_reference back        ( )             const;
            constexpr reference       at          ( size_t );
            constexpr const_reference at          ( size_t ) const;
            constexpr reference       operator [] ( size_t );
            constexpr const_reference operator [] ( size_t ) const;

            constexpr void            resize       ( size_t );
            constexpr void            resize       ( size_t, bool );
            constexpr iterator        insert       ( const_iterator, bool );
            constexpr iterator        insert       ( const_iterator, size_t, bool );
            constexpr iterator        erase        ( const_iterator );
            constexpr iterator        erase        ( const_iterator, const_iterator );
            constexpr iterator        emplace      ( const_iterator, auto&&... );
            constexpr void            push_back    ( bool );
            constexpr void            pop_back     ( );
            constexpr reference       emplace_back ( auto&&... );
    };



    template < class alloc >
    constexpr cpu::vector<bool,alloc>::vector ( size_t init_size, bool init_value )
        extends std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>> ( init_size, init_value )
    {

    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::vector ( std::initializer_list<bool> init_value )
        extends std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>> ( reinterpret_cast<const enum_bool*>(init_value.begin()), reinterpret_cast<const enum_bool*>(init_value.end()) )
    {

    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::begin ( )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::data());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_iterator cpu::vector<bool,alloc>::begin ( ) const
    {
        return reinterpret_cast<const_iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::data());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::end ( )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::data() + std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::size());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_iterator cpu::vector<bool,alloc>::end ( ) const
    {
        return reinterpret_cast<const_iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::data() + std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::size());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::data ( )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::data());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_iterator cpu::vector<bool,alloc>::data ( ) const
    {
        return reinterpret_cast<const_iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::data());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::reference cpu::vector<bool,alloc>::front ( )
    {
        return reinterpret_cast<reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::front());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_reference cpu::vector<bool,alloc>::front ( ) const
    {
        return reinterpret_cast<const_reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::front());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::reference cpu::vector<bool,alloc>::back ( )
    {
        return reinterpret_cast<reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::back());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_reference cpu::vector<bool,alloc>::back ( ) const
    {
        return reinterpret_cast<const_reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::back());
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::reference cpu::vector<bool,alloc>::at ( size_t pos )
    {
        return reinterpret_cast<reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::at(pos));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_reference cpu::vector<bool,alloc>::at ( size_t pos ) const
    {
        return reinterpret_cast<const_reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::at(pos));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::reference cpu::vector<bool,alloc>::operator [] ( size_t pos )
    {
        return reinterpret_cast<reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::operator[](pos));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::const_reference cpu::vector<bool,alloc>::operator [] ( size_t pos ) const
    {
        return reinterpret_cast<const_reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::operator[](pos));
    }

    template < class alloc >
    constexpr void cpu::vector<bool,alloc>::resize ( size_t new_size )
    {
        std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::resize(new_size);
    }

    template < class alloc >
    constexpr void cpu::vector<bool,alloc>::resize ( size_t new_size, bool new_value )
    {
        std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::resize(new_size, static_cast<enum_bool>(new_value));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::insert ( const_iterator it, bool new_value )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::insert(reinterpret_cast<std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::const_iterator>(it), static_cast<enum_bool>(new_value)));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::insert ( const_iterator it, size_t new_size, bool new_value )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::insert(reinterpret_cast<std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::const_iterator>(it), new_size, static_cast<enum_bool>(new_value)));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::erase ( const_iterator it )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::erase(reinterpret_cast<std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::const_iterator>(it)));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::erase ( const_iterator it1, const_iterator it2 )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::erase(reinterpret_cast<std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::const_iterator>(it1), reinterpret_cast<std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::const_iterator>(it2)));
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::iterator cpu::vector<bool,alloc>::emplace ( const_iterator it, auto&&... new_value )
    {
        return reinterpret_cast<iterator>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::insert(reinterpret_cast<std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::const_iterator>(it), static_cast<enum_bool>(bool(std::forward<decltype(new_value)>(new_value)...))));
    }

    template < class alloc >
    constexpr void cpu::vector<bool,alloc>::push_back ( bool new_value )
    {
        std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::push_back(static_cast<enum_bool>(new_value));
    }

    template < class alloc >
    constexpr void cpu::vector<bool,alloc>::pop_back ( )
    {
        std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::pop_back();
    }

    template < class alloc >
    constexpr cpu::vector<bool,alloc>::reference cpu::vector<bool,alloc>::emplace_back ( auto&&... new_value )
    {
        return reinterpret_cast<reference>(std::vector<enum_bool,typename std::allocator_traits<alloc>::template rebind_allocator<enum_bool>>::reference(static_cast<enum_bool>(bool(std::forward<decltype(new_value)>(new_value)...))));
    }
}