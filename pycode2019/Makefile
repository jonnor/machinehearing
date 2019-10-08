
slides:
	pandoc -t revealjs -s presentation.md -o slides.html --slide-level=2 --mathml -V center=false

slides.pdf:
	pandoc -t beamer -s presentation.md -o slides.pdf --slide-level=2 --mathml

EMB_SUFFIX = emb1

%.${EMB_SUFFIX}.npz: %.wav
	openl3 --suffix ${EMB_SUFFIX} --input-repr mel128 --content-type env --hop-size 0.5 --quiet $<

WAVS = $(wildcard data/UrbanSound8K/audio/*/*.wav)
#$(info $$WAVS is [${WAVS}])

urbansound: $(WAVS:%.wav=%.${EMB_SUFFIX}.npz)




