import anonymous;
import std;

int dep = 0;
auto engine = std::mt19937(std::random_device()());

__attribute__((noinline))
void func ( )
{
    if ( std::uniform_real_distribution(0.0, 1.0)(engine) <= 0.99 )
    {
        std::println("count {}", ++dep);
        return func();
    }
    else
    {
        std::println("OH NO");
        std::println("hello {}", *static_cast<int*>(nullptr));
    }
}

int main()
{
    func();
}