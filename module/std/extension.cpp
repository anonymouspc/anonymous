module;
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wreserved-module-identifier"
#endif

export module std:extension;
export import    :extension.assert;
export import    :extension.formatter;
export import    :extension.numeric;