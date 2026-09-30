# Python Chat Application — Beginner Version

A two-script command-line chat using Python TCP sockets and threads. Run the server, then connect two or more clients on the same computer using `localhost`.

## Run on Windows

1. Open Command Prompt or PowerShell in this folder, where `server.py` and `client.py` are saved.
2. Start the server:

   ```powershell
   python server.py
   ```

   Keep this window open. It should say the server is listening on `127.0.0.1:50000`.

3. Open a **second** Command Prompt window in this same folder and start the first client:

   ```powershell
   python client.py
   ```

   Choose a chat name, such as `Alice`.

4. Open a **third** Command Prompt window in this folder and start another client. Choose another name, such as `Bob`.
5. Type a message in either client and press Enter. Both clients should see the timestamped message. Type `/quit` in a client to leave; the other clients receive a departure notice.
6. Stop the server with **Ctrl+C** in its window.

No extra packages are required; `socket`, `threading`, and `datetime` are included with Python.

## How it works

- A **socket** is one endpoint of a network connection. The server binds to `127.0.0.1` (this computer) and port `50000`, then listens for connections.
- The client connects to that same host and port.
- TCP sends an ordered stream of bytes. This project sends each username and message as one UTF-8 line ending in `\n`.
- The server starts a **thread** for each client so it can receive messages from multiple clients at once.
- When a message arrives, the server adds the current time and username, then broadcasts it to connected clients.
- The client also has a receiving thread. This lets incoming messages appear while the user is typing.
- When `/quit` closes a client connection, the server removes it from the list and broadcasts a “left the chat” notice.

## Privacy and security

This beginner version binds to `127.0.0.1`, so it is intended for clients on the same computer. It does not save messages, use accounts, or encrypt chat content. Messages are sent as ordinary UTF-8 text over TCP and should be treated as unencrypted. Do not use this prototype for private or sensitive conversations. The server prints connection and disconnection details to its terminal; it does not store chat transcripts in a file or database.

## Advanced version roadmap

1. Build a Tkinter window with a scrolling message area and input box.
2. Add SQLite user registration and login. Store password hashes, never plain-text passwords.
3. Add rooms and route each message only to clients in that room.
4. Save each message with its room, sender, and timestamp; load a room's recent history when someone joins.
5. Add desktop notifications for new messages when the window is not focused.
6. Convert shortcodes such as `:smile:` to Unicode emoji before display.
7. Update this README with exactly where messages are stored and which network connections are encrypted. A localhost TCP socket alone does not provide end-to-end encryption.

## Learning references

- [Socket programming chat tutorial on YouTube](https://www.youtube.com/watch?v=bFamoBj5FbM)
- [Python networking chat tutorial search](https://www.youtube.com/results?search_query=Python+chat+app+socket+threading+tutorial)
- [Official Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Python Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
