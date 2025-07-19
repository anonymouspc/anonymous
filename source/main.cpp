import stdexec;
import std;
int main ( )
{
    std::cout << ctre::match<"[a-z]+">("hello") << std::endl;
}