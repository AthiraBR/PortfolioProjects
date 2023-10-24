# Spectrum

Points=10

Difficulty=Easy

OS= Windows/Linux


Tools Used/Required
-------------------
Photorec | Audio Software | steghide  | fcrackzip |  exiftool


Scenario
----------
Scotland yard have intercepted information about one of the biggest drug deals to go down in the city of London. Someone we believe is linked to the deal was arrested. The only item they had in their possession was a USB thumb drive. Unfortunately, one of our junior analysts was unable to find anything of interest. Before we let this suspect go, we would like one of our DF experts to see if they can find anything about the deal before it goes down. Can you find out where and when the deal is expected to go down?

Note: Once you have the coordinates, you can use https://www.gps-coordinates.net/ to view the location.

Challenge Submission
---------------------
Download the zip file, and analyze the images. We find that one of the image is a disk file
![s4](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/1b9b53f7-d508-450f-ae7b-8e9d56aaf757)

To analyze it see what it contains we will use the tool known as photorec.
  1. Select the image.dd
     
  ![s5](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/b27b2d97-0d33-432c-af3b-07cd321c05fe)

  2. Select the partition
     
  ![s6](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/1dc01537-51bc-4a76-bc28-73f88f03d300)

  3. Select the filesystem
     
  ![s7](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/5302156a-19a4-43ee-8459-1caa6643947f)

  4. Extract the whole partition
     
  ![s8](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/65c29620-6f4b-4209-b881-7cf8786f37e4)

  5. Finish
     
  ![s9](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/82062e89-97c1-497e-842e-43d09fccc3a3)

 Let’s see what we got from the disk. Let’s go the directory where data was extracted.

 ![s10](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/c12dd510-8dc6-4d82-beb6-91ca8c1d6c36)

 Use "exiftool" to analyze the images
 
 ![s11](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/d72b18d3-b790-4516-aac4-c6872eefdefb)

 Now lets try to extract information using the above password
 
 ![s12](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/6b4d3c92-cb25-427b-9f96-cd6dc61cdae8)

 Unfortunately there is no information here.
 Now we try to crack the zip file using fcrackzip

 ![s13](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/41a59455-5beb-4276-987c-3cc9adb4e4bf)

Hint 💡 : Steghide can also be used in audio files

![s14](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/7d22a9b6-0b71-4fe2-a6da-cb25e9d9b038)

Decode the string to get the value

1. What time is the meeting happening? (4 points)
    #### Answer : 00:10:51
    Hint 💡 : Decode the Base58. See "emit" which when read in reverse as "time", hence write the "15:01:00" in reverse order 
   
   <img src="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/71e6ea2a-4899-4b5d-8945-91c68c83c337" width="300" height="250">


3. What are the supposed coordinates for the deal? (4 points)
    #### Answer : 51.50278, 0.05527
    Hint 💡 : Use sonic viewer (an audio software) and apply spectrogram from Layer tab to get the coordiantes
   
    ![s2](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/732123ca-caa1-4e1a-a26a-688bbec7deba)
   
4. Looking into these coordinates, what is the name of this location? (2 points)
    #### Answer: London City Airport
    Hint 💡 : 
   
   ![s3](https://github.com/AthiraBR/PortfolioProjects/assets/87892369/fa0fc9e7-7288-480f-adf3-7fc91777d53c)

   Certificate
   ------------
   <img src="https://github.com/AthiraBR/PortfolioProjects/assets/87892369/6f8587f7-a40d-49f0-b236-8a8a4e46f0b6" width ="510" height="300">
