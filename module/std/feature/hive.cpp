module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif

export module std:feature.hive;
import           :compiler;
export import plf;

export namespace std
{
    using namespace ::plf;
}
