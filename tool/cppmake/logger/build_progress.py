class BuildProgressLogger:
    def log(self, prefix, target):
        if not hasattr(target.__class__, "current"):
               setattr(target.__class__, "current", 0)
        target.__class__.current += 1
        print(f"{prefix} [{target.current}/{len(target.__class__.tasks)}]: {target.name}")

build_progress_logger = BuildProgressLogger()