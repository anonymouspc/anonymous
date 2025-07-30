from common.config import argv
from common.error  import LogicError
from common.make   import meson
import common.config
import sys

async def initialize():
    if not argv.enable_ui:
        raise LogicError("arg `--disable-ui` set but package `cairo` imported")
    
    if sys.platform == "win32":
        raise LogicError("not coded yet")
    elif sys.platform == "linux":
        common.config.link_flags += ["-lgtk"]
    elif sys.platform == "darwin":
        common.config.link_flags += [
            "-framework CoreFoundation",
            "-framework CoreGraphics", 
            "-framework CoreText",
            "-framework AppKit",
            "-L/opt/homebrew/lib -lwebp -lexpat"
        ]
    common.config.define_flags["ENABLE_UI"] = "true"

async def build():
    await meson(
        name="cairo",
        dir="./package/cairo",
        args=[
            "-Ddwrite=enabled",
            "-Dfontconfig=enabled",
            "-Dfreetype=enabled",
            "-Dpng=enabled",
            "-Dquartz=auto",
            "-Dtee=auto",
            "-Dxcb=auto",
            "-Dxlib=auto",
            "-Dxlib-xcb=auto",
            "-Dzlib=enabled",
            "-Dtests=disabled",
            "-Dlzo=auto",
            "-Dgtk2-utils=disabled",
            "-Dglib=disabled",
            "-Dspectre=disabled",
            "-Dsymbol-lookup=disabled",
            "-Dgtk_doc=false"
        ]
    )

"""
>>> cat package/cairo/meson.options 
# Cairo font backends
option('dwrite', type : 'feature', value : 'auto')
option('fontconfig', type : 'feature', value : 'auto')
option('freetype', type : 'feature', value : 'auto')

# Cairo surface backends
option('png', type : 'feature', value : 'auto') # png and svg surfaces
option('quartz', type : 'feature', value : 'auto')
option('tee', type : 'feature', value : 'auto')
option('xcb', type : 'feature', value : 'auto')
option('xlib', type : 'feature', value : 'auto')
option('xlib-xcb', type : 'feature', value : 'disabled')
option('zlib', type : 'feature', value : 'auto') # script, ps, pdf, xml surfaces

# Tests
option('tests', type : 'feature', value : 'auto')

# Util deps
option('lzo', type : 'feature', value : 'auto')
option('gtk2-utils', type : 'feature', value : 'disabled')

# Misc deps
option('glib', type : 'feature', value : 'auto')
option('spectre', type : 'feature', value : 'auto')
option('symbol-lookup', type: 'feature', value : 'auto',
       description: 'Symbol lookup in debug utils via binutils/bfd')

# Documentation
option('gtk_doc', type : 'boolean', value : false,
       description: 'Build the Cairo API reference (depends on gtk-doc)')
"""