module;
#if __has_include(<unistd.h>)
#include <unistd.h>
#endif

export module system;
#ifdef __linux__
export import       :linux;
#endif
#ifdef __MACH__
export import       :macos;
#endif
#ifdef _POSIX_VERSION
export import       :posix;
#endif
#ifdef _WIN32
export import       :windows;
#endif
#ifdef __wasm__
export import       :wasm;
#endif