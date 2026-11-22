tokens = ["play","playing","playful","playground",]
print("Tokens:",tokens)

print("Length of tokens:",len(tokens))
print("first token:",tokens[0])
print("last token:",tokens[-1])
print("last token:",tokens[len(tokens)-1])

print("first two tokens:",tokens[0:2])
print("tokens in reverse:",tokens[::-1])
print("last two tokens:",tokens[-2:])

for  token in tokens:
    print(tokens,end=",")
