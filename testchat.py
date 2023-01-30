import azuretranslation
import chat

testdata = ['你好','結束']

for i in testdata:
    recieve_msg = azuretranslation.chitoeng(i)
    print(f"{i} \ntranslated to {recieve_msg}")
    output = chat.chatfunc(recieve_msg)
    print(f"translated to {output}")
    output = azuretranslation.engtochi(output)
    print(f"{output} \n \n")