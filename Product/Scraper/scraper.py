#import the regular expressions
import re
#interface for request element
class IRequest():
  def get_html(self):
      pass
#concrete request class
class Request(IRequest):
    def __init__(self,_url):
        self.url = _url

    def get_html(self):
        response = requests.get(self.url)
        return(response.text)

#Interface for the parser
class IParser():
    def parse_html(self):
        pass

#Parser implementation
class Parser(IParser):
    def __init__(self,_html,_match_dict):
        self.html = _html
        self.matching_dictonary = _match_dict

    def parse_html(self):
        #removes the html tags from a given string
        def remove_tags(_string):
            string_no_tags = re.sub("<.*?>","",_string)
            return string_no_tags
        #Runs each regex and tries to find matches
        for key in self.matching_dictonary:
            matches_list = re.findall(self.matching_dictonary[key],self.html)
            cleaned_matches_list = []
            #removes tags from each result
            for n in matches_list:
                clean_string = remove_tags(n)
                cleaned_matches_list.append(clean_string)

            #Replace dictonary element with the new list
            self.matching_dictonary[key] = cleaned_matches_list

if __name__ == "__main__":
    match_dict = {"link":"<a href.*?>.*?</a>",
                  "header":"<h1 id class>.*?</h1>"}
    parser = Parser("<h1 id class>Dette er en header</h1> <a href='google.com'>link</a><h1 id class>Anden<a href>link2</a> Header</h1>",match_dict)
    parser.parse_html()
    result = parser.matching_dictonary
    print(result)
