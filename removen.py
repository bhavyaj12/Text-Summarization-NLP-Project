from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
text = word_tokenize("In word processing and desktop publishing, a hard return or paragraph break indicates a new paragraph, to be distinguished from the soft return at the end of a line internal to a paragraph. This distinction allows word wrap to automatically re-flow text as it is edited, without losing paragraph breaks. The software may apply vertical whitespace or indenting at paragraph breaks, depending on the selected style. How such documents are actually stored depends on the file format. For example, HTML uses the <p> tag as a paragraph container. In plaintext files, there are two common formats. Pre-formatted text will have a newline at the end of every physical line, and two newlines at the end of a paragraph, creating a blank line. An alternative is to only put newlines at the end of each paragraph, and leave word wrapping up to the application that displays or processes the text.")
stop_words= stopwords.words('english')
nosw = [w for w in text if not w in stop_words]
nosw
s =nltk.pos_tag(nosw)
s
new = [s for s in s if (not s[1].startswith('N') and not s[1].startswith('V'))]
new
final= [s[0] for s in new]
final
listToStr = ' '.join([str(elem) for elem in final])
listToStr

)