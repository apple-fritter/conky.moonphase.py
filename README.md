# conky-moonphase
A small python script to add the current moon phase to beautify your conky display. 

It uses the `lunarcalendar` and `pytz` libraries to calculate the moon phase and the current time in your local timezone, respectively.

To use this script in Conky, you can add the following lines to your Conky configuration file:

```
${execpi 3600 python /path/to/moon_phase.py}
```

This will display the current moon phase, along with the previous and next major phases, their dates and times, in a `Conky` widget that updates every hour (3600 seconds). You can customize the font sizes and other formatting options to your liking. Just make sure to replace `/path/to/moon_phase.py` with the actual path to the Python script on your system.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
