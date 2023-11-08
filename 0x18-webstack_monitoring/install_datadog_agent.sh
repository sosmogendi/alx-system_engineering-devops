#!/usr/bin/env bash
# This script automates the setup for Task 0: Webstack Monitoring with Datadog

# Function to install Datadog agent on Ubuntu 16.04
install_datadog_agent() {
    echo "Installing Datadog agent..."
    DD_API_KEY="YOUR_API_KEY" # Replace with your Datadog API key
    DD_APPLICATION_KEY="YOUR_APPLICATION_KEY" # Replace with your Datadog application key
    DD_HOSTNAME="XX-web-01" # Replace XX with your desired prefix

    # Add the Datadog APT repository
    sudo sh -c "echo 'deb https://apt.datadoghq.com/ stable main' > /etc/apt/sources.list.d/datadog.list"
    
    # Import Datadog GPG key
    sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 C7A7DA52

    # Update package list
    sudo apt-get update

    # Install Datadog agent
    sudo apt-get install -y datadog-agent

    # Configure Datadog agent
    sudo sed -i -e "s/api_key:.*/api_key: $DD_API_KEY/" /etc/datadog-agent/datadog.yaml
    sudo sed -i -e "s/application_key:.*/application_key: $DD_APPLICATION_KEY/" /etc/datadog-agent/datadog.yaml
    sudo sed -i -e "s/# hostname:.*/hostname: $DD_HOSTNAME/" /etc/datadog-agent/datadog.yaml

    # Restart Datadog agent
    sudo service datadog-agent restart

    echo "Datadog agent installed and configured."

    # Validate server visibility in Datadog (you can add your validation here)
    # You may need to wait for some time for the server to appear in Datadog.

    # Add any additional validation steps here
}

# Main script
install_datadog_agent
