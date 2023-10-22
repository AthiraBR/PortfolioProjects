# Bruteforce  

Points = 20  
Difficulty = Medium   
OS = Windows/Linux

Scenario
---------
Can you analyze logs from an attempted RDP bruteforce attack?  
One of our system administrators identified a large number of Audit Failure events in the Windows Security Event log.  
There are a number of different ways to approach the analysis of these logs! Consider the suggested tools, but there are many others out there!  

Tools Used
----------
Grep   | Text Editor  | Excel

Challenge Submission
---------------------

1. How many Audit Failure events are there? (Format: Count of Events) 
    #### Answer : 3103
    Hint 💡 :    
![1](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/c84f46e6-a7bf-413e-87ef-abd3fe228059)

2. What is the username of the local account that is being targeted? (Format: Username)
   
   #### Answer : administrator
   Hint 💡 :    
![2](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/f536f8e8-b8ff-48a4-b9a6-2adfe55fcb5c)


3. What is the failure reason related to the Audit Failure logs? (Format: String) 
    #### Answer : Unknown user name or bad password
    Hint 💡 :      
![3](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/ece48d46-37d2-4ad1-9dee-0abc37ce92ae)


4. What is the Windows Event ID associated with these logon failures? (Format: ID)  
   #### Answer : 4625   
    Hint 💡 :        
![4](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/241d2e4e-1e1d-46b6-8bc8-c90afc4c07b3)

5. What is the source IP conducting this attack? (Format: X.X.X.X)  
   #### Answer :  113.161.192.227
   Hint 💡 :        
![5](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/da7dba1a-cb72-4995-a846-d51ee8e972cd)

6.  What country is this IP address associated with? (Format: Country)
   #### Answer :  Vietnam
   Hint 💡 :    
![6](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/df3cfe00-c4bb-4b1e-a613-1f1b59aca351)

7. What is the range of source ports that were used by the attacker to make these login requests? (LowestPort-HighestPort - Ex: 100-541)
   #### Answer : 49162- 65534
   Hint 💡 : Use grep
     -  grep all the line  containing source ports
      ![7](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/4cc4cf35-91b5-4f14-bece-6f9f49c672a5)
     - Use "sort" command to list the ports in asc order
      ![8](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/61fed64d-b06c-4d5d-a270-1ff13c599a3d)


Certificate
-----------

<img src = "https://github.com/AthiraBR/PortfolioProjects/assets/87892369/2e1c781a-831d-4fe3-abd4-3ef388a1ff6f" width ="360" height = "310">
