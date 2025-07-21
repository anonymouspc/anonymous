import std;
import ctre;

int main ( )
{
    std::cout << ctre::match<"[a-z]+">("hello") << std::endl;
}