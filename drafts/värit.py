# install ultraprint
import time

RED = '\033[38;2;255;0;95m'
GREEN = '\033[38;2;135;215;135m'
LILA = '\033[38;2;215;175;225m'
BLUE = '\033[38;2;135;215;225m'
YELLOW = '\033[38;2;255;255;135m'
DEEPMAGENTA = '\033[38;2;128;0;128m'
PINK = '\033[38;2;255;105;170m'
ORANGE = '\033[38;2;240;163;10m'
CYAN = '\033[96m'
RESET = '\033[0m'

print(f"{BLUE}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")
print(f"{GREEN}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")
print(f"{LILA}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")
print(f"{YELLOW}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")
print(f"{PINK}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")
print(f"{CYAN}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")
print(f"{RED}Kissa koira hevonen karhu hamsteri käärme"f"{RESET}")




# Määritä merkkijono
text = "*✧･ﾟ: *✧･ﾟ:"

# Tulosta jokainen merkki puolen sekunnin välein
for char in text:
    print(char, end='', flush=True)
    time.sleep(0.5)

