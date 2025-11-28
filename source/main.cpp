import std;

[[clang::noinline]]
template < class... types >
void func ( )
{
    if constexpr ((sizeof...(types)) <= 10)
    {
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
        return func<types...,int>();
    }
    else
        std::cout << "===========" << std::stacktrace::current();
}

int main ( )
{
    func();
}


