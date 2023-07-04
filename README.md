# CloudResumeChallenge: my resume built serverlessly in Azure

Here is my solution to the [Azure](https://cloudresumechallenge.dev/docs/the-challenge/azure/)

View it live [here](https://resume.ugwulo.me)


## Prerequisites

- [GitHub Account](https://github.com/join)
- [Azure Account](https://portal.azure.com/)

` The front-end is a static site with HTML, CSS, and JavaScript. It's static and has a visitor counter. The visitor counter data is fetched via an API call to the Azure Function.`

- I am not great in frontend, I used this [template](https://www.styleshout.com/free-templates/ceevee/) to create my frontend. 
- I'm also no JavaScript dev, but this [article](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-fetch-api-to-get-data) explains well and in a simple way how to use it to make an API call.


## Frontend CI/CD Workflow
It can be painful and time consuming to manually update, track and deploy code changes to production after testing.
To overcome this, I needed to implement a CI/CD workflow using Github Actions.

## Unit Testing
In order to reduce errors and save hours of debugging, writing unit tests are important and it also helps with documentation
All tests must pass before deployment
I implemented a unit test for the backend API to...

- TODO
## Monitoring Notifications In Slack