# conky-moonphase
A small python script to add the current moon phase to beautify your conky display. 

It uses the `lunarcalendar` and `pytz` libraries to calculate the moon phase and the current time in your local timezone, respectively.

To use this script in Conky, you can add the following lines to your Conky configuration file:

```
${execpi 3600 python /path/to/moon_phase.py}
```

This will display the current moon phase, along with the previous and next major phases, their dates and times, in a `Conky` widget that updates every hour (3600 seconds). You can customize the font sizes and other formatting options to your liking. Just make sure to replace `/path/to/moon_phase.py` with the actual path to the Python script on your system.

## License

This script is released under the [MIT License](LICENSE).
