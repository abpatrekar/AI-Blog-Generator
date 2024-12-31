# API Testing: Generic FURPS+/User Stories

**Each team will have to modify to implement user stories for the specific API chosen.**

Develop an application using free APIs like JokeAPI, NewsAPI, REST Countries API, etc. that can be used to demonstrate testing using POSTMAN.

A Web-Based application will require development using Flask or Django.  You will also need to use Flask or Django for your Web Application Testing Lab.

## FURPS+ Requirements

### Functionality

- Requirement:  The Python application, whether CLI or web-based, must interact with a chosen free API (like JokeAPI, NewsAPI, REST Countries API) to fetch and display data based on user input or predefined criteria.
- User Story: As a user, I want to interact with the chosen API through either a command line or a web interface, developed in Python, based on my input or selection criteria (like country, category, or keyword).
- Testing Requirement: The application’s API endpoints must be testable using Postman.
- User Story (Testing): As a developer, I want to ensure that all API endpoints function correctly, and I can test these using Postman.

### Usability

- Requirement: The application should have a user-friendly interface (CLI or web-based), with clear instructions on how to use it.
- User Story: As a user, I want clear guidance on how to interact with the application so that I can use it without confusion.

### Reliability

- Requirement: The application should handle exceptions and errors gracefully, providing useful feedback to the user.
- User Story: As a user, I want informative feedback in case of errors or issues so I can understand what went wrong.

### Performance

- Requirement: The application should respond to user requests promptly and efficiently.
- User Story: As a user, I expect quick responses, and as a developer, I want to use Postman to test the API's performance.

### Supportability

- Requirement: The application should be maintainable, with well-documented code and a clear structure.
- User Story: As a future developer or maintainer, I want documented code and a suite of Postman tests for ongoing support.

### Plus (+) - Design, Implementation, Interface, Physical

- Design Requirement: The application should adhere to good software design principles, be scalable, and follow the API’s usage guidelines.
- Implementation Requirement: Implement the application using Python, with suitable libraries and frameworks for CLI (like argparse, click) or web (like Flask, Django).
- Interface Requirement: The application should provide an API interface (if web-based) or a clear command-line interface.
- Physical Requirement: Ensure the application is deployable and runnable in environments supporting Python, for both CLI and web interfaces.

### Generic User Stories for Development

- Interact with API
  - As a user, I want to interact with a free API to retrieve and view data based on my inputs or selections.
- Handle Various Data Types
  - As a user, I want to see different types of data (text, images, etc.) handled appropriately by the application.
- Customizable Queries
  - As a user, I want to customize my queries or requests to the API to filter or search for specific information.
- Error and Exception Handling
  - As a user, I want the application to provide clear error messages for invalid inputs or API errors, helping me understand what needs to be corrected.
- Responsive and Efficient Performance
  - As a user, I expect the application to perform efficiently, with minimal delays or loading times.
- Documentation and Help
  - As a user or developer, I want the application to include documentation or help options so that I can easily understand how to use or modify it.
- Adaptability and Scalability
  - As a developer, I want the application structure to be adaptable and scalable, allowing for the integration of additional features or APIs in the future.
- Postman Testing for Interfaces
  - As a developer, I want to create Postman tests that are applicable to either CLI or web-based endpoints of the Python application.
- Documentation for Interfaces
  - As a developer, I want comprehensive documentation that covers both CLI and web usage of the application, including API endpoint details.
- Environment Setup for CLI/Web API Testing
  - As a developer, I need to set up environments in Postman for testing either CLI commands or web API requests effectively.

### Example of ONE modification based on example group API project

Functionality

- Requirement: The application must provide top news headlines from the News API based on country and category.
- User Story: As a user, I want to be able to specify the country and category for the news so that I can receive relevant top headlines.

User Stories for Development

- View Top Headlines
- As a news reader, I want to view the top headlines so that I can stay informed about current events.
