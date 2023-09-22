# Configuration Management and DevOps Project

## Overview

This project focuses on configuration management, DevOps practices, and system administration using Puppet on an Ubuntu 20.04 LTS system. The goal is to set up and manage a server environment efficiently, ensuring that Puppet manifests are well-structured and adhere to best practices.

## Table of Contents

- [Background Context](#background-context)
- [Requirements](#requirements)
  - [General](#general)
  - [Note on Versioning](#note-on-versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [CI/CD](#cicd)
- [Project Structure](#project-structure)

## Requirements

### General

- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A README.md file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension .pp.

### Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

#### Install puppet

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

