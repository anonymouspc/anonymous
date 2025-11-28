export module compiler;
#ifdef __clang__
export import         :clang;
#endif
#ifdef __EMSCRIPTEN__
export import         :emcc;
#endif
#ifdef __GNUC__
export import         :gcc;
#endif
#ifdef _MSC_VER
export import         :msvc;
#endif
