# IDA Pro VoiceAttack profile

## What Is This?

This is a [VoiceAttack](https://voiceattack.com/) profile created for [IDA Pro](https://www.hex-rays.com/products/ida/index.shtml). VoiceAttack is an inexpensive software application that utilizes the [Windows Speech Recognition](https://en.wikipedia.org/wiki/Windows_Speech_Recognition) feature to enable the creation of user-defined, voice-activated macros. The user specifies a key word or phrase, then defines one or more actions to be taken when that word or phrase is recognized. The most common types of actions to be taken include key presses, mouse movement and clicks, clipboard manipulation, and sleeping. However, there are many other more advanced features available that provide a lot of flexibility to users including variables, loops,  and conditionals. You can even have the computer speak to you in response to your commands! For a high level introduction, check out our [release blog](TODO), then come back here for the details.


## How Do I Install It?

Simply import the `IDA-Pro-Profile.vap` file as a profile in your VoiceAttack application and get to work with IDA Pro!

There is also a companion IDA Pro plugin, `voice_commands.py`, that registers hotkeys for specific functionality that can be driven with voice commands. To install this plugin, copy it to your IDA Pro installation's plugin directory, start IDA Pro, say **"quick run plugins"**, select `VoiceAttack Commands` from the list, and click or say **"OK"**.

## Usage Tips

* Spend at least 15 minutes or so with the speech recognition training, it helps make for a smoother experience.
* Use a headset with a boom mic for better speech recognition. It is possible to use voice recognition software with some laptop mics if it is in a quiet enough environment, but background noise can confuse the software and cause missed commands and wasted time.
* Be sure to say **"stop listening"** or **"hold on"** if you are not actively using IDA Pro, otherwise commands can be inadvertently triggered and ruin your session. Say **"start listening"** or **"I'm back"** when you wish to return to work.
* Be polite and mindful of others! Consider whether using voice commands might cause a disruption in your work environment.

## Commands

Below is an introduction to some of the types of commands supported by the profile. This is not an exhaustive list, see the [command reference sheet](https://github.com/pages/fireeye/IDA_Pro_Voice_Attack_profile/Reference_sheet.html) for a listing of all the commands.

### Shortcut Commands

All of IDA Pro's advertised keyboard shortcuts have an associated voice command in the profile. In most cases, the voice command will map directly to the name of the menu item or action desired. When in doubt, check the [command reference sheet](https://github.com/pages/fireeye/IDA_Pro_Voice_Attack_profile/Reference_sheet.html). 

### Multi-step Commands

Some commands take multiple steps to complete, sometimes involving GUI manipulation. For example, the **"show opcodes"** and **"hide opcodes"** commands will open the **IDA Options** dialog, tab to the **Number of opcode bytes** text field, change its value, and click the OK button. Another useful command, **"look it up"**, will copy the currently highlighted token in the disassembly and search Google for it using your default browser. Most of these commands happen very quickly, but take care not to press any keys during the process as they may have unintended effects.

### Cursor Movement Commands

The cursor movement commands allow the user to move the cursor up, down, left, or right, one or more times, in specified increments. Say **"go up"** (or left, right, down) to have the arrow key pressed. Say **"go up two"** (or three, four, five, ten, twenty, forty) to go up multiple times (works with any direction). Say **"go up a lot"** (or down) to have the Page Up (or Page Down) key pressed repeatedly and rapidly. Say **"go left a lot"** (or right) to have the arrow key pressed repeatedly and rapidly. When you want it to stop, say **"stop command"**. You can set the speed with which the Page Up/Page Down key is pushed by saying **"set speed to fast"** (or medium or slow). In the disassembly view, the cursor can also be moved per “item” on the current line of disassembly by saying **"next word"** (or previous).

### Dialog Commands

Like many other applications, dialogs are a part of IDA Pro’s user interface. The ability to easily navigate and interact with items in a dialog with your voice is essential to a smooth user experience. Say **"OK"** to press the `Enter` key and disable [input recognition](#Input-Recognition-Commands). Say **"OK 2"** to do this twice, useful when you need to accept two dialogs in succession. Say **"cancel"** to press the `Esc` key and disable input recognition. Say **"tab next"** or **"tab back"** to tab through the controls in a dialog. Add the number two, three, or four to the tab commands to tab through multiple controls. Saying **"toggle check box"** or **"check box"** will press the spacebar.

### Navigation Commands

Say **"go forward"** or **"go back"** to traverse the navigation history breadcrumbs. Add the number two, three, or four to these commands to move multiple positions forward or backward in your navigation history. Say **"next function"** or **"previous function"** to jump to the next or previous function by address. Say **"next block"** or **"previous block"** to navigate through the current function by basic blocks. Say **"scroll down blocks"** or **"scroll up blocks"** to scroll through them.

With the aid of a companion IDAPython plugin, additional navigation commands are supported. This plugin registers hotkeys for really annoying key combinations that no one would want to use, but are easy to use with voice commands. Say **"function start"** or **"go to the start of (the) function"** to jump to the beginning of the current function. Say **"function end"** or **"go to the end of (the)
function"** to jump to the end of the current function. Say **"next call"** or **"previous call"** to jump between call instructions in the disassembly. Say **"next token"** or **"previous token"** to jump between instructions referencing the same mnemonic, operand, word, or other token you currently have highlighted . Saying **"jump ahead"** or **"jump back"** with prompt you with a dialog asking for input into how far you wish to jump. Input a value and the cursor will jump to the specified, relative position from your current position.

### Input Recognition Commands

These commands recognize the names of Windows and other APIs, C runtime functions, and common words that make up the names of functions and variables, especially those used when reverse engineering malware. When one of these commands is triggered, it copies the word or function name to the clipboard and pastes into active text field. These commands are used for renaming functions and variables, creating comments, searching lists, and anything else that requires text input. Saying **"caps"** before a word capitalizes the first letter. If you wish to input individual letters, say **"letter"** followed by its pronunciation in the [NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet). Individual numbers are recognized for input, but the number zero must be spoken as **"zero"** (the letter "O" will not work). To jump to a specific address or location, say **"go to address"**, and then say the address character by character, or simply say the name of the function or location you wish to jump to.

All input recognition commands are disabled until specific commands are triggered, such as **"rename"** or **"find"**. This mitigates the risk of accidentally triggering such commands. Commands such as **"OK"**, **"cancel"**, and **"select item"** will disable the input recognition commands again. It is likely that on occasion the input recognition state machine will not be in a desirable state. This can happen if you manually close a dialog you were inputting text for without using a voice command, for example. The commands **"input mode on"** and **"input mode off"** explicitly set the state accordingly.

The input recognition commands are not included in the [command reference sheet](https://github.com/pages/fireeye/IDA_Pro_Voice_Attack_profile/Reference_sheet.html) because there are too many and would make perusing the sheet for commands tedious. If you wish to view these commands, you can edit the profile in VoiceAttack.

## How Can I Help?

One area of continual improvement to this profile is in the vast dictionary of recognizable function and variable name parts under what is called the `input recognition` category of commands [described above](#Input-Recognition-Commands).  Feel free to contribute there or with entirely new commands to make IDA Pro even easier to use with your voice.

If you wish to contribute to this project, be sure to clearly identify the commands you added or changed in your pull request. Diffs do not work so well for the verbose XML format of the profile file, unfortunately.
