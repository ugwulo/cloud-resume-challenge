# Frontend Implementation

The front-end is a static site with HTML, CSS, and JavaScript. It has a visitor counter. 
The visitor counter data is fetched via a HTTP trigger to the Azure Function.

- I am not great in frontend, I used this [template](https://www.styleshout.com/free-templates/ceevee/) to build my frontend. 
- I'm also no JavaScript dev, but this [article](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-fetch-api-to-get-data) explains well and in a simple way how to use it to make an API call.


## Frontend CI/CD Workflow
It can be painful and time consuming to manually update, track and deploy code changes to production after testing.
To overcome this, I needed to implement a CI/CD workflow using Github Actions.