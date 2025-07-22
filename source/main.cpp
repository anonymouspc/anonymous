import anonymous;
import xlnt;
using namespace anonymous;

int main ( )
{
    auto workbook = xlnt::workbook();
    auto worksheet = workbook.active_sheet();
    for ( int i in range(1, 100) ) 
        for ( int j in range(1, 100) )
            worksheet.cell(i, j).value(i + j);
    workbook.save("hello.xlsx");
}