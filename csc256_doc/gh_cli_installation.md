# Working with GitHub and Git

**GitHub CLI, Git, GitHub Desktop**, and the **GitHub Web Interface** are all tools related to using GitHub, but they serve different purposes and cater to different user needs and preferences. Let's explore how they differ:

## Git

- **Nature:** Git is a distributed version control system, primarily used for source code management.
- **Functionality:** It allows users to track changes in any set of files, usually for coordinating work among programmers collaboratively developing source code.
- **Usage:** Git operates locally. Changes are made to a local repository and can be synchronized with other repositories.
- **Interface:** It is primarily a command-line tool, though many graphical user interfaces (GUIs) are available for it.
- **Scope:** Git is not tied to GitHub; it can be used with any Git repository, whether hosted on GitHub, GitLab, Bitbucket, a private server, or elsewhere.

## GitHub CLI (gh)

- **Nature:** GitHub CLI is a command-line tool specifically designed to interact with GitHub features.
- **Functionality:** It extends GitHub functionality to the command line, allowing users to manage pull requests, issues, releases, gists, and more without leaving the terminal.
- **Usage:** It's focused on GitHub services and is used to interact with repositories hosted on GitHub.
- **Interface:** It operates through the command line.
- **Scope:** While Git manages the version control aspects, GitHub CLI handles GitHub-specific features that are not part of Git’s scope, like issues and pull requests.

## GitHub Desktop

- **Nature:** GitHub Desktop is a graphical user interface (GUI) application for interacting with **GitHub** and **Git**.
- **Functionality:** It simplifies the use of Git and GitHub, with a focus on ease of use, especially for users less comfortable with command-line tools.
- **Usage:** Ideal for those who prefer a visual interface over command-line operations. It provides a visual representation of Git commands.
- **Interface:** It’s a desktop application with a graphical user interface.
- **Scope:** Like GitHub CLI, it’s designed to work with GitHub, but it also supports basic Git functionalities. It does not, however, offer the full range of GitHub-specific features like managing issues and pull requests.

## GitHub Web Interface

- **Nature:** This is the web-based interface of GitHub accessible through a browser.
- **Functionality:** Offers comprehensive access to all GitHub features, including repository hosting, code review, issue tracking, wikis, and more.
- **Usage:** Suitable for users who prefer working in a web browser and need access to the full suite of GitHub features.
- **Interface:** It is accessed through any web browser.
- **Scope:** It covers all GitHub functionalities and is often more feature-rich in terms of repository management and collaboration tools than the other options.

## **Is Git Needed for GitHub CLI and GitHub Desktop?**

- **Git** must be installed in order to maximize use of **GitHub Desktop** and **GitHub CLI**.  

- While **GitHub CLI** enhances and streamlines your interaction with GitHub, **Git** remains the essential tool for handling the version control aspects of your code. Therefore, having Git installed is a prerequisite for a fully functional development workflow with GitHub CLI.
- **Git** needs to be installed for **GitHub Desktop** to function properly. **GitHub Desktop** is a graphical user interface that integrates with **Git**, the distributed version control system. While GitHub Desktop simplifies many of the common Git commands and processes through its user-friendly interface, it still relies on the underlying Git system for version control operations.

  - When you install GitHub Desktop, it typically includes an embedded version of Git. This means that you don't necessarily have to install Git separately before using GitHub Desktop; it comes with everything needed to start working with Git repositories.

  - However, if you plan to use Git features outside of GitHub Desktop, such as through a terminal or command prompt, you might still want to install Git separately. This can ensure that you have access to the latest features and updates of Git.
- ** In order to clone the **Wiki** repository which is separate from the -main- repo, you need to use Git or GitHub CLI.  Currently GitHub Desktop does not support this.

## Key features and Functionalities of GitHub CLI

- Repository Management: You can create, clone, fork, and view repositories directly from the command line.

- Issues and Pull Requests: It allows you to create, view, edit, and manage issues and pull requests. This feature is particularly useful for managing workflows around code review and collaboration.

- GitHub Actions: You can view logs, run, and manage GitHub Actions directly from your terminal. This is helpful for automating and streamlining your development workflow.

- Gists: Create and manage gists, which are a simple way to share snippets or larger chunks of code or text.

- Seamless Navigation: The tool enables seamless navigation to relevant pages on the GitHub website for further detailed actions or visual interface, if necessary.

- Scripting and Automation: Since it's a command-line tool, it can be used in scripts and automated tasks, making it easier to integrate GitHub functionality into larger automated workflows.

## GitHub CLI is available for Windows, Mac, and Linux

GitHub CLI is designed to work well with a variety of terminal applications. Its purpose is to bring GitHub functionality to your terminal, making it more accessible for tasks that would otherwise require using the GitHub website or a Git client. This tool is particularly beneficial for those who are comfortable with a text-based interface and looking to streamline their GitHub workflow.

## **INSTALLATION INSTRUCTIONS for GitHub CLI**

## Windows OS

### 1. Download the GitHub CLI

- Go to the GitHub CLI release page (<https://cli.github.com/>).
- Download the latest ***.msi*** file for Windows.
- Install GitHub CLI:
  - Run the downloaded ***.msi*** file.
  - Follow the installation prompts.

### 2. Verify Installation

- Open Command Prompt.
- Type ***gh --version*** and press [Enter]. This will display the GitHub CLI version if installed correctly.

### 3. Login to GitHub

- In Command Prompt, type ***gh auth login*** and press [Enter].
- Follow the prompts to authenticate via a web browser.
  - The CLI will provide instructions for completing authentication, usually involving opening a browser and entering a code.
  - Follow these instructions to log in to your GitHub account through the CLI.
  
![cmd_line_login](https://github.com/Talonness/sp24_lessons/blob/main/assets/ghcli.png)
  ![cmd line login](gh_cli_installation.png)

## For Mac

### 1. Install Homebrew (if not already installed)

- Open Terminal.
- Enter ***/bin/bash -c "$(curl -fsSL <https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh>"*** and press [Enter].
- Follow the installation instructions.

### 2. Install GitHub CLI

- In Terminal, type ***brew install gh***.

### 4. Verify Installation

- In Terminal, type ***gh --version*** and press Enter. This will display the GitHub CLI version if installed correctly.

### 5. Login to GitHub

- In Terminal, type ***gh auth login*** and press [Enter].
- Follow the prompts to authenticate via a web browser.
