import fmt;
import std;
import assert;

int main ( )
{
    assert(fmt::format("Hello, {}!", "fmt") == "Hello, fmt!");
}