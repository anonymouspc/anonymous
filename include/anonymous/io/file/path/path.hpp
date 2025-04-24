class path
    extends public string
{
    public: // Core
        using string::string;

    public: // Conversion
        path   ( std::filesystem::path );
        operator std::filesystem::path ( ) const;

    public: // Member
        path absolute_path ( )      const;
        path relative_path ( )      const;
        path parent_path   ( )      const;
        path child_path    ( path ) const;
        path root_path     ( )      const;

    public: // Iterator
        const array<path> dir  ( ) const;
        const array<path> ls   ( ) const;
        const array<path> tree ( ) const;
};

bool operator == ( const path&, const path& );



#ifdef dll
    #include "path.cpp"
#endif