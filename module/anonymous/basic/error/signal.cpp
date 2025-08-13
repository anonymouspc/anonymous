module;
#include <csignal>

export module anonymous:basic.error.signal;
import                 :basic.error.exception;
import        std;

export namespace anonymous
{
    struct signal_initializer_type
    {
        signal_initializer_type ( );
    };

    inline auto signal_initializer = signal_initializer_type();



    signal_initializer_type::signal_initializer_type ( )
    {
        // standard
        #ifdef SIGFPE
        std::signal(SIGFPE,    [] (int s) { throw signal("SIGFPE (erroneous arithmetic operation)"); });
        #endif
        #ifdef SIGILL
        std::signal(SIGILL,    [] (int s) { throw signal("SIGILL (illegal instruction)"); });
        #endif
        #ifdef SIGINT
        std::signal(SIGINT,    [] (int s) { throw signal("SIGINT (terminal interrupt signal)"); });
        #endif
        #ifdef SIGSEGV
        std::signal(SIGSEGV,   [] (int s) { throw signal("SIGSEGV (invalid memory reference)"); });
        #endif
        #ifdef SIGTERM
        std::signal(SIGTERM,   [] (int s) { throw signal("SIGTERM (termination signal)"); });
        #endif

        // posix
        #ifdef SIGALRM
        std::signal(SIGALRM,   [] (int s) { throw signal("SIGALRM (alarm clock)"); });
        #endif
        #ifdef SIGBUS
        std::signal(SIGBUS,    [] (int s) { throw signal("SIGBUS (access to an undefined portion of a memory object)"); });
        #endif
        #ifdef SIGHUP
        std::signal(SIGHUP,    [] (int s) { throw signal("SIGHUP (hangup)"); });
        #endif
        #ifdef SIGPIPE
        std::signal(SIGPIPE,   [] (int s) { throw signal("SIGPIPE (write on a pipe with no one to read it)"); });
        #endif
        #ifdef SIGPOLL
        std::signal(SIGPOLL,   [] (int s) { throw signal("SIGPOLL (pollable event)"); });
        #endif
        #ifdef SIGPROF
        std::signal(SIGPROF,   [] (int s) { throw signal("SIGPROF (profiling timer expired)"); });
        #endif
        #ifdef SIGQUIT
        std::signal(SIGQUIT,   [] (int s) { throw signal("SIGQUIT (terminal quit signal)"); });
        #endif
        #ifdef SIGSYS
        std::signal(SIGSYS,    [] (int s) { throw signal("SIGSYS (bad system call)"); });
        #endif
        #ifdef SIGTRAP
        std::signal(SIGTRAP,   [] (int s) { throw signal("SIGTRAP (trace/breakpoint trap)"); });
        #endif
        #ifdef SIGTSTP
        std::signal(SIGTSTP,   [] (int s) { throw signal("SIGTSTP (terminal stop signal)"); });
        #endif
        #ifdef SIGTTIN
        std::signal(SIGTTIN,   [] (int s) { throw signal("SIGTTIN (background process attempting read)"); });
        #endif
        #ifdef SIGTTOU
        std::signal(SIGTTOU,   [] (int s) { throw signal("SIGTTOU (background process attempting write)"); });
        #endif
        #ifdef SIGUSR1
        std::signal(SIGUSR1,   [] (int s) { throw signal("SIGUSR1 (user-defined signal 1)"); });
        #endif
        #ifdef SIGUSR2
        std::signal(SIGUSR2,   [] (int s) { throw signal("SIGUSR2 (user-defined signal 2)"); });
        #endif
        #ifdef SIGVTALRM
        std::signal(SIGVTALRM, [] (int s) { throw signal("SIGVTALRM (virtual timer expired)"); });
        #endif
        #ifdef SIGXCPU
        std::signal(SIGXCPU,   [] (int s) { throw signal("SIGXCPU (cpu time limit exceeded)"); });
        #endif
        #ifdef SIGXFSZ
        std::signal(SIGXCPU,   [] (int s) { throw signal("SIGXFSZ (file size limit exceeded)"); });
        #endif
    }
}

