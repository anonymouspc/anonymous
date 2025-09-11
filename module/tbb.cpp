module;
#undef in
#undef self
#include <tbb/tbb.h>
export module tbb;
// import std; This module might be depended by stdexec by std:feature.sender by std:feature by std.
import        hwloc;

export namespace tbb
{
    using ::tbb::concurrent_map;
    using ::tbb::concurrent_priority_queue;
    using ::tbb::concurrent_queue;
    using ::tbb::concurrent_set;
    using ::tbb::concurrent_unordered_map;
    using ::tbb::concurrent_unordered_set;
    using ::tbb::tbb_allocator;
}