---
title: GNU/Linux
---
<div class="body">
  <p>I was the President of the University of Northern Iowa's Linux User Group <i>CedarLUG</i> from 2018 to 2020,
    and was the Vice-President for two years previous to that (while I was still in high school, even!).
    I recall that I've been using one GNU/Linux distribution or another since I was about thirteen,
    so I've certainly had a bit of practice with it.
  </p>
  <p>
    This area mainly serves to host the list of programs I install on first boot-ups of Debian,
    but anything GNU/Linux related may get put in here as well.
  </p>
  <h3 style="text-align: center;">Additional Programs For Debian</h3>
  <p>
    <a href="./assets/debian12_install.txt">Here</a> are a number of programs I add to a fresh install of Debian 12 (Bookworm) before I get to work. Note that many of them are for niche applications, so if you want to use this, be aware that precious MB of disk space may be taken up by libraries that you may never use.
  </p>
  <p>
    Here are the packages I have used on previous versions of Debian:
    <ul>
      <li><a href="./assets/debian11_install.txt">Debian 11 (Bullseye)</a></li>
      <li><a href="./assets/debian10_install.txt">Debian 10 (Buster)</a></li>
      <li><a href="./assets/debian9_install.txt">Debian 9 (Jessie)</a></li>
    </ul>
  </p>
  <h3 style="text-align: center;">Proto-Operating System in MARIE</h3>
  <h5 style="text-align: center;">(A 2018 CedarLUG Presentation I Gave)</h5>
  <p>
    Here are a couple files in MARIE assembler (shown as if entered into memory) showing what a runnable program would look like on a "Altair 8800 -- style" personal computer (saying it used the MARIE architecture). 
  </p>
  <p>
    The first file contains a simple program example and the (modified) MARIE architecture description: <a href="./assets/computing_0.org">MARIE Description</a>
  </p>
  <p>
    This is an example of a boot loader which would be used once and likely overwritten: <a href="./assets/computing_1.org">Boot loader</a>
  </p>
  <p>
    This is what could be called a resident monitor. Essentially a boot loader which loads and runs a program before regaining control to load another. This might be considered similar to CP/M, but without fancy stuff like a linker or text prompts. Here is the code: <a href="./assets/computing_2.org">Resident Monitor</a>
  </p>
  <p>
    There is a fourth program that I was working on that had preemption and a file-system for the kernel. I might get around to writing it when I delve further into making my (modified) MARIE TTL computer.
  </p>
</div>
