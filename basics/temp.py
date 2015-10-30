__author__ = 'naveen'
def predictLine(filename,condition):



    # a = open(filenname,'r')
    for i in range(100):
        line = a.readline()
        for words in line.split(" "):
            lword = words.lower()
            if lword in condition or words in condition and :
                print "computer-company"
                break
            elseif





input_text = '''Apple already plans to buy back `$100 billion in shares, including $`16 billion worth last quarter. Icahn probably pounded the dinner table he and Cook shared recently for their much-reported bread-breaking at Icahn's New York apartment. Apple's cash stash currently sits at a whopping `$145 billion but only $`43 billion is in the U.S., which is why Icahn wants to float bonds to cover a buy back.
Fortunately, there are “low-chill” apple varieties for temperate climates. (Chilling hours are defined as nonconsecutive hours of winter temperatures below 45 degrees.) As a general guide, if you live on or near the coast, your garden gets only 100 to 200 chilling hours. Inland San Diego gardens get about 400 to 500 chilling hours — still considered “low chill.”
If this seems a bit like déjà vu, you’ll recall that Apple just held an event to unveil two new iPhone models – the 5c and 5s – back on September 10.'''

predictLine(input_text)

a_filename = "AppleInc.txt"
f_filename = "Apple.txt"
appleinc_conditions = ['Apple Inc', 'Inc', 'Electronics','Steve Jobs','computer','employees','Apple Store','Machine']
apple_conditions = ['fruit','leaves','Botanical','breeding','Honey','wealthy','Apple']

predictLine(a_filename,appleinc_conditions)
predictLine(f_filename,apple_conditions)