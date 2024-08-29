# Problem Summary

My Discord community was in desperate need of revitalisation, and I created a Discord bot to do exactly that. Developed as part of our school project, the Discord bots aim was to streamline processes, create fun and enhance communication for our target audience. Designed to address several issues, the Discord bot offers a range of functions tailored to meet the needs of its users. From private administrative features, custom server events, API features, fun commands, polls and even counting, this Discord bot ensures an efficient and user-friendly experience. The initial goal was to solely rely on the one Discord bot to manage the entire Discord community, instead of using 6-7 already implemented Discord bots. These required hours of dedication to complete. Features such as administration and server protection were a priority and a must-have. Fun features such as polls and small games were also required to tick that fun-creation box. Our target audience included the people already present in the Discord community and all the people who were to join after the creation of the Discord bot. The Discord bot was designed to simplify tasks, allow the users to have fun together, and provide quick access to essential information for the administrators. By providing these fun but necessary features we revitalised the Discord community just as intended and brought new, fun things for the community to experiment with.

# Motivation & Research

There are numerous Discord bots that were a valuable inspiration to the creation of the Discord Bot. Discord bots such as Hydra, Yggdrasil, Maki, Dank Memer, and Disboard to name a few included many features that were ultimately included in our Discord bot. One problem we discovered was that we relied too heavily on 3rd party Discord bots to do several different tasks, resulting in many Discord bots doing different tasks.

## Motivation

While there are already several Discord bots that solve the issues we were looking for, we did not want to have countless bots roaming around the server as it became a lot to maintain. Therefor, the goal was to combine all the features we use in other bots into one singular bot that was a lot easier to maintain. This allowed us to differentiate ourselves from other server communities and draw in more people. Alongside making the server more streamlined, we wanted to introduce the ability to create features for the server quickly and efficiently. By creating our own Discord bot we achieved this goal and allowed the community members to suggest different features to include into the server through the bot or the bot itself.

# Program Features

## Administrative Features

- Administrative HELP commands.
- Polls.
- Varied embeds.
- Purge commands.
- Automatic role addition.
- Ban/unban commands.
- Tag configuration.
- Rule displays.
- Server logging.
- Reporting.
- Suggestions.

## Backend Features

- Self-assigning roles/member joining role assignment.
- Error handling.
- Profile scrutiny.

## Fun Features

- Custom emojis.
- Server event announcements.
- Sniping.
- Suggestions.
- Speaking with the bot.
- Ping returning

# Interface

## Readability

The number of interactable elements on the screen are kept to a minimal. The elements are also placed in generally recognised places to make them easier to see and make out. The fonts are user friendly and contrast with the background colours used. The icons used are universally recognised to make them easier to understand. The icons are combined with text to help the user interpret their usage.

## Navigation

The bot uses the 3-click-rule in order to maximise the usage of the bot. The user achieves what they are looking for in a suffice amount of time. Headings and well-structured formats are kept to in order to help the user more comfortable with navigating the interface. Menus and buttons are used to help the user move around the interface more efficiently.

## Typography

The interface fonts are large and readable and contrast the background colours where necessary. The colours are used in a thematic way. However, the universally understood colours are used to help the user interpret what each element does. There are few colours in order to keep the interface thematically consistent and understandable.

## Layout

The layout is simple to avoid misunderstanding and a hard-to-read interface. The most important sections of the interface are prioritised in the screen space and less important elements may not even be visible. Colours, fonts and images are used to draw attention to the important parts of the interface.

## Theme

The bot has a thematic interface. The server colours are incorporated to ensure coherence and a simple look. The important elements of the interface are kept the same to avoid confusion.

## Consistency

The elements of the interface that are similar in behaviour are consistent in colour, size and position. The position of important screen elements is placed in universally recognised positions, for example to close a prompt the user needs to click the “X” at the top right of the screen. The “X” is universally recognised to close program and is in the top right corner. Mobile devices and computer devices have a consistent theme at proportionally smaller/bigger scales.

# HELP

A HELP command was implemented for both normal users and administrators. The HELP command would be introduced to the user whenever a command was issued that the bot did not recognise. The administration HELP command was only available to administrators. The HELP command summarised every possible feature of the bot available to the specific individual to aid in the usage of the bot.

# Storage

- Certain data was required to be stored on an external database (via the cloud) such as a counting database that was used to store the current number in counting.
- Member records were also stored in an external database.
- The database was created using Sqlite3 and accessed and updated within the code of the bot.

# Hardware and Software Requirements

- The Discord bot required an external server running an external Discord API-caller to run 24/7.
- The server specifications were: 1GB RAM and a 1.1GHz CPU.
- The server ran the bot without latency even during peak times.
- The user had no hardware or software requirements beside the ability to run Discord.

# Program Flow

The user would be introduced to the bot when they join the Discord server (server). This allowed the user to experiment using the provided bot channels in the server. The user could use the universally recognised “help” command, that majority of server bots must have, to aid them in their usage of the bot. Once the user found the command/feature that they intended on using they followed the on-screen prompts to progress through the required arguments for that command. Ultimately leading to the user sending through the command where the bot would process the command and return a desired output.
![image](https://github.com/GuyMcKechnie/Saddu/assets/168367036/d20562dc-8e81-4726-8807-c5dc2ead8b1e)

# Bibliography

- Bot, H. (no date) Hydra - The Perfect Discord Bot. Available at: [Hydra](https://hydra.bot/).
 Maki - The Discord Bot (no date). Available at: [Maki](https://maki.gg/).
- Yggdrasil Discord Bot (no date). Available at: [Yggdrasil](https://ygg.fun/).
- Dank Memer | Home (no date). Available at: [Dankmemer](https://dankmemer.lol/).
- Ramkoe (no date) DISBOARD | Public Discord Server List. Available at: [Disboard](https://disboard.org/).
