from nltk.corpus import stopwords

class Exhaustive:
    """ Exhaustive (statistical) method for text summarization """

    def __init__(self, **kwargs):
        self.text = None
        self.wfreq = {}
        self.tokens = []
        self.wstop = set(stopwords.words("english"))

        if "tokens" in kwargs.keys() and "text" in kwargs.keys():
            raise ValueError(
                "Error: Both tokens and text specified. Specify only one.")

        if "tokens" in kwargs.keys():
            self.tokens = []
            for line in kwargs["tokens"]:
                self.tokens += [line.split(" ")]
            assert type(self.tokens) in [list, tuple]
        else:
            self.text = kwargs["text"]
            #assert type(self.text) == str
            self.__TokenizePara(delim="।")

    """
    @kwargs:
    @term = term for which we need to calculate wt. freq.
    """

    def __GetWeightedFreq(self, **kwargs):
        """
        Returns the weighted frequency of the word specified.
        Weighted frequency is calculated as:
            wf = freq(wx)/max(freq(wi))
        """
        if len(self.wfreq) == 0:
            self.__PopulateFreq()

        word = kwargs["term"]
        if word.lower() in self.wstop or word.isdigit() or len(word) == 0:
            return 0

        if word.lower() not in self.wfreq.keys() and word.lower() not in self.wstop:
            raise ValueError("Invalid word {0} specified".format(word))
        return self.wfreq[word.lower()] / max(self.wfreq.values())

    """
    @kwargs:
    @k = k sentences to pick.
    """

    def KTopRanks(self, **kwargs):
        """ Returns the top "k" sentences based on the exh. method chosen """
        if "k" not in kwargs.keys():
            raise ValueError("Error: Missing arg \"k\"")

        k = kwargs["k"]
        if k > len(self.tokens):
            raise ValueError("Error: dimm of k is greater than \"text\"")

        if len(self.wfreq) == 0:
            self.__PopulateFreq()
        idx=0
        arr = {}
        for lines in self.tokens:
            swt = 0
            line = str()
            for word in lines:
                line += "{0} ".format(word)
                swt += self.__GetWeightedFreq(term=word)
            arr[line] = (swt,idx)
        arr = sorted(arr.items(), key=lambda x: x[1], reverse=True)
        arr=arr[:k]
        arr=sorted(arr,key=lambda x:x[1][1])
        return arr[:k]

    def __PopulateFreq(self):
        """ Builds the hashmap - words & their frequencies. """
        for item in self.tokens:
            for word in item:
                if word not in self.wstop and len(word) > 0 and word.isdigit() == False:
                    if word.lower() in self.wfreq:
                        self.wfreq[word.lower()] += 1
                    else:
                        self.wfreq[word.lower()] = 1

    """
    @kwargs:
    @delim = delimeter to split on
    """

    def __TokenizePara(self, **kwargs):
        """ Tokenize the paragraph based on the specified delim. """
        if len(self.tokens) != 0:
            raise ValueError("Error: dimm of tokens is not 0")

        lines = list(filter(None, self.text.split(kwargs["delim"])))
        for line in lines:
            arr = []
            for word in line.split(" "):
                if len(word) > 0 and word != "\n":
                    arr.append(word.lower())
            self.tokens.append(arr)
        self.tokens = list(filter(None, self.tokens))