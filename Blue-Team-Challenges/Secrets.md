# Secrets

Points - 10

Difficulty - Easy

**Scenario**
-------------
You’re a senior cyber security engineer and during your shift, we have intercepted/noticed a high privilege actions from unknown source that could be identified as malicious.We have got you the ticket that made these actions.
You are the one who created the secret for these tickets. Please fix this and submit the low privilege ticket so we can make sure that you deserve this position.
Here is the ticket:

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOnRydWV9.jbkZHll_W17BOALT95JQ17glHBj9nY-oWhT1uiahtv8

**Tools Used**
--------------
- [Cyberchef](https://gchq.github.io/CyberChef)
- [JWT](https://jwt.io/)
  
**Challenge Submission**
---------------------
#1) Can you identify the name of the token? (Format: String) (2 points)
  #### Answer: JWT
  #### Hint 💡:
  <img src="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/8b5655c0-dd43-4a82-b6ca-c75a46b2eac6"  width="1200" height = "300">

  <img src ="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/9bf78383-84e1-481d-9081-9ac29f173e03"  width="800" height = "600">
 
#2) What is the structure of this token? (Format: Section.Section.Section) (2 points)
  #### Answer: header.payload.signature

#3) What is the hint you found from this token? (Format: String) (2 points)
  #### Answer: _4_Eyes

#4) What is the Secret? (Format: String) (2 points)
  #### Answer: bT!0
  #### Hint💡 : 
  We need to crack jwt token using brute-forcing with hash-cat or john to get the secret to solve this challenge using 
  
  hashcat json.txt -m 16500 -a 3 ?a?a?a?a

#5) Can you generate a new verified signature ticket with a low privilege? (Format: String.String.String) 
  #### Answer:  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOmZhbHNlfQ.nMXNFvttCvtDcpswOQA8u_LpURwv6ZrCJ-ftIXegtX4
  #### Hint💡 : 
  <img src="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/bef0f292-7ebd-413d-9ce6-c5cc001eb81f" width="800" height = "600">

**Certificate**
------------------
<img src = "https://github.com/AthiraBR/PortfolioProjects/assets/87892369/d554ce53-2a5a-4a15-a49e-db2773e5c788"  width="800" height = "600">
