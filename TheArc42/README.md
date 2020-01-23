
# Arc42 Template
***arc42 is a template for architecture communication and documentation.   
arc42 answers the following two questions in a pragmatic way, but can be tailored to your specific needs:   
1. What should we document/communicate about our architecture?   
2. How should we document/communicate?   
***

- Introduction and goals: Requirements, stakeholder, (top) quality goals  
- Constraints: Technical and organizational constraints, conventions  
- Context and scope: Business and technical context, external interfaces  
- Solution strategy: Fundamental solution decisions and ideas  
- Building block view: Abstractions of source code, black-/whiteboxes  
- Runtime view: Runtime scenarios: How do building blocks interact  
- Deployment view: Hardware and technical infrastructure, deployment  
- Crosscutting concepts: Recurring solution approaches and patterns  
- Architecture decisions: Important decisions  
- Quality: Quality tree and quality scenarios  
- Risks and technical debt: Known problems, risks and technical debt  
- Glossary: Definitions of important business and technical terms  

# IMP Takeaways 

- Use activity diagrams with swimlanes to describe or specify runtime scenarios
![Use activity diagrams with swimlanes to describe or specify runtime scenarios](https://docs.arc42.org/images/06-activity-with-swimlane.png)

- [Describe the solution approaches as a table!] (https://docs.arc42.org/tips/4-2/)
  - quality goal: What’s the top-level goal?
  - scenario: What is a or the detailed scenario for this quality goal?
  - solution approach: How does the system approach this scenario? What tactics, approaches or decisions have been taken in this direction?
  - link to details: Where are the details of this solution described? This link will either point to a concrete building block, (implementing the approach) or a section of the crosscutting concepts.
  

# Resource
- https://docs.arc42.org/home/ 
- https://arc42.org/overview/


