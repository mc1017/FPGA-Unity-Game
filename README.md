# InfoProcCW

**Objective:**
Create a 2D/3D multiplayer battleroyale game with maximum 6 players with Unity Game Engine in AWS. 

**Langauge:**
1. C++ for FPGA accelerometer 
2. Python for game dev

**Gameplan:**
1. Create 2D game
2. Add gameplay functionalities 
3. Build a 3D game based on the 2D Mechanics (Never done in previous years)
4. Write report and create video explaining gameplay and design process 



**Official Specifications**

The minimum **functional requirements** for your system are:
- Local processing of the accelerometer data.
- Establishing a cloud server to process events/information
- Communicating information from the node to the server.
- Communicating information from the server back to the nodes in way that the local
processing can be impacted.

**Coursework deliverables**
Your coursework deliverables consist of the following:
1. A report (pdf) that describes your system, consisting of at most 5 A4 pages. The
report should cover:
  a. The purpose of your system.
  b. The overall architecture of your system.
  c. A description of the performance metrics of your system. Which metrics
  should be used? Why?
  d. At least one diagram of your system’s architecture.
  e. Design decisions taken when implementing the system.
  f. The approach taken to test your system.
  g. At least one diagram or flow-chart describing your testing flow or approach.
  h. Resources utilised for the DE10-Lite from Quartus
2. Peer feedback: individual submission by each group member to provide peer
  feedback on your team members, submitted via Microsoft Forms.
3. Your design (Quartus – Hardware), and software for NIOS/host/server in a zip file
  version 1.0
4. (Optional) A short video (up to 5 min) where you can provide a description of your
  project and demonstrate what you have done. This is not assessed, but it can provide
  a nice advertisement of your work.
  
**Assessment**
The coursework mark comes from the following components:
1. Functionality (30%) : does your system work? This is assessed purely based on
  whether the various parts of the system are functionally correct, and they meet
  the minimum functional requirements described above.
2. Testing (20%) : Is your testing complete? Have you considered testing all aspects
  of the system?
3. X-factor (20%) : This component aims to capture how challenging your system is
  and the optimisations that you have applied/considered. For example, when it
  comes to processing the data on the local node, this can be done with a direct
  implementation of an FIR filter using floats, a more optimised approach would be
  to consider performing the operations under a fixed-point representation, where
  an even more optimised approach would be to have a hardware component that
  performs the filtering. What are the trade-offs?
4. Documentation (20%) : Are the architectural and testing approached adequately
  described? Have the required components been covered? Does it provide useful
  information specific to your solution? Does it highlight any clever or important
  features/decisions?
5. Oral examination (10%) : An opportunity to demonstrate and explain your project.
6. Peer-feedback (+-5%) : allocated according to peer feed-back within the group.
  This will affect the individual mark by up to 5% relative to the group mark.
