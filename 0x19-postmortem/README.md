# Postmortem

![alt text]()

### Issue Summary
From 0314hrs to 1430hrs EAT, the Shwitter APIs, mainly profile and profile_list endpoints experienced unexplainable downtimes. Requests to our servers in Chan_tech data center resulted in 500 error response messages. The issue affected all requests to this data center. The root cause was determined to be a error in redirecting requests in the nginx configuration file that went unnoticed.

### Timeline (All East African Time)
- 0300hrs: routine update of configurations in our servers
- 0314hrs: First incident communicated to us
- 0500hrs: Alerted the team involved
- 0800hrs: Meeting held to go through the code
- 1100hrs: Communication sent out to customers to inform them of the incidence
- 1300hrs: Error noted and corrected
- 1430hrs: All servers back online

### Root Cause
> At 0300hrs, a change in our nginx configuration file was routinely executed by our script but the developer team had forgoten to run a check using nginx's built in linter. This resulted in the script publishing changes to all our servers with the wrong configuration file. Our servers could no longer server the intended traffic and our users could not access our social medial site.

### Resolution and recovery
> At 0800hrs EAT the dev team had a lengthy meeting where changes were rolled back in a test environment and the updates done manually step by step to figure out where the issue was.
>At 1300hrs, the team was able to figure out the issue and made the necessary updates and brought the servers back online by 1430hrs EAT.

### Corrective and Preventative Measures
> In a post meeting held after the recovery, the team put inplace mechanisms to address the occurrence of such issues in the future. It was agreed that the dev team would carry out diligent tests in a test environment before progagating changes to our production environment.

##### Sincerely,
##### The SRE team.

NB: This is a made up scenario of a postmortem and the required documentation. In the real world, where we are dealing with a big application, the postmortem needs to be more detailed and informative. 