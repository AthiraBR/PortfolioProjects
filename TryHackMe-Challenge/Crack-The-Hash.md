# Crack The Hash
Cracking hashes challenges

Difficulty = Easy

Tools Used
--------------
[Crackstation](https://crackstation.net/)

Command Line
 
Task 1 ✔️ Level 1
-----------

Can you complete the level 1 tasks by cracking the hashes?

Answer the questions below
  
  1. Hash : 48bb6e862e54f2a795ffc4e541caed4d
      #### Answer: easy
      Hint 💡 : Use online tools to crack
     ![90](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/df48fb8e-9408-44b3-a721-aafdb894af19)

  2. Hash: CBFDAC6008F9CAB4083784CBD1874F76618D2A97   
      #### Answer: password123
      Hint 💡 :
     ![91](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/2c83960e-e84e-419d-aadb-a2c282bdcb99)

  3. Hash : 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
      #### Answer: letmein
      Hint 💡 :
     ![92](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/1dd4c20b-c204-4591-8ea7-81bf32dc35e8)

  4. Hash : $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom  
      #### Answer: Bleh
      Hint 💡 :  hashcat -m 3200 [hash-file-location] [wordlist-file-location]
                                                           
     ![93](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/e55b11d5-455f-4b7e-9993-58db180518b4)

  5. Hash: 279412f945939ba78ce0758d3fd83daa
      #### Answer: Eternity22
      Hint 💡 :
     ![94](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/967ca1be-60d8-46cc-a4e1-4278d85e6a17)

Task 2  ✔️ Level 2
--------------------

This task increases the difficulty. All of the answers will be in the classic rock you password list.

You might have to start using hashcat here and not online tools. It might also be handy to look at some example hashes on hashcats page.

Answer the questions below:

  1. Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85  
      #### Answer: paule
      Hint 💡 :
     ![95](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/4bb8650f-447a-4c32-8404-976f38c2c761)

  2. Hash: 1DFECA0C002AE40B8619ECF94819CC1B  
  	    #### Answer: n63umy8lkf4i
        Hint 💡 :
     ![96](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/385e10d7-9d1e-461b-8907-858fe4ee3be1)

  3. Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.
     
     Salt: aReallyHardSalt  
      #### Answer:  waka99
      Hint 💡 :   Notice that the hash we starts with $6. Look through [Hashcat’s LIST](https://hashcat.net/wiki/doku.php?id=example_hashes). We see that the hash appears to be sha512crypt, which is mode 1800.
     
     ![97](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/31e86503-0fd2-4883-b0b0-721c62972b95)

  4. Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6
  
     Salt: tryhackme
       #### Answer:  481616481616
       Hint 💡 : find the hash id using the command "hashid e5d8870e5bdd26602cab8dbe07a942c8669e56d6" and We see that the hash appears to be sha1, which is mode 110
     
           hashcat -m 110 e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme ../../rockyou.txt
