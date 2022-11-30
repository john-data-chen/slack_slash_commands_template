# Slack Slash Commands
this is a template of Slack Slash Commands bulit on Cloud Functions of Google Cloud Platform <br />

## how to use it?
in slack, enter command such as: /command xxxx <br />


## how to setup GCP cloud functions?
Environment: 2nd gen <br />
Region: asia-east1 (because my office is in Taiwan, so choose this region, you can pick another region where your office is) <br />
Trigger: HTTP, Allow unauthenticated invocations and require HTTPS <br />
Runtime environment variables: add a variable to save SLACK_SIGNING_SECRET <br />
Choose Code Runtime: Python 3.10 <br />
Entry point: example, modify by yourself <br />
reference: <https://cloud.google.com/functions/docs/tutorials/slack> <br />

## how to fix timeout issue?
this issue can't be fixed, we only can set the max waiting time 3600 seconds in RUNTIME - Timeout settings. <br />
After 1 hour of no activity, send a command to bot, it still returns a timeout error. <br />
After bot's timeout error, it will work again in one hour <br />