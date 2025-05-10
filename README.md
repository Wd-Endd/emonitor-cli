# emonitor-cli
Emonitor-cli is a first dpkg by Endd.
Emotion CPU, RAM or Swap,.. and display into Command Line, great for any low-end cli monitor like gemmy.
# Depends
Git: To clone this repo to "Home"
Python: Beacause this repo need python
# Installation
Clone this repo and change directory
```bash
git clone https://github.com/Wd-Endd/emonitor-cli.git
cd emonitor-cli
```
Run main.py script to packing emonitor-cli
```bash
python main.py
```
then, you can see any ``emonitor-cli-*.deb`` in ``.build/``, install it:
```zsh
apt install ./.build/emonitor-cli-xxxxx.deb
```
or
```bash
sudo apt install ./.build/emonitor-cli-xxxxx.deb
```
# Usage
Help command
```zsh
> emonitor-cli
Usage: emonitor-cli [options]
Options:
-r: RAM
-s: Swap
-c: CPU

~ >                                                                 01:11:47 PM
```