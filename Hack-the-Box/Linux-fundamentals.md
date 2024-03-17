# Linux Fundamentals | HTB Academy (Incomplete)

  ***Logging In via SSH***

Use Kali Linux (Ubuntu) or Windows Command Prompt to run the command

    $ssh [username]@[IP address]
    
  **user: "htb-student"**
  
  **password: "HTB_@cademy_stdnt!"**
    
<img src ="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/9d47d58c-3ec6-40ff-97bd-28b45e2eff2e" width="360" height = "310">

**I tried using Kali Linux in VirtualBox first, but the machine got stuck and disconnected. I then switched to Windows Command Prompt.*
## 1. System-Information

1.  Find out the machine hardware name and submit it as the answer.
   
    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/cbfe91a1-4075-4013-9e76-137e0007b379)
    
    ***Answer: x86_64***
    
3.  What is the path to htb-student's home directory?

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/ce09cdbd-b0ad-49ba-8fee-0af0dfdb9896)

     ***Answer: /home/htb-student***

  
5.  What is the path to the htb-student's mail?

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/56b89acc-6bd8-4e6f-affd-209a29169315)
    
     ***Answer: /var/mail/htb-student***


7.  Which shell is specified for the htb-student user?

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/9d7c55f9-a5a8-4f6b-8c3c-485e204ab995)

     ***Answer: /bin/bash***

9.  Which kernel version is installed on the system? (Format: 1.22.3)

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/f9572a94-57bf-45e7-a28c-fa90fdfc7cfa)

     ***Answer: 4.15.0***


11.  What is the name of the network interface that MTU is set to 1500?

     <img src="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/51575121-bcc9-43aa-aec8-de22d55d6d13"  width="420" height = "350">
     
      ***Answer: ens192***

## 2. Navigation

1.  What is the name of the hidden "history" file in the htb-user's home directory?
   
    ***Answer: .bash_history***

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/6e731f75-2106-4ad3-b3de-bf2a1133efaa)

2. What is the index number of the "sudoers" file in the "/etc" directory?

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/3353f277-57f4-47cf-8163-83a849ed9811)

   ***Answer: 147627***

## 3. Working with Files and Directories

1. What is the name of the last modified file in the "/var/backups" directory?

   ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/fe4a44da-eb9b-484a-b62c-85f8a0b5645a)
   ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/4d924e26-19f2-4437-8e4f-c70f8784e2fe)

   ***Answer: apt.extended_states.0***

2. What is the inode number of the "shadow.bak" file in the "/var/backups" directory?

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/ead1778d-e7af-4516-b940-874ec498632a)

   ***Answer: 265293***

## 4. Find Files and Directories

1. What is the name of the config file that has been created after 2020-03-03 and is smaller than 28k but larger than 25k?

   ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/6538c4ea-a398-4f77-9865-e38cd24e7240)

   ***Answer: 00-mesa-defaults.conf***

2. How many files exist on the system that have the ".bak" extension?

   ***Answer: 4***

   ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/91d04bd7-0173-456c-a56a-91852dd429ee)

3. Submit full path of xxd binary file

   ***Answer: /usr//bin/xxd**

   ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/e2cf3650-a836-4118-a59e-416966e36f5e)


## 5. File Descriptors and Redirections

1. How many files exist on the system that have the ".log" file extension?

   ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/95e0484d-468d-41bd-9ac7-e02e5c8ea65f)

   ***Answer: 32***

2. How many total packages are installed on the target system?

    ![image](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/4cf076bb-85c4-4dc6-835a-2ce5cdb3e0d8)

   ***Answer: 737***

   

   
   





    









