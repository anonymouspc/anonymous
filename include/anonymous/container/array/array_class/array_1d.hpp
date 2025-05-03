template < class type, class device >
class array<type,1,device>
    extends private device::template vector<type>,      // (Static  extends) Data storage.
            private detail::array_upper<type,1,device>, // (Dyanmic extends) Manages the upper-dimension host arrays. Only transposable.
            public  array_algo<array<type,1,device>,type,1,device>
{
    private: // Precondition
        static_assert ( not is_const<type> and not is_volatile<type> and not is_reference<type> );
        static_assert ( default_initializable<type> );
        static_assert ( not ( same_as<device,cpu> and same_as<type,bool> ) ); // std::vector<bool>.

    public: // Base
        using base  = device::template vector<type>;
        using upper = detail::array_upper<type,1,device>;

    public: // Typedef
        using  value_type      = device::template value_type          <type>;
        using  reference       = device::template reference           <type>;
        using  const_reference = device::template const_reference     <type>;
        using  pointer         = device::template pointer             <type>;
        using  const_pointer   = device::template const_pointer       <type>;
        using  iterator        = device::template stride_pointer      <type>;
        using  const_iterator  = device::template const_stride_pointer<type>;
        using  device_type     = device;
        struct array_concept { };

    public: // Core
        constexpr          array ( ) = default;
        constexpr          array ( const array&  )                   requires copyable<type>;
        constexpr          array (       array&& );
        constexpr          array& operator = ( const array&  )       requires copyable<type>;
        constexpr          array& operator = (       array&& );

    public: // Constructor
        constexpr explicit array ( int );
        constexpr          array ( int, const type& )                requires copyable<type>;
        constexpr          array ( int, invocable_r<type>     auto );
        constexpr          array ( int, invocable_r<type,int> auto );
        constexpr          array ( std::initializer_list<type> )     requires copyable<type>;
        constexpr          array ( range<type> )                     requires copyable<type> and number_type<type>;

    public: // Conversion
        template < class type2, class device2 > constexpr          array ( const array<type2,1,device2>& ) requires convertible_to  <type2,type>;
        template < class type2, class device2 > constexpr explicit array ( const array<type2,1,device2>& ) requires constructible_to<type2,type>;

        public: // Memebr
        constexpr static int                  dimension     ( );
        constexpr        int                  size          ( )     const;
        constexpr        int                  capacity      ( )     const;
        constexpr        array<int>           shape         ( )     const;
        constexpr        int                  row           ( )     const = delete;
        constexpr        int                  column        ( )     const = delete;
        constexpr        bool                 empty         ( )     const;
        constexpr        pointer              data          ( );
        constexpr        const_pointer        data          ( )     const;
        constexpr        iterator             begin         ( );
        constexpr        const_iterator       begin         ( )     const;
        constexpr        iterator             end           ( );
        constexpr        const_iterator       end           ( )     const;
        constexpr        reference            operator []   ( int );
        constexpr        const_reference      operator []   ( int ) const;

    public: // Member
                                  constexpr array& clear  ( );
                                  constexpr array& resize ( int );
                                  constexpr array& resize ( array<int> );
        template < int axis = 1 > constexpr array& push   ( type )       requires ( axis == 1 or axis == -1 );
        template < int axis = 1 > constexpr array& pop    ( int = -1 )   requires ( axis == 1 or axis == -1 );
        template < int axis = 1 > constexpr array& insert ( int, type )  requires ( axis == 1 or axis == -1 );
        template < int axis = 1 > constexpr array& erase  ( int, int )   requires ( axis == 1 or axis == -1 );
        
    public: // View
        constexpr       array<type,1,device>& flatten   ( );
        constexpr const array<type,1,device>& flatten   ( ) const;
        constexpr       array<type,1,device>& transpose ( )       = delete;
        constexpr const array<type,1,device>& transpose ( ) const = delete;

    public: // Memory
        constexpr bool ownership  ( ) const;
        constexpr bool contiguous ( ) const;

    public: // Mdspan
        constexpr       auto mdspan ( );
        constexpr const auto mdspan ( ) const;

    private: // Detail
                              constexpr       int                                              get_size_top  ( )                        const = delete;
        template < int axis > constexpr       int                                              get_size_axis ( )                        const = delete;
                              constexpr       detail::array_shape<1>                           get_shape     ( )                        const = delete;
        template < int dim2 > constexpr       std::span<detail::array_upper<type,dim2,device>> get_rows      ( int_type auto... )             = delete;
        template < int dim2 > constexpr const std::span<detail::array_upper<type,dim2,device>> get_rows      ( int_type auto... )       const = delete;
        template < int dim2 > constexpr       std::span<detail::array_upper<type,dim2,device>> get_columns   ( int_type auto... )             = delete;
        template < int dim2 > constexpr const std::span<detail::array_upper<type,dim2,device>> get_columns   ( int_type auto... )       const = delete;
                              constexpr       reference                                        get_value     ( int_type auto... )             = delete;
                              constexpr       const_reference                                  get_value     ( int_type auto... )       const = delete;
                              constexpr       pointer                                          get_pointer   ( )                              = delete;
                              constexpr       const_pointer                                    get_pointer   ( )                        const = delete;
                              constexpr       void                                             set_resize    ( detail::array_shape<1> )       = delete;
  
    private: // Friend
        template < class type2, int dim2, class device2 > friend class array;
        template < class type2, int dim2, class device2 > friend class detail::array_lower;
        template < class type2, int dim2, class device2 > friend class detail::array_upper;
        template < class type2, int dim2, class device2 > friend class detail::array_line_iterator;
        template < class type2, int dim2, class device2 > friend class detail::array_line_const_iterator;

    protected: // ADL
        template < class type2, class device2 = cpu > using vector = array<type2,1,device2>; // Redirect to global array instead of extended one.
};