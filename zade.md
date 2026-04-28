# 🛡️ Discord Zade Self-Bot

A professional-grade Discord self-bot built with `discord.py-self`. Features advanced cleanup logic, interactive visual archives, terminal-based remote control, and multi-layered rate-limit protection.

---

## ✨ Key Features
-   **🛡️ Vast Rate-Limit Protection:** Multi-layered jitter, batch cooling, and dynamic 429 error handling to keep your account safe.
-   **💻 Terminal Console:** Control your bot directly from the terminal. Supports remote clearing by ID and status updates.
-   **🎯 Targeted Cleanup:** Delete messages or reactions in any DM or channel using their ID, even if you aren't active in them.
-   **📊 Interactive HTML Archives:** Generates beautiful, Discord-themed chat logs with live CDN avatars and clickable user profile modals.
-   **🤖 Persistent Automation:** Full Auto-Responder system (`.ar`) and custom message triggers (`.msg`) saved via JSON.
-   **🟣 Advanced Presence:** Streaming status, Watching/Listening/Competing modes, and Rich Presence buttons.
-   **🔍 Utility Suite:** Built-in Snipe, Calculator, Avatar fetcher, Translator, and Detailed User Info.
-   **🔤 Text Effects:** Mock text, Reversing, and Zalgo corruption.

---

## 🚀 Installation Guide

1.  **Install Dependencies:**
    Make sure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure `.env`:**
    Create a file named `.env` in the root directory:
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

---

## 🗂️ Configuration Files

| File | Purpose |
| :--- | :--- |
| `.env` | Token and command prefix |
| `auto_responses.json` | Auto-Responder triggers (managed by `.ar` commands) |
| `rpc_config.json` | Rich Presence settings (managed by `.rpc` commands) |
| `config.json` | Saved custom messages (managed by `.msg` commands) |

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

### 🧹 Cleanup & Safety
| Command | Alias | Description |
| :--- | :--- | :--- |
| `.clear <n/all> [id]` | `.c`, `.cl` | Clears your messages. (Optional ID for remote clear). |
| `.cr <n/all> [id]` | `.unreact` | Full Cleanup: Deletes your messages AND reactions. |
| `.block [@user]` | - | Mass deletes your messages with a user and blocks them. |
| `.nuke [msg]` | - | Deletes and recreates the current channel (if you have perms). |
| `.ghost` | - | Toggles Invisible/Online mode. |
| `.panic` | - | **Instant Kill:** Shuts down the bot immediately. |

### 🎭 Presence & Status
| Command | Description |
| :--- | :--- |
| `.rpc` | Shows the interactive Rich Presence Builder menu. |
| `.rpc set <name>` | Sets the main title of your Rich Presence. |
| `.rpc apply` | Pushes the configured Rich Presence to your profile. |
| `.rpc clear` | Clears your current Rich Presence. |
| `.status <text>` | Sets activity or status (online, dnd, idle, invisible). |
| `.stream <title>\|<url>`| Sets Streaming status with custom Twitch URL and details. |

### 🛠️ Utility
| Command | Alias | Description |
| :--- | :--- | :--- |
| `.archive [@user]` | - | Generates an interactive HTML log of a channel or DM. |
| `.calc <math>` | - | Evaluates mathematical expressions (e.g., `.calc 5*5`). |
| `.snipe` | - | Shows the last message deleted in the channel. |
| `.av <@user>` | `.avatar` | Fetches a user's high-res profile picture link. |
| `.whois <@user>` | `.info` | Shows detailed user/account information and roles. |
| `.perms [@user]` | - | Checks your (or another user's) permissions in the channel. |
| `.sd <sec> <msg>` | - | Sends a Self-Destructing message. |
| `.countdown <n>` | - | Starts a countdown from N. |
| `.schedule <min> <msg>`| - | Sends a message after a specified delay. |
| `.fake <text>` | - | Generates a fake forwarded message block. |
| `.typing <on/off>` | - | Toggles your typing indicator. |
| `.steal <emoji> [name]`| - | Steals a custom emoji and adds it to your server. |
| `.reload` | - | Reloads data from disk (configs, etc). |

### ✨ Fun & Visuals
| Command | Description |
| :--- | :--- |
| `.react <n> <emoji>`| Reacts to the last N messages with the specified emoji. |
| `.tr <lang> <text>` | Translates text (e.g., `.tr es Hello`). Use `.tr list` for languages. |
| `.ascii <text>` | Generates 3D ASCII art text. |
| `.embed <title>\|<txt>`| Creates a fake embed block using ANSI colors. |
| `.txt mock <text>` | AlTeRnAtInG cApS. |
| `.txt rev <text>` | Reverse text. |
| `.txt zalgo <text>` | Z̸̢͔͝a̷̢̛l̵̰͑g̶̟͝o̶ corruption. |

### 👤 Account & Automation
| Command | Description |
| :--- | :--- |
| `.guilds` | Lists the servers you are currently in. |
| `.friends` | Lists your current friends. |
| `.leave <id>` | Leaves a specific server by its ID. |
| `.ar add <trg>\|<rsp>`| Adds an auto-response trigger. |
| `.ar list` | Lists all active auto-responses. |
| `.ar remove <trg>` | Removes an auto-response. |
| `.msg add <nm>\|<txt>`| Saves a custom message. |
| `.msg list` | Shows all saved messages. |
| `.msg <name>` | Sends a saved message. |

---

## 📝 License
This project is licensed under the ISC License.

---

## ⚠️ Safety Warning
Self-bots are against Discord's ToS. This bot includes advanced rate-limiting and humanized delays to minimize risk, but use it responsibly. Avoid mass-deleting thousands of messages in a single session.

---

## 📬 Contact Me

[![Website](https://img.shields.io/badge/Website-Bitnade-4BC51D?style=for-the-badge&logo=google-chrome&logoColor=white)](https://bitnade.com)
[![Discord](https://img.shields.io/badge/Discord-Bitnade-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/et8q3CZsf5)
[![GitHub](https://img.shields.io/badge/GitHub-Bitnade-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Bitnade)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@bitnade.com)
