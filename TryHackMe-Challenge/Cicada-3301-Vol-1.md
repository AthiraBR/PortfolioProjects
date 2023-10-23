# Cicada-3301 Vol:1

   Difficulty = Medium
   
Scenario
------------
A basic steganography and cryptography challenge room based on the Cicada 3301 challenges

Challenge Submission
---------------------

### Task 1 : Download!
  Download the file given in the challenge

### Task 2 : Analyze The Audio
  1. What is the link inside of the audio?
      #### Answer: https://pastebin.com/wphPq0Aa
      Hint 💡 : Use Sonic Visualizer, apply Spectogram from Layer tab, then a QR appears. Scan the QR code to get the URL
### Task 3 : Decode the Passphrase

  1. Find and Decrypt the passphrase and key
      #### No answer needed    
  2. What is the decrypted passphrase?        
      #### Answer: Hm5R_4_P455mhp453!
      Hint 💡 :  Paste the URL in the browser to get the passphrase. Now decrypt the passphrase from BASE64
     
     ![1](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/fa90d358-256c-4ad7-bd3d-1af4b5b12fd9)
     ![2](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/9c3bed36-0dc1-4432-9fb9-4813de43535a)

  3. What is the decrypted key?      
      #### Answer: Cicada
      Hint 💡 :    
      ![3](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/90a01b9c-0393-4c15-ba38-69ea1e62fca3)

  4. Still looks funny? Find and use a cipher along with the key to decipher the passphrase      
      #### No answer needed
  5. What is the final passphrase
      #### Answer: Ju5T_4_P455phr453!
      Hint 💡 :    hint on Question 4, It says [French Diplomat Cipher](https://www.boxentriq.com/code-breaking/vigenere-cipher)
     
     ![4 1](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/a010a425-f000-4b9f-8198-825d6013c148)
     ![4 2](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/eb257188-e9fe-4c9f-b974-c149788aebf2)


### Task 4 : Gather Metadata

  1. Using the found passphrase along with Stego tools find the secret message
      #### No answer needed

  2. What link is given?   
      #### Answer : https://imgur.com/a/c0ZSZga
      Hint 💡 : Use steghide to find the secret message, use the final passphrase that we just found.
     
      ![5](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/a48231af-3fe9-4871-9182-ac346d56dc71)
      ![6](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/d9c87ba8-dde0-44e4-9c57-c8f4aebb0587)


### Task 5 : Find Hidden Files

  1. Using stego tools find the hidden file inside of the image
      #### No answer needed
      Hint 💡 : Before proceeding to next Qn , open the link we found in invitation.txt and download the image
     
      ![7](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/31cf4565-3115-487b-a260-add18a478df1)

  2. What tool did you use to find the hidden file      
      #### Answer: outguess
      Hint 💡 : Use the outguess stegnograpgy tool to decode the file and then use cat command to read the contents
     
     ![8](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/f6b28a52-4170-4c44-bfb2-fe9a9986a9ef)
     ![9](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/8ccc3667-ce06-4358-bd03-c0d78c3bf396)


### Task 6 : Book Cipher

  1. Crack the Hash      
      #### No answer needed
     
  2. What is the Hash type?      
      #### Answer : SHA512
     
  3. What is the Link from the hash?   
      #### Answer: https://pastebin.com/6FNiVLh5
      Hint 💡 : Use [MD5Hashing](https://md5hashing.net/) , Paste the Hash value that you found in the hidden file
     
     ![10](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/27c2b7ea-0fab-46a7-b8ad-2a55d63febc9)

  4. Decipher the message
      #### No answer needed
      Hint 💡 : Use positive integers to move forward and negative to move backward     
     
  6. What is the link?  
      #### Answer: https://bit.ly/39pw2NH
      Hint 💡 :For the first letter we have to go to the first line of the book and move 6 characters to the right…
     
        ![13](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/f21849af-c6ee-43f0-9820-9d73a0d9567b)                                        
     … and should be able to solve the first part.
        ![14](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/10a93548-e744-445a-8211-1ec2377495ce)
     
### Task 7 : The Final Song

  1. What is the song linked?
      #### Answer : The Instar Emergence
      Hint 💡 : Visting the link above we get to a SoundCloud page which has the answer.
