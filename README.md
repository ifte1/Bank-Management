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

- Naming Convension: Throughout the project I tried to give all the variable and function a meaningfull name. You can check code [here](cleancode/namingcon.png).

- Write meaningfull comment: I write comment whenever needed so anyone can understand my code easily.
[Check here](cleancode/Comment.png).

- 	Separate concepts vertically: I separate each function vertically so that anyone can easily understand each blocks. [Check here](cleancode/separate.png).

- Removed unused code: I removed all the unused code and import after completing the project.

- Exception Handling: I tried to handle any exception that can occur in my project.

#### 6. **Build Management** with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. ####
- I used pybuilder as a build management tool. You can check my successfull build [here](Build/build.png).


#### 7. Integrate some nice **Unit-Tests** in your Code to be integrated into the Build ####

- I face some difficulties to integrate unit test in build. So i decided to test my functional programming code to show my unit-test ability.

- You can find my unit test result [here](unittest/test.png)


#### 8. **Continuous Delivery:** show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc. ####

- Continuous Delivery: I used circleci as the countinous integration platform. I make a branch for circleci in git and connect that branch with circleci. You can Check [here](Pipeline/pipeline.png).

#### 9. Use a good **IDE** and get fluent with it as e.g. IntelliJ. What are your favorite **Key-Shortcuts**?! ####

I used the pycharm as IDE for this project. My favorite shortcuts are the following:

 - Run (F10)
 - Add/remove line or block comment (cmd + /)
 - Find Action (shift + cmd + A)
 - Jump from a function to another (Alt + up/down)
 - Import the missing packages (Alt + Enter)



#### 10. **DSL** Create a small DSL Demo example snippet in your code even if it does not contribute to your project ####




#### 11. **Functional Programming** (prove that you have covered all functional aspects in your code as ####

-  I come up with an external python program where i covered all the aspect of functional programming.

-  I only use final data structures, anonymous lambda function, mostly side effect free functions,  and also provides function as an argument. I also only use higher-order functions (map).

- Check Functional progamming example [here](Functional_programming.py)