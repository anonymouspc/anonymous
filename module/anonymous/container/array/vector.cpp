export module anonymous.container.array.vector;
import        anonymous.basic.container.array.detail.array_declaration;

template < class type, class device >
using vector = array<type,1,device>;

template < class type, class device >
class array<type,1,device>
{

};