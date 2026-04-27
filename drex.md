# Discord D-Rex Selfbot

A powerful, feature-rich Discord self-bot built with `discord.js-selfbot-v13`. Designed for utility, automation, and stealth.

> **Warning:** Self-bots are against Discord's Terms of Service. Use this at your own risk.

## ✨ Features

- 🧹 **Cleanup:** Purge your own messages or clear reactions.
- 👻 **Stealth:** Ghost mode (invisible toggle) and message snipers.
- 🎮 **Status:** Custom RPC, streaming status, and custom activity.
- 🛠️ **Utility:** Math calculator, ASCII art, avatar fetcher, and custom embeds.
- 🏰 **Management:** Join/leave servers and manage friends via commands.
- 🤖 **Automation:** Custom auto-responses and saved messages.

## 🚀 Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   DISCORD_TOKEN=your_account_token_here
   ALLOWED_USER_ID=optional_secondary_user_id
   ```

3. **Start the bot:**
   ```bash
   node index.js
   ```

## 🛠️ Commands

The default prefix is `.`.

| Category | Command | Description |
| :--- | :--- | :--- |
| **Cleanup** | `.clear <n/all>` | Delete `n` of your recent messages. |
| | `.cr <n>` | Delete messages and remove reactions. |
| | `.sd <sec> <msg>` | Send a message that self-destructs after `sec`. |
| **Stealth** | `.ghost` | Toggle between online and invisible. |
| | `.block <@user>` | Block a user. |
| | `.snipe` | View the last deleted message in the channel. |
| **Status** | `.rpc <text>` | Set "Playing" activity. |
| | `.stream <text>` | Set "Streaming" activity. |
| | `.status <txt\|det>` | Set a custom status with details. |
| **Utility** | `.calc <exp>` | Calculate a mathematical expression. |
| | `.av [@user]` | Get a user's avatar. |
| | `.ascii <text>` | Generate ASCII art text. |
| | `.embed <t\|c>` | Send a stylized text separator. |
| **Account** | `.guilds` | List joined servers. |
| | `.join <code>` | Join a server via invite code/link. |
| | `.leave [id]` | Leave current or specified server. |
| | `.friends` | List your friends. |
| | `.addfriend <id>` | Send a friend request. |
| **Automation**| `.ar add <k\|v>` | Add an auto-response (Key \| Value). |
| | `.msg <name>` | Send a saved message. |

## 🛡️ Safety & Stability

- **Global Error Handling:** Prevents crashes from unhandled rejections.
- **Cooldowns:** Built-in rate limiting to prevent API spam.
- **Randomized Delays:** Mimics human behavior with random delays between actions.

## 📝 License

This project is licensed under the ISC License.

---

## 📬 Contact Me

Have questions, suggestions, or just want to connect? Reach out!

[![Website](https://img.shields.io/badge/Website-Bitnade-4BC51D?style=for-the-badge&logo=google-chrome&logoColor=white)](https://bitnade.com)
[![Discord](https://img.shields.io/badge/Discord-Bitnade-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/et8q3CZsf5)
[![GitHub](https://img.shields.io/badge/GitHub-Bitnade-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Bitnade)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@bitnade.com)
