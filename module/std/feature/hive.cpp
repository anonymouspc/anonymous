export module std:feature.hive;
import           :compiler;
export import plf;

export namespace std
{
    using namespace plf;
    namespace pmr
    {
        template < class type >
        using hive = plf::hive<type,std::pmr::polymorphic_allocator<type>>;
    }
}
