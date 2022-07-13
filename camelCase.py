#camelCase convertion

#phrase = str(input("Enter a phrase: "))
def to_camel_case(text):
    if text != "":
        splitText = text.replace("-"," ").replace("_"," ").split(" ")
        outputString = ""
        for loop in splitText:
            outputString += (loop.capitalize())
        if text[0].isupper() == False:
            outputString = outputString[0].lower() + outputString[1:]
        print(outputString)
        return outputString
    else:
        print("")
        return ""

#to_camel_case(phrase)