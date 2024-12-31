# Selenium and Playwright Requirements

The following are areas that Selenium and Playwright can test.  They can perform a wide range of tests to ensure the functionality, reliability, and performance of web applications. Your lab must demonstrate the tests that have a MANDATORY.  This means your web application must have the entities to be tested.  For example,  to perform a form submission test your application must have a form.  This means your web application must have a form that can be tested.  Here's a list of specific things that must be testable in your web application.

1. Functional Testing

- MANDATORY: Form Submissions: Test form filling, submissions, and validation messages.
- MANDATORY: Link and Button Clicks: Automate clicking on various links and buttons to ensure they lead to the correct actions or pages.
- MANDATORY: Dropdown Menus: Test interactions with dropdown menus, including selecting various options.

2.User Interaction Simulation

- MANDATORY: Mouse Actions: Simulate mouse actions like clicks, double-clicks, hover, and drag-and-drop.
- MANDATORY: Keyboard Inputs: Test keyboard interactions, including text input and keyboard shortcuts.
- Scrolling: Ensure pages and elements scroll correctly.

3.UI Component Testing

- MANDATORY: Visibility Checks: Verify if certain elements are visible or hidden under specific conditions.
- MANDATORY: Layout Testing: Check the layout and positioning of UI components.
- MANDATORY: Styling Validation: Verify the correct application of CSS styles.

4.Navigation and Workflow Testing

- MANDATORY: Page Navigation: Test navigation between different pages or sections of the application.
- Breadcrumbs: Validate the functionality of breadcrumb navigation.
- Workflow Simulation: Test entire user workflows from start to finish.

5.Data Handling and Validation

- MANDATORY: Data Entry and Retrieval: Test CRUD (Create, Read, Update, Delete) operations on data.
- Data Validation: Ensure the correctness of data processing and output.

6.Responsive Design Testing

- Different Viewports: Test how the application looks and behaves on different screen sizes and devices.
- Media Query Behavior: Check if responsive design elements react correctly to changes in viewport dimensions.

7.Cross-Browser Testing

- Compatibility: Test application compatibility across different browsers.
- Feature Support: Verify that all features work correctly in each supported browser.

8 Performance Testing

- Load Times: Measure how long pages and resources take to load.
- Resource Usage: Monitor the usage of resources like memory and CPU during different operations.

9.Error and Exception Handling

- Error Messages: Test for correct error messages under various error conditions.
- Handling Exceptions: Ensure the application handles unexpected exceptions gracefully.

10. Accessibility Testing

- Screen Reader Compatibility: Test compatibility with screen readers and other assistive technologies.

- Keyboard Navigation: Ensure the application is fully navigable using a keyboard.

11.Security Testing (Basic)

- Input Validation: Check for vulnerabilities like SQL injection, XSS via form inputs.

- Secure Connections: Verify if secure pages use HTTPS and if data is transmitted securely.
Advanced Testing with Playwright
In addition to the above, Playwright offers some advanced testing capabilities:
- Multi-Page Scenarios: Test scenarios involving multiple browser tabs or windows.
- Network Interception: Intercept and mock network requests for testing offline behavior or API failures.
- Headless Browser Testing: Run tests in headless browsers for faster execution.
- Both Selenium and Playwright can be integrated into CI/CD pipelines for continuous testing. They are essential tools for ensuring the robustness and reliability of web applications in various environments and use cases.

For the first part of your lab **Student Demonstration** you can use [Formy](https://formy-project.herokuapp.com/) from Heroku and test all of the mandatory above.
For the second part of your lab: **Now you do it part of the lab** your web application must allow testing for those at least 5 of the mandatory above.
