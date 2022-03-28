# InfoProcCW

**Objective:**
Create a real time remote multiplayer game that uses FPGA as an input and AWS

**Langauge:**
1. C# for game development
2. Python for server management 

Video Link: 
https://imperiallondon-my.sharepoint.com/:v:/g/personal/mc620_ic_ac_uk/ESUwiGZXywdEs02p68YBDPEBSvGz4cjECBFP_qcCZHzQjw?e=kaiPxR

**Gameplan:**
1. Create 2D game
2. Add gameplay functionalities 
3. Build multiple gamemodes to use all inputs from FPGA
4. Write report and create video explaining gameplay and design process 

Purpose of the System:
We designed and implemented a real-time multiplayer game using the FPGAs as controllers. Using AWS servers, local FPGA processing and Unity infrastructure we created an exciting “Mario style” 2D co-operative game.

Game Description:
A co-op real time multiplayer game was created on Unity using C#. It currently supports 2 players to play in real time on the same laptop, and it is also easily scalable. The game can be adjusted to spawn multiple players when there are more control nodes. The objective of the game is for the players to reach a treasure case at the end of the map. If any player fell off the map or died, all the players are sent back to the starting point; if any player finishes the map, all the players progress to the next level.

We are currently replicating the experience of a console multiplayer game, which 2 players play a multiplayer game on the same screen with 1 PlayStation. The natural future development would be to replicate the PC gaming, which each player sits in front their own PC and have unique gameplay perspectives. Our server can be easily adjusted to support this functionality, but it takes some time to create a multiplayer game that displays different objects on various screens. 

Design decisions: using raw data instead of FIR filtered data:
Initially, we tried to pass the accelerometer data through an FIR filter that we coded in C to process the data readings. We experimented generating different coefficients in MATLAB through using the designfilt() function and encoded the filter in the C script in Eclipse. However, to provide meaningful filtering we needed to use a large n-tap filter (50) which we found reduced the sampling rate below that of raw data processing increasing the lag between a player moving the board and the detection being communicated. As our game is dynamic (involves real-time player movement), fast input times are prudent. Consequently, to balance the sensitivity we tested how we physically move the board and implemented boundary conditions to detect input (i.e the game rejects minor movements of the board and accepts deliberate movements).
Getting data from NIOS to Python:
Once we obtained the accelerometer data in the NIOS terminal we needed to extract this into Python so it can be used by a client-side program. We utilised the subprocess module which allows us to spawn new processes and communicate with I/O streams in the NIOS terminal.

Server side:
The clients would first send an identification message to the server, declaring the client either to be an FPGA or a computer. The server then records the IP address and port number, along with what device it is, of the client that sends the message. Thus, even if the FPGA client and computer client share the same IP, the port number would differentiate between the processes. 
The FPGA client constantly sends the accelerometer data to the server and the server constantly receives it. When it receives an update from a particular FPGA client, it will send it to the computer client with a header inserted declaring which FPGA it is from. 
Some useful information about the connection status would also be printed in the terminal for monitoring and troubleshooting purposes. 

Design decisions: using UDP instead of using TCP 
Initially, we tried to use TCP for the server but it didn’t work. Since TCP is connection-oriented, the original logic was to use threading to take care of listening for new clients, receiving data from the FPGA client, and sending data to the computer client. However, in later stages of testing it was found that the TCP recv() function would fill up the buffer it was given and then output the data. This introduced a significant delay (~2 seconds) to receive and extract player control information. 
The solution was to switch to UDP, which turned out to be very efficient and fits our demands very well. The message-based nature of the protocol allows the logic to be extremely simple, and storing the IP and port number of the clients avoids the need to use multicasting. 


Unity game Development:
The game engine is a client node and receive data from the server. The data sent to the game engine is in the form of (P1/P2 X_Coordinates Y_Coordinates Z_Coordinates Button_Pressed). The data will then be parsed into a form that the game can take as an input. For example, if the data for x-coordinate sent to the game engine is 112<X_Coordinate<10000, then we know the player has tilted the FPGA to the left. Hence, the data will be parsed as horizontal =’-1’. The parsed data for all the controls will be written to a datafile playercontroltext1/2.txt (Figure 11). We wrote C# scripts to read datafiles at a rate of 60 Hz and change the movement of the player accordingly. This introduced a delay of approximately 20ms which is neglectable compared to the delay of the AWS server.

For a real-time multiplayer game to be played smoothly, minimising latency is a key factor. We have measured the amount of latency between FPGA movement and game player change using a stopwatch. The results below are the average results for 50 measurements. The maximum delay measured wass 923ms even when player reaction time was taken into account. We believe this is a very satisfactory average latency for a real time multiplayer game considering the server is in US Virginia. 
After multiple individuals tested the game, the overall feedback suggested that latency did not affect gameplay.
