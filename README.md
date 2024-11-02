# NeoLogger

![PyPI Downloads](https://static.pepy.tech/badge/neologger)     
[neologger package in PyPi.org](https://pypi.org/project/neologger/)    


<p align="center">
  <img src="docs/imgs/neologger_banner.png" alt="NeoLogger Banner">
</p>

A collection of Python notification classes for enhanced logging, messaging, and Slack notifications.

## Overview

NeoNotifications provides a set of tools to improve logging output with customizable styles, send messages over STOMP protocol, and send Slack notifications with rich formatting.

## Features

- **NeoLogger**: Advanced logging with customizable colors, styles, and templates.
- **StompBabbler**: Send messages over STOMP protocol to a specified queue.
- **SlackNotification**: Assemble and send richly formatted notifications to Slack channels via webhooks.

## Installation

You can install NeoNotifications via pip:

```bash
pip install neologger
```

## Requirements

Python 3.6 or higher

## Dependencies:
stomp.py    
requests

## Package Content

- [NeoLogger](docs/neologger.md)    
Examples of NeoLogger usage as well as examples for customisation for logs.

- [SlackNotifications](docs/slacknotifications.md)    
Examples of Slack Notification usage as well as examples for custom for notifications.

- [StompBabbler](docs/stompbabbler.md)    
Examples of Stomp Notification usage.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Inspired by the need for customizable logging and notification tools in Python applications.

Utilizes the stomp.py library for STOMP protocol messaging.     
Utilizes the requests library for HTTP requests to Slack webhooks.

## Contact

For questions or suggestions, please contact Pablo Martinez at neolink3891@gmail.com    

You can also connect with me on [LinkedIn](https://www.linkedin.com/in/orlando-martinez-2649051aa).