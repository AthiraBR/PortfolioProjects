<h1>Failed RDP Logins to IP Geolocation Information</h1>

<h2>Description</h2>
<b>The Powershell script in this repository is responsible for parsing out Windows Event Log information for failed RDP attacks and using a third-party API to collect geographic information about the attackers' location.
</b>
<br />
<br />
Azure Sentinel (SIEM) is set up and connected to a live virtual machine acting as a honey pot to observe live attacks (RDP Brute Force) from all around the world. Used a custom PowerShell script to Look up the attackers' Geolocation information and plot it on an Azure Sentinel Map!
<br />
<br />

<p align="center">
<img src="https://github.com/user-attachments/assets/3d5924d9-e5a7-43ba-9013-a2fbf274eabd" height="85%" width="85%" alt="RDP event fail logs to iP Geographic information"/>
</p>
<h2>Tool Used</h2>

- <b>PowerShell:</b> Extract RDP failed logon logs from Windows Event Viewer 

<h2>Utilities Used</h2>

- <b>ipgeolocation.io:</b> IP Address to Geolocation API

<h2>Attacks from Poland coming in; Custom logs being output with geodata</h2>

<p align="center">
<img src="https://github.com/user-attachments/assets/4dd329ed-ae0e-4d42-bedc-252d435ab3ca" height="85%" width="85%" alt="Image Analysis Dataflow"/>
</p>

<h2>World map of incoming attacks after 24 hours (built custom logs including geodata)</h2>

<p align="center">
<img src="https://github.com/user-attachments/assets/61fea3b0-2337-4195-8a14-56069debf3f9" height="85%" width="85%" alt="Image Analysis Dataflow"/>
</p>


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
