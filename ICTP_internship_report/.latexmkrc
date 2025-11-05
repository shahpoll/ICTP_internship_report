$pdf_mode = 1;

# Enable shell-escape so minted and other external tools work out of the box
$latex = 'pdflatex %O -interaction=nonstopmode -synctex=1 -file-line-error -shell-escape %S';

# Automatically run biber when biblatex needs it
$bibtex = 'biber %O %B';

# Keep intermediate files in build/
$aux_dir = 'build';
$out_dir = 'build';

@default_files = ('main.tex');

push @generated_exts, qw(bbl bcf blg run.xml synctex.gz);
