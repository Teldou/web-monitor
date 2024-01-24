from multi_rake import Rake


def keywords(text):
   if text is not None:
       rake = Rake()
       keywords_with_scores = rake.apply(text)
       keywords = [keyword for keyword, score in keywords_with_scores]
       return keywords
   else:
       print("Text is None")
       return None
