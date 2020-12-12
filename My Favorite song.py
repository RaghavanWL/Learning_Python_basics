import webbrowser

print("Do you want to hear my favorite music ?")
list_answer = ["Y", "YES", "N", "NO"]
input_answer = input("(Yes/No): ").upper()
if input_answer in list_answer:
    if (input_answer == "YES") or (input_answer == "Y"):
        webbrowser.open("https://youtu.be/UOxkGD8qRB4")
        print("want another one ?")
        input_answer = input("(Yes/No): ").upper()
        if (input_answer == "YES") or (input_answer == "Y"):
            webbrowser.open("https://youtu.be/RkID8_gnTxw")
else:
    print("option not available")
