class Web:
    name = "web"
    executable_suffix = ".html"
    static_suffix     = ""
    shared_suffix     = ""
    default_compiler  = "em++"
    env               = {}
    env_seperator     = ""

    def check():
        assert False, "system not checkable"