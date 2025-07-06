import scn;
import std;
import assert;

int main ( )
{
    assert(scn::scan<int,int,int>(
               "12 34 56",
               "{} {} {}"
           )->values() == std::tuple(12, 34, 56));

    assert(scn::scan<int,double>(
               "hello, first number = 12.0, second number = 34",
               "hello, first number = {1}, second number = {0}"
           )->values() == std::tuple(34, 12.0)); 
}