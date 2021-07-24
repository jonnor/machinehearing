
slides.html: Makefile presentation.md style.css
	pandoc -t revealjs -s presentation.md -o slides.html --slide-level=2 --mathml -V theme=white

slides.pdf: Makefile presentation.md
	pandoc -t beamer -s presentation.md -o slides.pdf --slide-level=2 --mathml --dpi 144

all: slides.html slides.pdf
