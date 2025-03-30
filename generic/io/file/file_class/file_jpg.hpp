#pragma once

class file_jpg
    extends public file_interface<file_jpg>,
            public matrix<color>
{
    public: // Core
        using file_interface<file_jpg>::file_interface;
        using matrix<color>::operator=;

    public: // Interface (override)
        file_jpg& open ( const path& );
        file_jpg& save ( );

    public: // Interface
              int& depth ( );
        const int& depth ( ) const;

    private: // Data
        int image_depth = 24;
};


#ifdef dll
    #include "file_jpg.cpp"
#endif