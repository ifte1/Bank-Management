### This is a project from Md. Ifte Khairul islam for the Data Science Master class "Advanced Software Engineering" at the Berliner Hochschule für Technik (BHT) ###

#### 1. Use and understand **Git!** ####
Look around my Github account

#### 2. **UML** at least **3** good diagrams. "good" means you can pump it up artificially as written in DDD. You have 10 million $ from me! Please export the pics. I can not install all tools to view them! ####
I modelled the following three diagrams:
- The Use Case Diagram shows the user interactions with the Bank. In this system there are two actor 'user and system' and seven use cases.
   - [Use Case Diagram](UML/USE-CASE_Diagram.svg)   -->  [PlantUMl](UML/USE_CASE_Diagram)

- The Activity Diagram shows the workflow of the Banking process. It starts with choosing what a user wants to do.
   - [Activity Diagram](UML/Activity_diagram.svg)   -->  [PlantUMl](UML/Activity_Diagram)

#### 3. **DDD** If your domain is too small, invent other domains around and document these domains (as if you have 10 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with 5-0 Domains. It would be nice if these domains are derived from an Event-Storming (but not mandatory). ####
To figure out all domain events i started with event stroming. Then i combined related subdomain to a bigger domain and established their relationship. After that, I created the core domain chart and placed every domain in their category.

- [Domain and Subdomain Relationships](DDD/domains_and_sub_domains_core_domain_chart.pdf)
- [Core Domain Chart](DDD/domains_and_sub_domains_core_domain_chart.pdf)


#### 4. **Metrics** at least two. Sonarcube would be great. Other non trivial metrics are also fine. ####
I used SonarCloud to find Metrices.it concluded the follwing results

- [SonarCloud Overview](metrics/Sonarcloud.png)
- 0 Bugs 
- 0 Vulnerabilities
- 0 Security Hotspots
- 28 Code Smells


#### 5. **Clean Code Development:** at least **5** points you can show me + >>10 points on your **personal cheat sheet** ####

My personal cheat sheet is [here](cleancode/Personal_Cheat_Sheet.pdf). From there i applied the following elements:





#### 6. **Build Management** with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. ####



#### 7. Integrate some nice **Unit-Tests** in your Code to be integrated into the Build ####



#### 8. **Continuous Delivery:** show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc. ####



#### 9. Use a good **IDE** and get fluent with it as e.g. IntelliJ. What are your favorite **Key-Shortcuts**?! ####




#### 10. **DSL** Create a small DSL Demo example snippet in your code even if it does not contribute to your project ####




#### 11. **Functional Programming** (prove that you have covered all functional aspects in your code as ####
