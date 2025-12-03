export module std:extension.stdio;
import           :extension.detail.compat;

export
{
    auto stdin  = stdin_;
    auto stdout = stdout_;
    auto stderr = stderr_;
}