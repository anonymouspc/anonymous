module;
#include <dlfcn.h>
#include <unistd.h>

export module system:posix;
export
{
    using ::dladdr;
    using ::Dl_info;
}