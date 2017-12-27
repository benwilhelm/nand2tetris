// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.



// Bootstraps all values, and resets them when the pressed key is changed
(Start)
  @k // ASCII value of key pressed
  M=0
  @SCREEN
  D=A
  @s // word in screen memory map
  M=D

  @v // black/white
  M=0

  @KBD
  D=M
  @k
  M=D
  @Loop
  D;JEQ // if nothing pressed, go to loop


// We're here if there's a key pressed.
// set @v to -1
(KeyDown)
  @v
  M=-1


// The main loop
// iterate over all words in the screen's memory map, setting them to 0 (white) or -1 (black)
// according to the value of @v
(Loop)

  @v   // set D register to value of @v
  D=M

  @s   // set current memory word to value of D register (@v)
  A=M
  M=D

  D=A+1 // increment memory word
  @s
  M=D

  @24576 // Check that we haven't overrun the memory map. If so, start again at the top
  D=D-A
  @Start
  D;JGT

  @KBD   // Check current pressed key. If it's changed, start over at the top
  D=M
  @k
  D=D-M
  @Start
  D;JNE

  @Loop // Loop it!
  0;JMP
