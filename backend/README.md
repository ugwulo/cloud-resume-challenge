# Backend Implementation

The backend API is written in Python and deployed to Azure Function service which interacts with the Cosmos DB to retrieve the counter item.

## Unit Testing
In order to reduce errors and save hours of debugging, writing unit tests are important and it also helps with documentation
All tests must pass before deployment.
I implemented a unit test for the backend API to check the Cosmos DB count item increments on every API call
The test uses the [Pytest](https://docs.pytest.org/) tool.