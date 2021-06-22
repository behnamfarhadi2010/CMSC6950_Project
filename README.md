# CMSC6950_Project
Course project for CMSC6950 Spring 2021

Behnam Farhadi

## Software setup
Assuming you have installed conda already

```
conda create -n pymagicc_pro
conda install matplotlib pandas seaborn notebook pymagicc
conda activate pymagicc_pro
```

## install wine 
wine is a compatibility layer capable of running Windows applications on several
POSIX-compliant operating systems, such as Linux, macOS, & BSD.

```
sudo apt-get update
sudo dpkg --add-architecture i386
sudo apt-get install wine32
```

On 32-bit systems Debian/Ubuntu-based systems wine can be installed with

```
sudo apt-get install wine
```
## Usage Instructions
First clone the respository and create a directory named CMSC6950_Projects
```
git clone https://github.com/behnamfarhadi2010/CMSC6950_Project.git
cd CMSC6950_Project
```

Assuming you already Installed LaTEX and its dependencies, type the following commands.
Note that by using the following commands all datasets, visulaizations, and pdf files will be created.

```
make
```

To clean the generated files try the following commands:
```
make clean
make deepclean
``` 
