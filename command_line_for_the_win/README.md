# Command Line for the Win Project

## Introduction

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line, and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

This project is NOT mandatory at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won’t get hurt if you don’t do it, but if your current average is greater than your score on this project, your average might go down. Have fun!

## Requirements

### General

- A README.md file, at the root of the folder of the project, is mandatory.
- This project will be manually reviewed.
- As each task is completed, the name of that task will turn green.
- Create a screenshot, showing that you completed the required levels.
- Push this screenshot with the right name to GitHub, in either the PNG or JPEG format.

### Specific

In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

## SFTP File Transfer Steps

To transfer the screenshots from your local machine to the sandbox environment, follow these steps:

1. **Open a Terminal or Command Prompt**:
   - Open a new terminal or command prompt on your local machine (Windows).

2. **Establish an SFTP Connection**:
   - Use the `sftp` command to establish an SFTP connection to the sandbox environment. Replace `username`, `sandbox_hostname`, and `sandbox_password` with your actual credentials provided for the sandbox:

   ```bash
   sftp username@sandbox_hostname
