str = "Quotes:"

kanye_quote = "my greatest pain in live is that I will never be able to see myself perform live"

kanye1_quote = """my greatest pain in live is that  
I will never be able to see 
myself perform live"""
#cannot seperate strings into paras with "" or '', must use """

#print(str,"\n",kanye_quote,"\n",lines,"\n",kanye1_quote )
#print(kanye1_quote)

hamilton_quote = "Well, the word got around, they said, \"This kid's insane, man\""  #if you want to use single or double-quotes 
                                                                                     #in a string without closing it out, you have to 
                                                                                     #"escape" it by putting a backslash (\) in front of it
                                                                                     #or you can use """ (triple quotes) to enclose the string
print(hamilton_quote)

name = "Bob"
orphan_fee = 200
toy_fee = 121.80123

total = orphan_fee + toy_fee

print(f"{name} the total will be {total:.2f}") #'f' takes the variables and puts them directly into the string. This is called string interpolation.
#.2f rounds it to decimal points/hundredths