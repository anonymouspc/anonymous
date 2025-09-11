module;
#undef in
#undef self
#define BOOST_LOCALE_WITH_ICU
#include <boost/locale.hpp>

export module boost.locale;
import        std;
import        icu;

export namespace boost::locale
{
    
}