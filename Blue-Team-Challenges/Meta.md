### Meta

Points = 10      
Difficulty = Easy   
OS = Windows/Linux


Scenario
-------------
An attached images were posted by a criminal on the run, with the caption “I’m roaming free. You will never catch me.” And as a Cyber Defender it's your job to find details about the crime. Let's assist the team in proving him wrong.
Exiftool and Reverse Image Search can be used to solve the Lab.

Challenge Submission (Using LINUX)
---------------------
1. What is the camera model? 
    ### Answer: Canon EOS 550D
    Hint :bulb: : We use exiftool to extract the Metadata of the image. Extracting the Metadata of an image can be a good starting point for this investigation.

2. When was the picture taken? 
    ### Answer : 2021:11:02 13:20:23
    Hint :bulb: : This can be answered from the Metadata that we have extracted from the previous question. Search for the original time and date when the picture was taken.

3. What does the comment on the first image says? (3 points)
    ### Answer: relying on altered metadata to catch me?
    Hint :bulb: : The comment on the first image can be found in the same metadata which we have extracted for the above question.

4. Where could the criminal be? 
    ### Answer: Kathmandu
    Hint :bulb: : Do a reverse image search for both images


In WINDOWS:
---------------
- Download the exiftool and Extract "exiftool(-k).exe" from the ".zip" file, 
- Rename "exiftool(-k).exe" to "exiftool.exe".
  (or "exiftool(-k)" to "exiftool" if file name extensions are hidden on your system)
- Move "exiftool.exe" to the "C:\WINDOWS" directory (or any other directory in your PATH).
- You can now run exiftool by typing "exiftool" at the command prompt.                               

Certificate
----------------


![BTLO_page-0001 (2) (1)](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/7373f7e8-b647-4ce4-99d2-8860fb9ae2ee)
