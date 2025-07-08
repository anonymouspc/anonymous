// declare interface
export module test;
import        std;

export namespace mymodule {
    template<typename T>
    T add(T x, T y);

    std::string greetings();
}

// implement interface
module :private;

std::string mymodule::greetings() {
    return "hello";
}

template<typename T>
T mymodule::add(T x, T y) {
    return x + y;
}