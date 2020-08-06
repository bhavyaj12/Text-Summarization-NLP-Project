import sys
from first import Exhaustive, TextRank


text = list()
text = "Democracy isn’t taking over the world as many hoped. In many places, it seems to be in decline, and a group of scientists tasked with studying this decline says it’s because of a complicated series of interconnected feedback loops, such as rising inequality causing political polarization. At the end of the 20th century, political theorist Francis Fukuyama declared the “end of history.” People assumed democracy had won, but now authoritarianism and dictatorships are rising again. Human society is a complex web of connections, with any single event causing many different outcomes depending on many factors. Feedback loops often produce effects that spiral well beyond the original event that started the chain reaction, such as the popularly known “butterfly effect” in natural systems. Using complex systems analysis, scientists from the University of Bristol found five interconnected reasons behind the decline of democracies. In their study, published in the European Journal of Physics, they note that “many of these mechanisms are interconnected, meaning that their temporal and/or spatial dynamics are not separable but influence each other to a significant degree.” The economy, culture, politics, technology and everything else are all linked and influence each other, often in unpredictable ways. And like in natural systems, “The system may even transform itself into a completely different structure via its capacity to evolve.” First, there was feudalism, then there was mercantilism, and now there is capitalism."
text = text.split(".")
text = [x.lstrip() for x in text]
text = [x.rstrip() for x in text]
exhm = Exhaustive(tokens=text)
ktop = exhm.KTopRanks(k=2)
for s, wt in ktop:
    print(s)



