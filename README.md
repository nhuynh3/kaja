
## Electron Cloud
Refine your Jewels


### Overview: 
Electron Cloud is a marketplace that connects independent jewelry makers to buyers.
  
In this repository, you'll find the technology that powers the core pricing service offered to jewelers on Electron Cloud. Our platform uses machine learning to determine the optimal pricing of jewelry pieces based on interest in an individual jeweler's work and generalized market demand. We make use of constrained optimization to maximize expected profits of an independent jewelry owner's portfolio of products.

### Objective Function:
<a href="https://www.codecogs.com/eqnedit.php?latex=\textup{arg&space;max&space;}&space;\pi&space;_{j}&space;E[profit(\pi_{j}^{&space;})&space;|&space;x_t]&space;\textup{&space;s.t.&space;}&space;cost(\pi_{j}^{&space;})&space;\leq&space;\textup{budget}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textup{arg&space;max&space;}&space;\pi&space;_{j}&space;E[profit(\pi_{j}^{&space;})&space;|&space;x_t]&space;\textup{&space;s.t.&space;}&space;cost(\pi_{j}^{&space;})&space;\leq&space;\textup{budget}" title="\textup{arg max } \pi _{j} E[profit(\pi_{j}^{ }) | x_t] \textup{ s.t. } cost(\pi_{j}^{ }) \leq \textup{budget}" /></a>

### Key Components:
- Constrained Optimization
- Dynamic Programming
- Parametric Modeling / Supervised Learning

### Steps to Build and Test: 
In the root directory, run `$ python src/optimizer/jewelry_optimization.py`
### UI Prototype:
https://xd.adobe.com/view/840f4443-1cb1-47e7-6aea-295b3b663f42-f23e/?fullscreen

### Presentation:
https://docs.google.com/presentation/d/1UBqfpQ0L6mwN7NK4aXRSmVjIu9kDYm0x70i9sb9QDr4/edit#slide=id.p
