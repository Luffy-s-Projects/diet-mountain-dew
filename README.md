# 🍒 Aesthetic Terminal Karaoke 🍒

> Bringing that cinematic, late-night TikTok aesthetic straight to your command line. 

**Aesthetic Terminal Karaoke** is a lightweight Python script that prints lyrics in real-time, perfectly synced to the vibe of Lana Del Rey's *Diet Mountain Dew*. Because why use standard `print()` statements when you can have a neon pink, typewriter-style aesthetic breakdown in your terminal? 💅💻

## ✨ The Vibe

* **Color-Coded:** Uses `colorama` to inject a moody, neon magenta glow directly into your console.
* **Perfect Timing:** Custom float delays sync the text generation letter-by-letter and line-by-line, mimicking the exact pacing of the song.
* **Clean Exits:** Built-in `KeyboardInterrupt` handling. If you cancel the script (`Ctrl+C`), it fades out gracefully instead of throwing an ugly Python error trace.

## 🛠️ How to run it

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/Luffy-s-Projects/diet-mountain-dew.git](https://github.com/Luffy-s-Projects/diet-mountain-dew.git)
   ```

2. **Navigate to the folder:**
   ```bash
   cd diet-mountain-dew
   ```

3. **Install the aesthetic dependencies:**
   ```bash
   pip install colorama
   ```

4. **pip install colorama**
   ```bash
   python diet_mountain_dew.py
   ```

## 🎵 Customization

Want to add your own favorite song? Just open aesthetic_karaoke.py and modify the lyrics array!

**The format is incredibly simple:**
("Your lyric here", character_typing_speed, pause_after_line)

Adjust the char_delay for fast rapping or the line_delay for dramatic, cinematic pauses.