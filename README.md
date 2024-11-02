# FontTools

This Github repository was made to make it easier for you to decrease the size of font files to make it quicker to load them into web applications. This github repository reads all the fonts from the `input-folder`, which should contain `ttf` font files that have extra characters that you don't need inside the font file, and outputs the truncated font files into the `output-fonts` folder. 

**Note**: The `requirements.txt` file was made on a Windows system.

**Note**: In order to run the `pyftsubset` command, you will need to `pip install fonttool`