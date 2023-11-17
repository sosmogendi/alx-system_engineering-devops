# Web Stack Debugging #4

## Description
This project focuses on debugging and configuring a web stack using Puppet manifests on Ubuntu 14.04 LTS. The goal is to ensure that all Puppet manifests pass linting tests, run without errors, and conform to specific guidelines provided.

## Requirements
- Operating System: Ubuntu 14.04 LTS
- All files should end with a new line.
- Ensure there's a README.md file at the root of the project folder.
- Puppet manifests must:
  - Pass `puppet-lint` version 2.1.1 without errors.
  - Run without any errors.
  - Have the first line as a comment explaining the purpose of the manifest.
  - Use the file extension `.pp`.
- Tools: Files will be checked with Puppet v3.4.

## Installation
To install `puppet-lint` version 2.1.1, use the following commands:

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
