# Discord Server Cloner

My own script to clone servers (not skided fuck you)

This script clones a Discord guild (server) using the Discord API and the Python `discord.py-self` library.

## Installation

1. Install the required Python libraries:

```bash
pip install discord.py-self aiohttp aiohttp_socks
```

2. Create a `proxy.txt` file containing a list of proxy servers, one per line.

## Usage

1. Replace the `TOKEN` variable in the script with your Discord user token.

2. Run the script:

```bash
python guild_cloner.py
```

3. Enter the IDs of the source and destination guilds when prompted.

## How it works

The script performs the following steps:

1. Connects to the Discord API using the user token.
2. Retrieves a random proxy server from the `proxy.txt` file.
3. Deletes existing content (categories, channels, roles) in the destination guild.
4. Clones categories, channels, and roles from the source guild to the destination guild.

## Limitations and Notes

- The script does not clone user-specific data, such as messages and permissions.
- Be aware of Discord API rate limits when using this script.
