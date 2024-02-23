import sys
input = sys.stdin.readline
morse_d = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "_": "..--", ",": ".-.-", ".": "---.", "?": "----",}
morse_d1 = {v: k for k, v in morse_d.items()}
ans = []

for message in open(0):
    morse_code = [morse_d[m] for m in message.strip()]
    lengths, i = reversed(tuple(map(len, morse_code))), 0
    morse_x_pauses = "".join(morse_code)
    ans.append("".join((morse_d1[morse_x_pauses[i : (i := i + j)]] for j in lengths)))
print("\n".join(ans))