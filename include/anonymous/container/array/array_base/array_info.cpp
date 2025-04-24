namespace detail
{
    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr array_info<type,dim,device>::array_info ( const auto&... args )
    {
        static_assert(sizeof...(args) == dim or sizeof...(args) == dim + 1);
        for_constexpr<1,dim>([&] <int index> { shp[index] = index_value_of<index>(args...); });
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr array_info<type,dim,device>::array_info ( const static_array<int,dim>& args )
        extends shp ( args )
    {

    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr int array_info<type,dim,device>::size ( ) const
    {
        auto s = 1;
        for_constexpr<1,dim>([&] <int index> { s *= shp[index]; });
        return s;
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr static_array<int,dim> array_info<type,dim,device>::shape ( ) const
    {
        return shp;
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr int array_info<type,dim,device>::row ( ) const
    {
        return shp[1];
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr int array_info<type,dim,device>::column ( ) const
        requires ( dim == 2 )
    {
        return shp[2];
    }
    
    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr bool array_info<type,dim,device>::empty ( ) const
    {
        auto e = false;
        for_constexpr<1,dim>([&] <int index> { if (shp[index] == 0) e = true; });
        return e;
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr array_info<type,dim,device>& array_info<type,dim,device>::clear ( )
    {
        for_constexpr<1,dim>([&] <int index> { shp[index] = 0; });
        return self;
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    constexpr array_info<type,dim,device>& array_info<type,dim,device>::resize ( const static_array<int,dim>& new_shape )
    {
        shp = new_shape;
        return self;
    }

    template < class type, int dim, class device >
        requires ( dim >= 2 )
    template < int axis >
    constexpr int array_info<type,dim,device>::get_size_axis ( ) const
    {
        static_assert ( axis >= 1 and axis <= dim );
        return shp[axis];
    }
} // namespace detail
