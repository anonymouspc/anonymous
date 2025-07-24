import anonymous;
import std;
import boost.core;

auto operator | ( std::execution::sender auto&& lhs, auto&& rhs )
{
    return rhs(lhs);
}

using namespace anonymous;

int main ( )
{
    auto a = [] (auto&&...) { std::println("{}", "hello"); };
    a(1, 2, 3);
    auto task1 = std::execution::schedule(system::execution_context.get_scheduler());
    auto task2 = std::move(task1)
               | std::execution::then([] (auto&&...) { std::println("{}", std::this_thread::get_id()); });
    std::execution::sync_wait(std::move(task2));
}