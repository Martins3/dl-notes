# xrandr --newmode "2560x1440" 312.25  2560 2752 3024 3488  1440 1443 1448 1493 -hsync +vsync 
# xrandr --newmode "2560x1440R" 41.50 2560 2600 2632 2720 1440 1443 1448 1481 -hsync +vsync
xrandr --newmode "2560x1440R" 173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync

xrandr --addmode DP-2 2560x1440R

xrandr --output DP-2 --mode 2560x1440R

