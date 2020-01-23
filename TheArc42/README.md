
# The Arc42 Template
***arc42 is a template for architecture communication and documentation.***   
arc42 answers the following two questions in a pragmatic way, but can be tailored to your specific needs:   
One. What should we document/communicate about our architecture?   
Two. How should we document/communicate?   


- 1. Introduction and goals: Requirements, stakeholder, (top) quality goals  
- 2. Constraints: Technical and organizational constraints, conventions  
- 3. Context and scope: Business and technical context, external interfaces  
- 4. Solution strategy: Fundamental solution decisions and ideas  
- 5. Building block view: Abstractions of source code, black-/whiteboxes  
- 6. Runtime view: Runtime scenarios: How do building blocks interact  
- 7. Deployment view: Hardware and technical infrastructure, deployment  
- 8. Crosscutting concepts: Recurring solution approaches and patterns  
- 9. Architecture decisions: Important decisions  
- 10. Quality: Quality tree and quality scenarios  
- 11. Risks and technical debt: Known problems, risks and technical debt  
- 12. Glossary: Definitions of important business and technical terms  

# Takeaways 

- Use activity diagrams with swimlanes to describe or specify runtime scenarios
![Use activity diagrams with swimlanes to describe or specify runtime scenarios](https://docs.arc42.org/images/06-activity-with-swimlane.png)

- [Describe the solution approaches as a table!] (https://docs.arc42.org/tips/4-2/)
  - quality goal: What’s the top-level goal?
  - scenario: What is a or the detailed scenario for this quality goal?
  - solution approach: How does the system approach this scenario? What tactics, approaches or decisions have been taken in this direction?
  - link to details: Where are the details of this solution described? This link will either point to a concrete building block, (implementing the approach) or a section of the crosscutting concepts.
  
- Document the various environments
![Document the various environments](https://docs.arc42.org/images/07-deployment-overview.png)

- Use sequence diagrams to describe or specify runtime scenarios
![Use sequence diagrams to describe or specify runtime scenarios](http://docs.arc42.org/images/06-short-and-interesting.png)

- collection from arc42 as checklist for concepts
![collection from arc42 as checklist for concepts](http://docs.arc42.org/images/08-Crosscutting-Concepts-Structure.png)

- mind-map as quality tree
![mind-map as quality tree](http://docs.arc42.org/images/10-quality-tree-mindmap-example.png)

- Document and explain the specific quality tree
![Document and explain the specific quality tree](http://docs.arc42.org/images/10-quality-tree-example.png)

- quality tree as checklist
![quality tree as checklist](http://docs.arc42.org/images/01-ISO-25010-EN.png)

- Amend the glossary by a (graphical) model
![Amend the glossary by a (graphical) model](http://docs.arc42.org/images/12-graphical-glossary.png)



# Resource
- https://docs.arc42.org/home/ 
- https://arc42.org/overview/


