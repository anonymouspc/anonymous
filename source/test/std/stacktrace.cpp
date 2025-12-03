import std;

int main ( )
{
    auto trace = std::stacktrace::current();
    assert(0 < trace.size() and trace.size() < 10, std::format("trace.size() = {}", trace.size()));
}