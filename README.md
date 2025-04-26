# TestChat - Real-Time Chat Application

A simple and real-time chat application built with Python and Flet framework. This application allows multiple users to chat in real-time through a web browser interface.

![TestChat Preview](https://raw.githubusercontent.com/flet-dev/flet/main/media/controls/banner.png)

## Features

- 💬 Real-time messaging
- 👤 User identification system
- 🕒 Message timestamps
- 🎨 Clean and modern interface
- 🌐 Web browser based
- 📱 Responsive design
- 🔄 Auto-scroll chat
- 🎯 System notifications for user join events

## Requirements

- Python 3.7 or higher
- Flet package

## Installation

1. Clone this repository:
```bash
git clone [https://github.com/paulojrtoledo/realtime_chatapplication.git]
cd [realtime_chatapplication.git]
```

2. Install the required package:
```bash
pip install flet
```

## Usage

1. Run the application:
```bash
python chat_app.py
```

2. The chat will automatically open in your default web browser at `http://localhost:8550`

3. Enter your name to join the chat

4. Start chatting!

## How It Works

The application uses Flet, a Python framework for building interactive multi-user web applications. Key features include:

- **Real-time Updates**: Uses Flet's pubsub system for instant message delivery
- **User Management**: Tracks user sessions and displays join notifications
- **Message System**: Supports text messages with timestamps
- **UI Components**: Utilizes Flet's material design components for a modern look

## Project Structure

```
.
├── README.md
└── chat_app.py
```

## Contributing

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature suggestions.

## License

This project is open source 

## Credits

Built with [Flet](https://flet.dev/) - A Python framework for building interactive multi-user web applications. 