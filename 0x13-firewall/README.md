### Firewall
This project involves configuring a firewall for a set of servers, with a focus on security, DevOps, and SysAdmin tasks. The goal is to ensure that the servers are secure, and only necessary connections are allowed while blocking unauthorized access.

## Concepts

The project is expected to cover the concept of "Web stack debugging."

## Background Context

Your servers currently do not have a firewall. It's essential to understand that improper firewall configuration can lead to loss of access to your servers. So, exercise caution when implementing firewall rules.

## Important Warning

Be extremely careful with firewall rules, particularly regarding port 22 (SSH). Blocking this port without proper access may lead to losing SSH access to your servers. If you're using UFW, remember that port 22 is blocked by default and should be unblocked before logging out of your server.

## Testing

To test your firewall configuration on "web-01," perform the test from outside of the school network, such as from your "web-02" server. This ensures that the traffic originates from "web-02" and not the school's network, bypassing the firewall.
