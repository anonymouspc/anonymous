def get_context():
    return _context

def set_context(name):
    global _context
    _context = name

_context = "real"