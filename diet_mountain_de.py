import time
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def type_lyrics(text, char_delay, line_delay, color):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(char_delay)
    
    print()
    time.sleep(line_delay)

lyrics = [
    ("You're no good for me", 0.06, 0.6),
    ("Baby, you're no good for me", 0.06, 0.6),
    ("You're no good for me", 0.06, 0.5),
    ("But baby, I want you, I want you", 0.05, 1.2),
    ("Diet Mountain Dew, baby, New York City", 0.04, 0.4),
    ("Never was there ever a girl so pretty", 0.04, 0.6),
    ("Do you think we'll be in love forever?", 0.05, 0.4),
    ("Do you think we'll be in love?", 0.06, 1.5)
]

def main():
    print("\n" * 20)
    
    print(Style.BRIGHT + Fore.CYAN + " ♫ Playing: Diet Mountain Dew - Lana Del Rey ♫ ")
    print("=" * 50 + "\n")
    time.sleep(1.5)

    for line, c_delay, l_delay in lyrics:
        type_lyrics(line, c_delay, l_delay, Style.BRIGHT + Fore.MAGENTA)
        
    print("\n" + Fore.DARK_GREY + "[Song fades out...]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "Karaoke stopped. 🛑")
        sys.exit()