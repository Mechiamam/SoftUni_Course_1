key = int(input())
numb_of_lines = int(input())
message = []
decrypted_message = []
for i in range(numb_of_lines):
    letter = input()
    message.append(ord(letter) + key)
    decrypted_message.append(chr(message[i]))
print(''.join(map(str, decrypted_message)))
