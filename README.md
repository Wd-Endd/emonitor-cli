# emonitor-cli
Emonitor-cli is a first Debian/Pacman pkg by Endd.
Emotion CPU, RAM or Swap,.. and display into Command Line, great for any low-end cli monitor like Genmon.
# Depends
- Git: To clone this repo to "Home"
- Python: Beacause this repo need python
# Installation
Clone this repo and change directory
```shell
git clone https://github.com/Wd-Endd/emonitor-cli.git
cd emonitor-cli
```
Run main.py script to packing emonitor-cli
```shell
python main.py
```
then, you can see any ``emonitor-cli-*.deb`` or ``emonitor-cli-*.pkg.tar.zst`` in ``.build/``, install it:
```shell
apt install ./.build/emonitor-cli-xxxxx.deb
```
or
```shell
sudo apt install ./.build/emonitor-cli-xxxxx.deb
```
if you use pacman, then:
```shell
pacman -U ./.build/emonitor-cli-xxxxx.pkg.tar.zst
```
or
```shell
sudo pacman -U ./.build/emonitor-cli-xxxxx.pkg.tar.zst
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
Exsample:
```zsh
> emonitor-cli -r
RAM: 4.11GB/5.70GB (72%)
> emonitor-cli -c
CPU: 14.07%
> emonitor-cli -rs
RAM: 4.11GB/5.70GB (72%)
Swap: 3.14GB/6.29GB (50%)
> emonitor-cli -rsc
RAM: 4.14GB/5.70GB (72%)
Swap: 3.17GB/6.29GB (50%)
CPU: 14.01%

~ >                                                                 01:17:44 PM

```

And, you can apply it to more cli emonitor
Apply with Generic Monitor - Genmon:
<p align="center">
  <img src="./resources/Screenshot_2025-05-10_13-28-40.png">
</p>
Resoult if you master it:
<p align="center">
  <img src="./resources/Screenshot_2025-05-10_13-42-41.png">
</p>
and
<p align="center">
  <img src="./resources/Screenshot_2025-05-10_13-47-51.png">
</p>
