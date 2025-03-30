#pragma once

class file_pnm
    extends public file_interface<file_pnm>,
            public matrix<color>
{
    public: // Core
        using file_interface<file_pnm>::file_interface;
        using matrix<color>::operator=;

    public: // Interface (override)
        file_pnm& open ( const path& );
        file_pnm& save ( );

    public: // Interface
              int& depth ( );
        const int& depth ( ) const;

    private: // Data
        int image_depth = 32;
};

#ifdef dll
    #include "file_pnm.cpp"
#endif