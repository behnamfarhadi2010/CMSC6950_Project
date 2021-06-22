report.pdf: report.tex Radiative_Forcing.png Co_emission.png rcp2_data.csv rcp_data.csv
	latexmk -pdf

Radiative_Forcing.png:	greenhousegases_radioactive.py
	python3 greenhousegases_radioactive.py

Co_emission.png: greenhousegases_emision.py
	python3 greenhousegases_emision.py


clean:
	rm *.csv
	rm *.png

.PHONY : clean

deepclean:
	rm *.png
	latexmk -c
	rm *.pdf
	rm *.csv
	rm Report.log
	rm Report.out
	rm Report.bbl

.PHONY : deepclean

