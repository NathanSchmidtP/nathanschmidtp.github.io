---
title: Various Hacks and Novelties
---
<div style="text-align: center;" class="body">
  <h3 style="text-align: center;">A Talking Fish</h3>
  <iframe width="560" height="315" style="display:block;margin:auto;" src="https://www.youtube.com/embed/VHSHPGPk6w0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <p>
    The fish in the video was controlled by a partially bread-boarded prototype of the <i>FISH Dialogue</i> board shown below:
  </p>
  <img src="/Electronics/Misc_Circuits/assets/img/FISH-Dialogue.png" width="640" height="480">
</div>
<br>
<div style="text-align: center;" class="body">
  <h3 style="text-align: center;">CNC Laser PCB Manufacture</h3>
  <p>
    Around 2017 I was trying to set up some way
    of rapidly producing printed circuit boards.
    For many years prior to that I only had access
    to perf-board and etchable two sided boards.
    I imagine some reasonable services were already
    available at that time, but I hadn't heard of them.
  </p>
  <p>
    The three methods I had devised were:
    <ul style="text-align:left;">
      <li>Creating a positive print using India Ink</li>
      <li>Burning away negative prints from a coat of spray paint</li>
      <li>The standard transparency method</li>
    </ul>
  </p>
  <p>
    The laser engraver I have been using is an Eleksmaker <i>EleksLaser A3</i>.
    It is really not much more than a two-axis rep-rap style CNC machine.
    It has an Arduino Nano clone with GRBL driving two A4988 stepper motor drivers,
    and uses a 405nm 2.5w laser.
  </p>
</div>
<div style="text-align: center;" class="body">
  <h3 style="text-align: center;">Pumpkin Spectrometry</h3>
  <video width="640" height="360" controls loop>
    <source src="./assets/img/pumpkin.webm" type="video/webm">
  </video> <br>
  <i>Still working out some bugs</i>
</div>
<div style="text-align: center;" class="body">
  <br>
  The source for the Atmel ATMega328p can be found (<a href="./assets/pumpkin.c">here</a>) written in C and can be compiled with avr-gcc. 
</div>
