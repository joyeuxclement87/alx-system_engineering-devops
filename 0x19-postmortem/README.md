Postmortem: Web Stack Debugging
Incident (IMAGINED ISSUE)

Postmortem Report: June 22, 2024 Outage
--------------------------------------------------------
Issue Summary
--------------------------------------------------------
Duration of the Outage:
Start: June 22, 2024, 10:00 AM
End: June 22, 2024, 11:30 AM
--------------------------------------------------------
Impact:
--------------------------------------------------------
Capricorn Visuals’ primary image rendering service was
down, preventing users from uploading or processing
images.
Approximately 70% of users experienced issues
accessing the service, with 50% unable to complete
uploads and 20% facing slow processing timeS
--------------------------------------------------------
Root Cause:
--------------------------------------------------------
The outage was caused by an unhandled exception in the
image processing microservice. This exception occurred
due to a malformed response from a third-party image
enhancement service API. The service did not have
appropriate error handling for this specific scenario,
leading to a failure in processing images and thus causing
the service to become unresponsive for a significant
portion of users.
--------------------------------------------------------
Timeline
--------------------------------------------------------

10:05 AM: Issue detected via automated monitoring
alerts indicating an unusual drop in successful image
uploads.
10:10 AM: Initial investigation by the on-call engineer
confirmed the issue was related to the image processing
service.
10:15 AM: Assumed root cause to be a network latency
issue; network team was engaged to check for
connectivity problems.
10:30 AM: Customer complaints started flooding in,
confirming widespread impact.
10:40 AM: Misleading path taken by restarting network
services and rolling back recent code deployments, which
did not resolve the issue.
11:00 AM: Incident escalated to the image processing
team after network and code rollback solutions failed.
11:10 AM: Image processing team identified unhandled
exception caused by malformed API response from
third-party image enhancement service.
11:20 AM: Temporary fix deployed to handle the
exception and bypass the faulty API response.
11:30 AM: Service fully restored and functioning normally.
--------------------------------------------------------
Resolution:
--------------------------------------------------------
To resolve the issue, the image processing team
implemented a temporary fix to handle the exception and
bypass the malformed response. This allowed the service
to continue processing images without interruption from
the faulty API response. Subsequently, a permanent fix was
developed to include robust error handling and validation
for all external API responses to prevent similar issues in
the future.
Corrective and Preventative Measures
Improvements and Fixes:
Enhance error handling in all microservices to gracefully
manage malformed or unexpected responses from external
APIs.
Improve monitoring and alerting to detect and diagnose
similar issues more rapidly.
Conduct regular audits and testing of third-party API
integrations to ensure resilience
--------------------------------------------------------
--------------------------------------------------------
here is link for post https://www.linkedin.com/posts/tuyishimire-joyeux-clement-32418528a_postmortem-web-stack-debugging-incident-activity-7210659940061872129-ukK6?utm_source=share&utm_medium=member_desktop