# Phishing Analysis 2

Points = 10  
Difficulty =  Easy        
 OS = Windows/Linux
 

Scenario
-------------
Put your phishing analysis skils to the test by triaging and collecting information about a recent phishing campaign. Use Text Editor , Thunderbird

Challenge Submission
---------------------

1. What is the sending email address?

       amazon@zyevantoby.cn

2.  Who received the email?

        saintington73@outlook.com

3.  What is the subject line of the email?

        Your Account has been locked

4. What company is the attacker trying to imitate?

         Amazon

5. What is the date and time the email was sent? (As copied from a text editor)

         Wed, 14 Jul 2021 01:40:32 +0900

6. What is the URL of the main call-to-action button?

        https://emea01.safelinks.protection.outlook.com/?url=https%3A%2F%2Famaozn.zzyuchengzhika.cn%2F%3Fmailtoken%3Dsaintington73%40outlook.com&data=04%7C01%7C%7C70072381ba6e49d1d12d08d94632811e%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C637618004988892053%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=oPvTW08ASiViZTLfMECsvwDvguT6ODYKPQZNK3203m0%3D&reserved=0

7. Look at the URL using URL2PNG. What is the first sentence (heading) displayed on this site? (regardless of whether you think the site is malicious or not)

        This web page could not be loaded.

8. When looking at the main body content in a text editor, what encoding scheme is being used? (1 points)

        base64

9.  What is the URL used to retrieve the company's logo in the email? (1 points)

         https://images.squarespace-cdn.com/content/52e2b6d3e4b06446e8bf13ed/1500584238342-OX2L298XVSKF8AO6I3SV/amazon-logo?format=750w&content-type=image%2Fpng.fastly.com
     Hint 💡: In the email we can see that there is an image that was not fully loaded, In this case I what I did was the following:    
              * open URL2PNG website  
              * I dragged the image from the email to URL2PNG, With this we were able to get the URL
    
            

  ![URL2PNG](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/b64040d6-4bb3-4267-bac6-6596af951b3c)

 
10. For some unknown reason one of the URLs contains a Facebook profile URL. What is the username (not necessarily the display name) of this account, based on the URL? (1 points)

           amir.boyka.7
    Hint 💡 : Copy the link attached to the phrase "Amazon Support Team" into a text editor and analyze the URL. In this URL, there is a Facebook user id.
   

Certificate
-------------
<img src="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/95953f11-f458-4c47-bcc0-31a51aedc55d" width="350" height="300">
