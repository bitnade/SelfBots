# 🛡️ Discord Zade Self-Bot

A professional-grade Discord self-bot built with `discord.py-self`. Features advanced cleanup logic, interactive visual archives, terminal-based remote control, and multi-layered rate-limit protection.

---

## ✨ Key Features
-   **🛡️ Vast Rate-Limit Protection:** Multi-layered jitter, batch cooling, and dynamic 429 error handling to keep your account safe during mass deletions.
-   **💻 Terminal Console:** Control your bot directly from the terminal. Supports remote clearing by ID and status updates.
-   **🎯 Targeted Cleanup:** Delete messages or reactions in any DM or channel using their ID, even if you aren't active in them.
-   **📊 Interactive HTML Archives:** Generates beautiful, Discord-themed chat logs with live CDN avatars and clickable user profile modals.
-   **🤖 Persistent Automation:** Full Auto-Responder system (`.ar`) and custom message triggers (`.msg`) saved via JSON.
-   **🟣 Advanced Presence:** Streaming status, Watching/Listening/Competing modes, and Rich Presence buttons.
-   **🔍 Utility Suite:** Built-in Snipe, Calculator, Avatar fetcher, and Detailed User Info.

---

## 🚀 Installation Guide & Quick Start

1.  **Install Dependencies:**
    Make sure you have Python installed, then run:
    ```bash
    pip install discord.py-self python-dotenv chat-exporter pyfiglet
    ```
2.  **Configure `.env`:**
    Create a file named `.env` in the same folder:
    ```env
    # Your Discord user token (NOT a bot token)
    DISCORD_TOKEN=your_token_here

    # Command prefix — change to any character you like (default: .)
    PREFIX=.
    ```
    *(To find your token: Open Discord in your browser > DevTools `F12` > Application > Local Storage > `token`)*
3.  **Run the Bot:**
    ```bash
    python main.py
    ```
    The bot auto-generates `config.json`, `auto_responses.json`, and `rpc_config.json` on first run.

---

## 🗂️ Configuration Files

| File | Purpose |
| :--- | :--- |
| `.env` | Token and command prefix |
| `auto_responses.json` | Auto-Responder triggers (managed by `.ar` commands) |
| `rpc_config.json` | Rich Presence settings (managed by `.rpc` commands — persists across restarts) |
| `config.json` | Saved custom messages (used by `.msg`) |

---

## 💻 Console Commands (Type in Terminal)
| Command | Description |
| :--- | :--- |
| `clear <id> <n/all>` | Clears messages in a specific Channel or DM ID. |
| `cr <id> <n/all>` | Full cleanup (msgs + reactions) in a specific ID. |
| `status <text>` | Updates your status directly from the terminal. |
| `panic` | Immediate emergency shutdown of the bot. |

---

## 📜 Discord Commands (Default Prefix: `.`)
> The prefix can be changed in `.env` by setting `PREFIX=!` (or any character).

### 🧹 Cleanup & Safety
| Command | Alias | Description |
| :--- | :--- | :--- |
| `.clear <n/all> [id]` | `.c`, `.cl` | Clears your messages. (Optional ID for remote clear). |
| `.cr <n/all> [id]` | `.unreact` | Full Cleanup: Deletes your messages AND reactions. |
| `.ghost` | - | Toggles Invisible/Online mode (auto-deletes confirmation). |
| `.panic` | - | **Instant Kill:** Shuts down the bot immediately. |

### 🎭 Presence & Status
| Command | Description |
| :--- | :--- |
| `.rpc` | Shows the interactive Rich Presence Builder menu. |
| `.rpc set <name>` | Sets the main title of your Rich Presence. |
| `.rpc type <type>` | Sets activity type (play, watch, listen, stream, compete). |
| `.rpc img <large\|small> <url>` | Sets the large or small image (URL or asset key). |
| `.rpc button <label> \| <url>` | Adds clickable buttons to your RPC (Max 2). |
| `.rpc apply` | Pushes the configured Rich Presence to your profile. |
| `.status <txt>\|<det>`| Sets advanced simple status (e.g., `.s Playing\|Level 99`). |
| `.stream <title>\|<url>`| Sets Streaming status with custom Twitch URL and details. |

### 🤖 Automation & Utility
| Command | Alias | Description |
| :--- | :--- | :--- |
| `.ar` | - | Shows Auto-Responder help & available modes. |
| `.ar add <trigger>\|<reply>` | - | Adds a trigger (DM only by default). |
| `.ar add <trigger>\|<reply>\|<mode>` | - | Adds a trigger with a specific scope mode. |
| `.ar add <trigger>\|<reply>\|guild\|<id1,id2>` | - | Adds a trigger scoped to specific server IDs. |
| `.ar mode <trigger> <mode> [ids]` | - | Changes the scope of an existing trigger. |
| `.ar list` | - | Lists all triggers with their scope. |
| `.ar remove <trigger>` | - | Removes a trigger. |
| `.msg <name>` | - | Sends a saved message from `config.json`. |
| `.sd <sec> <text>` | - | Sends a Self-Destructing message that deletes after X seconds. |
| `.react <n> <emoji>`| - | Reacts to the last N messages with the specified emoji. |
| `.tr <lang> <text>` | - | Translates text to the specified language (e.g., `.tr es Hello`). |
| `.embed <title>\|<txt>`| - | Creates a fake embed block using ANSI colors. |
| `.ascii <txt>` | - | Generates 3D ASCII art text using pyfiglet. |
| `.calc <math>` | - | Evaluates mathematical expressions (e.g., `.calc 5*5`). |
| `.archive [@user]` | - | Generates an interactive HTML log of a channel or DM. |
| `.snipe` | - | Shows the last message deleted in the channel. |
| `.avatar <@user>` | `.av` | Fetches a user's high-res profile picture link. |
| `.info <@user>` | `.whois` | Shows detailed user/account information. |

### ⚙️ Account Management
| Command | Description |
| :--- | :--- |
| `.block <@user>` | Mass deletes your messages with a user and blocks them. |
| `.guilds` | Lists the first 15 servers you are currently in. |
| `.leave <id>` | Leaves a specific server by its ID. |
| `.friends` | Lists your current friends. |
| `.perms [@user]` | Checks your (or another user's) permissions in the current channel. |

---

## ⚠️ Safety Warning
Self-bots are against Discord's ToS. This bot includes advanced rate-limiting and humanized delays to minimize risk, but use it responsibly. Avoid mass-deleting thousands of messages in a single session.

---

## 📬 Contact Me

Have questions, suggestions, or just want to connect? Reach out!

[![Discord](https://img.shields.io/badge/Discord-Prince-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/users/Prince)
[![GitHub](https://img.shields.io/badge/GitHub-Prince-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Prince)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your@email.com)

