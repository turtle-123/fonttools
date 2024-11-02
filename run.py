import os
# Unicode glyphs to keep in output font

unicodes = "U+0020-007F,U+00A0-00FF,U+2010-201F,U+2020-2027,U+2030-203E,U+2044,U+20AC,U+2122,U+2190-2199,U+2200-22FF,U+25A0-25FF,U+2600-26FF"
for filename in os.listdir(os.path.join(os.path.curdir,"input-fonts")):
    path_to_input_file =  os.path.join(os.path.curdir,"input-fonts",filename)
    path_to_output_file =  os.path.join(os.path.curdir,"output-fonts",filename.replace(".ttf",".woff2"))
    cmd = f'pyftsubset \"" + path_to_input_file + "\" --unicodes=\"{unicodes}\" --output-file=\"" + path_to_output_file +"\"  --flavor=\"woff2\" --ignore-missing-glyphs --verbose'
    os.system(cmd)
