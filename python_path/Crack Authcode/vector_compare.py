#-*- utf8 -*-
import math
# vector compare not deeplearning
class VectorCompare:
    # sum(*^2)
    def magnitude(self,concordance):
        total=0
        for word,count in concordance.items():
            total+=count**2
            return math.sqrt(total)

    def relation(self,concordance_first,concordance_compare):
        relevance=0
        topvalue=0
        for word,count in concordance_first.items():
            if word in concordance_compare:
                topvalue+=count * concordance_compare[word]
        return topvalue/(self.magnitude(concordance_first)*self.magnitude(concordance_compare))