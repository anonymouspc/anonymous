module;
#undef in
#undef self
#ifdef __clang__
    #pragma clang diagnostic ignored "-Wdeprecated-declarations"
#endif
#include <elements.hpp>

export module elements;
import        std;
import        cairo;

export namespace elements
{
    using cycfi::elements::align_left_top;
    using cycfi::elements::app;
    using cycfi::elements::basic_text_box;
    using cycfi::elements::font_descr;
    using cycfi::elements::hsize;
    using cycfi::elements::image;
    using cycfi::elements::margin;
    using cycfi::elements::port;
    using cycfi::elements::scroller;
    using cycfi::elements::view;
    using cycfi::elements::window;
}