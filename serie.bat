@echo off
FOR /R Sims\Serie\ %%f IN (*.ini) DO (
	echo Elaborating %%f
	DoubleHole.exe "%%f" "%%f.npy"
)