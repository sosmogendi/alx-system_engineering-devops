# Distributed Web Infrastructure Project

This project aims to design a distributed web infrastructure that hosts the website www.foobar.com. The infrastructure includes multiple components such as servers, a load balancer, web server, application server, and a database. The goal is to create a resilient and efficient setup to serve the website while maintaining high availability and performance.

## Project Structure

The distributed web infrastructure consists of the following components:

- **Load Balancer (HAproxy):** This component balances incoming traffic across the two servers for even distribution of workloads.

- **Servers (Server 1 and Server 2):** These servers host instances of Nginx (web server) and the application server. The application files are stored on these servers.

- **Web Server (Nginx):** Nginx serves as the web server that handles HTTP requests, serves static files, and forwards dynamic requests to the application server.

- **Application Server:** The application server processes dynamic content, executes business logic, and interacts with the database to retrieve and store data.

- **Database (MySQL):** The MySQL database stores the website's data, including user information and content.

## Getting Started

To set up and deploy this distributed web infrastructure, follow these steps:

1. Clone this repository to your local machine.

2. Configure the servers, load balancer, Nginx, application server, and MySQL database according to your environment.

3. Upload your application code base to the servers and configure the Nginx and application server accordingly.

4. Set up the MySQL database and import any necessary data.

5. Configure the HAproxy load balancer to distribute incoming traffic to the servers.

6. Ensure that SSL certificates are properly configured for secure communication.

7. Set up monitoring clients, such as data collectors for Sumo Logic, to monitor performance, security, and issues.

## Additional Information

For detailed explanations of the roles and responsibilities of each component, refer to the accompanying documentation in this repository.

## Issues and Challenges

While this distributed web infrastructure enhances availability and performance, it's important to be aware of certain challenges:

- **SSL Termination at Load Balancer:** Termination of SSL at the load balancer level might expose decrypted data, necessitating careful handling of encrypted traffic.

- **MySQL Write Scalability:** Having only one MySQL server capable of accepting writes can lead to performance bottlenecks and limited write scalability.

- **Uniform Server Components:** Using identical server components might lead to resource contention and hinder performance optimization.

## Conclusion

By implementing this distributed web infrastructure, we aim to provide a reliable, high-performing, and secure environment for hosting the website www.foobar.com. While addressing challenges, we strive to ensure smooth user experiences and efficient resource utilization.

Feel free to contribute, modify, or customize this infrastructure according to your project requirements.
