import anonymous;

int main ( )
{
    auto stream = tcp_stream();
    co_await stream.async_read(ptr, 20);
    
}