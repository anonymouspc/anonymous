module;
#include <csignal>

export module anonymous:basic.error.detail.signal_initializer;
import                 :basic.error.exception;

export namespace anonymous
{
    struct signal_initializer_type  
    {
        signal_initializer_type ( );

        static void signal_handler                          ( int, const char* );
        static void abort_signal_handler                    ( int );
        static void floating_point_exception_signal_handler ( int );
        static void illegal_instruction_signal_handler      ( int );
        static void interrupt_signal_handler                ( int );
        static void segmentation_violation_signal_handler   ( int );
        static void terminate_signal_handler                ( int );
    };


    
    signal_initializer_type::signal_initializer_type ( )
    {
        // Signal.standard
        std::signal(SIGFPE,  floating_point_exception_signal_handler);
        std::signal(SIGILL,  illegal_instruction_signal_handler);
        std::signal(SIGINT,  interrupt_signal_handler);
        std::signal(SIGSEGV, segmentation_violation_signal_handler);
        std::signal(SIGTERM, terminate_signal_handler);

        // Signal.posix
        #ifdef SIGALRM
        std::signal(SIGALRM,   [] (int s) { signal_handler(s, "SIGALRM (alarm clock)"); });
        #endif
        #ifdef SIGBUS
        std::signal(SIGBUS,    [] (int s) { signal_handler(s, "SIGBUS (access to an undefined portion of a memory object)"); });
        #endif
        #ifdef SIGHUP
        std::signal(SIGHUP,    [] (int s) { signal_handler(s, "SIGHUP (hangup)"); });
        #endif
        #ifdef SIGPIPE
        std::signal(SIGPIPE,   [] (int s) { signal_handler(s, "SIGPIPE (write on a pipe with no one to read it)"); });
        #endif
        #ifdef SIGPOLL
        std::signal(SIGPOLL,   [] (int s) { signal_handler(s, "SIGPOLL (pollable event)"); });
        #endif
        #ifdef SIGPROF
        std::signal(SIGPROF,   [] (int s) { signal_handler(s, "SIGPROF (profiling timer expired)"); });
        #endif
        #ifdef SIGQUIT
        std::signal(SIGQUIT,   [] (int s) { signal_handler(s, "SIGQUIT (terminal quit signal)"); });
        #endif
        #ifdef SIGSYS
        std::signal(SIGSYS,    [] (int s) { signal_handler(s, "SIGSYS (bad system call)"); });
        #endif
        #ifdef SIGTRAP
        std::signal(SIGTRAP,   [] (int s) { signal_handler(s, "SIGTRAP (trace/breakpoint trap)"); });
        #endif
        #ifdef SIGTSTP
        std::signal(SIGTSTP,   [] (int s) { signal_handler(s, "SIGTSTP (terminal stop signal)"); });
        #endif
        #ifdef SIGTTIN
        std::signal(SIGTTIN,   [] (int s) { signal_handler(s, "SIGTTIN (background process attempting read)"); });
        #endif
        #ifdef SIGTTOU
        std::signal(SIGTTOU,   [] (int s) { signal_handler(s, "SIGTTOU (background process attempting write)"); });
        #endif
        #ifdef SIGUSR1
        std::signal(SIGUSR1,   [] (int s) { signal_handler(s, "SIGUSR1 (user-defined signal 1)"); });
        #endif
        #ifdef SIGUSR2
        std::signal(SIGUSR2,   [] (int s) { signal_handler(s, "SIGUSR2 (user-defined signal 2)"); });
        #endif
        #ifdef SIGVTALRM
        std::signal(SIGVTALRM, [] (int s) { signal_handler(s, "SIGVTALRM (virtual timer expired)"); });
        #endif
        #ifdef SIGXCPU
        std::signal(SIGXCPU,   [] (int s) { signal_handler(s, "SIGXCPU (cpu time limit exceeded)"); });
        #endif
        #ifdef SIGXFSZ
        std::signal(SIGXCPU,   [] (int s) { signal_handler(s, "SIGXFSZ (file size limit exceeded)"); });
        #endif
    }

    void signal_initializer_type::signal_handler ( int, const char* msg )
    {
        throw signal("{}", msg);
    }

    void signal_initializer_type::abort_signal_handler ( int )
    {
        throw abort_signal("SIGABRT (process abort signal)");
    }

    void signal_initializer_type::floating_point_exception_signal_handler ( int )
    {
        throw floating_point_exception_signal("SIGFPE (erroneous arithmetic operation)");
    }

    void signal_initializer_type::illegal_instruction_signal_handler ( int )
    {
        throw illegal_instruction_signal("SIGILL (illegal instruction)");      
    }

    void signal_initializer_type::interrupt_signal_handler ( int )
    {
        throw interrupt_signal("SIGINT (terminal interrupt signal)");                
    }

    void signal_initializer_type::segmentation_violation_signal_handler ( int )
    {
        throw segmentation_violation_signal("SIGSEGV (invalid memory reference)");   
    }

    void signal_initializer_type::terminate_signal_handler ( int )
    {
        throw terminate_signal("SIGTERM (termination signal)");
    }
}