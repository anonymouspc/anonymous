module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif

export module std.extension;
export import              :formatter;
export import              :numeric;