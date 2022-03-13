# DirStat
 A CLI to get information about a directory

# Table of Contents
- [DirStat](#dirstat)
- [Table of Contents](#table-of-contents)
- [How to use](#how-to-use)
- [Changes Coming](#changes-coming)
- [Changelog](#changelog)
- [License](#license)

# How to use
There isn't really a lot of arguments that can be passed. To use this program (be sure that you download the program from the releases tab), you type in:
```
dirstat.exe <directory>
```
Where `directory` is the directory you want to get info from

# Changes Coming
* Add Support for multiple directories
* Probs comment the fuck out of the file
* Split up `main`'s update/append functionality into their own functions
* Prettify the output

# Changelog
* 1.0.0
   * Rewrote the entire program
   * Used SQLite for keeping track of the data instead of a dict
   * Used `argparse` to handle arguments and make the program a wee more feature-rich

* 0.0.1
   * Published to Github
# License
MIT License

Copyright (c) 2021 CarbonFodder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
