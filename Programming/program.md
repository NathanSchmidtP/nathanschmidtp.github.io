---
title: Programming
---
<div class="body">
  <p>
    Programming is one of my favorite pastimes.
    My main interest area tends to be hardware control and interfacing.
    However I frequently cross over into other areas when I find interesting problems.
    Such problems include my <a href="../Mathematics/math.html">mathematics projects</a>
    and extend as far out as to biological physics.
  </p>
</div>
<div class="body">
  <a href="https://gitlab.com/schminak/tiny-machine"><h3 style="text-align: center;">Tiny-Machine</h3></a>
  tiny-machine is a virtual machine which executes programs written in
  the Tiny Machine language, as defined by Kenneth C. Louden in his book
  <a href="http://www.cs.sjsu.edu/faculty/louden/cmptext/">Compiler Construction Principles and Practice</a>.
  It is entirely written in Guile Scheme and utilizes a PEG parser
  to implement its interpreter in an enjoyably concise way.
  As an example, the entire implementation of tiny-machine's fetch-execute cycle is shown below.
  This includes the definition of all seventeen instructions in the Tiny Machine language:
</div>
<div style="max-width: 72ch; text-align:justify; margin: 0 auto;">
  <script src="https://gitlab.com/schminak/tiny-machine/-/snippets/2411747.js"></script>
</div>
<div class="body">
  <a href="https://gitlab.com/schminak/affinity"><h3 style="text-align: center;">Affinity and AFiNeS</h3></a>
  <p>Affinity is a program I wrote for plotting the output of the <a href="https://github.com/Simfreed/AFINES">Active Filament Network Simulation (AFiNeS)</a> program. It allows the evolving cytoskeletal actin networks to be visualized as either a GIF animation or in real time during the simulation. Affinity uses libplot from the <a href="https://www.gnu.org/software/plotutils/">plotutils</a> package.
  </p>
</div>
<div style="text-align: center;" class="body">
  <img src="https://gitlab.com/schminak/affinity/-/raw/master/doc/affinity_test.gif" style="width:480px;height:480px;"><br>
  <i>An actin network animation output from Affinity</i>
</div>
<div class="body">
  <h3 style="text-align: center;">ATMEGA328P "Arduino" Embedded Programming</h3>
  <p>
    This is a bibliography I frequently reference when working with Atmel chips outside of an Arduino.
    All links have been archived using <a href="https://web.archive.org">The Wayback Machine</a>.
    If the links are broken, simply paste the URL in their search engine to find an old copy.
  </p>
  <ol>
    <li><a href="https://web.archive.org/web/20170803114958/http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42735-8-bit-AVR-Microcontroller-ATmega328-328P_Datasheet.pdf">ATMEGA328P Datasheet (Old, 328/P chip specific)</a></li>
    <li><a href="http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega48A-PA-88A-PA-168A-PA-328-P-DS-DS40002061A.pdf">ATMEGA328P Datasheet (New)</a></li>
    <li><a href="https://www.nongnu.org/avr-libc/user-manual/index.html">AVR Libc User Manual (avr-gcc/avrdude)</a></li>
    <li><a href="https://www.microchip.com/webdoc/AVRLibcReferenceManual/">AVR Libc Reference Manual (Microchip, proprietary)</a></li>
    <li><a href="https://balau82.wordpress.com/2011/03/29/programming-arduino-uno-in-pure-c/">Tutorial w. a similar objective (Quite Good!)</a></li>
    <li><a href="http://brittonkerin.com/cduino/lessons.html">Another tutorial w. a similar objective</a></li>
    <li><a href="https://www.arduino.cc/en/Hacking/Atmega168Hardware">ATMEGA168/328 to Arduino Uno Pinout</a></li>
    <li><a href="https://www.arduino.cc/en/Tutorial/ArduinoISP">ArduinoISP and Bootloader explanations</a></li>
    <li><a href="https://www.arduino.cc/en/Hacking/ParallelProgrammer">Make a Parallel Programmer</a></li>
    <li><a href="https://web.archive.org/web/20061212161422/http://www.captain.at:80/electronics/atmel-programmer/">Make an older Parallel Programmer</a></li>
    <li><a href="/Hacking/pumpkin.c">A simplistic program of mine that displays "Pumpkin Error"</a></li>
  </ol>
</div>
<div style="text-align: center;" class="body">
  <h3 style="text-align: center;">Project Euler</h3><br>
  <img src="https://projecteuler.net/profile/nathanschmidt.png" width="200" height="60"><br>
  <span style="display:block; height: 20px;"></span>
</div>
