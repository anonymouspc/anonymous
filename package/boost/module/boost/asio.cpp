module;
#include <boost/asio.hpp>
#include <boost/asio/ssl.hpp>

export module boost.asio;
import        boost.system;
import        openssl;
import        std;

export namespace boost::asio
{
    using boost::asio::post;
    using boost::asio::system_context;
    using boost::asio::system_executor;
}