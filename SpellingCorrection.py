from textblob import TextBlob as t

a="fyne comptr"
b=t(a)
c=b.correct()
print("Corrected Text of '" + a + "' is: "+str(c))