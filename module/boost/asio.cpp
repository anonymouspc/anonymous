module;
#undef in
#undef self
#include <boost/asio.hpp>
#include <boost/asio/ssl.hpp>

export module boost.asio;
import        boost.system;
import        openssl;
import        std;

export namespace boost::asio
{

}