import os
import sys
import platform

from Text_manipulator import Text_manipulator

class Formatter():
    def __init__(self):
        pass
        
    def identify(self, token = str(), tags = ["","node", platform.uname()[1]]):
        #print tokens
        try:
            tags.index(token)
            return True
        except:
            return False

    def stringfy(self, raw = list(), separator = str()):
        raw_str = str()
        
        for item in raw:
            raw_str += (item + separator)

        raw_str = raw_str[: - len(separator)]

        return raw_str

    def listfy(self, raw = str(), separator = str()):
        return raw.split(separator)
    
    def tabify(self, n_tabs = int()):
        tabs = str()
        for n in range(n_tabs):
            tabs += "\t"

        return tabs

    def check_duble_dotted(self, line = str(), tabs = int()):
        tabs += 1
        if line != str():
            if line[-1] == ":":
                line_plus = ["_"]
                
                while line_plus[-1] != str():
                    new_line = check_duble_dotted(raw_input(str(tabify(tabs))), tabs)
                    line_plus.append(new_line)
                    
                line_plus = line_plus[1:]
                
                for ln in line_plus:
                    line += ("\n" + tabify(tabs) + ln)
                
        return line
    def delinefy(self, line  = str()):
        return line.replace("\n", "\\n")

    def linefy(self, line = str()):
        return line.replace("\n", "")

    def dictionarize(self, Formatted = str(), tags = list()):
        tokens = Formatted
        
        if tags == list():
            tags = self.tags
            
        okazaki = dict()

        tag_position = list()
        for tag in tags:
            
            start = tokens.find(tag)
            
            if start != -1:
                end = start + len(tag)
            else:
                continue

            tag_position.append([start, end])

        i = 0
        for pos in tag_position:
            if i < len(tag_position) -1:
                okazaki[tags[i]] = tokens[pos[1]: tag_position[i+1][0]]
            else:
                okazaki[tags[i]] = tokens[pos[1]:]

            i += 1

        return okazaki

    def Unformat_str(self, Formatted = str(), tags = list()):
        tokens = Formatted
        
        if tags == list():
            tags = self.tags
            
        okazaki = dict()

        tag_position = list()
        for tag in tags:
            
            start = tokens.find(tag)
            
            if start != -1:
                end = start + len(tag)
            else:
                continue

            tag_position.append([start, end])

        i = 0
        for pos in tag_position:
            if i < len(tag_position) -1:
                okazaki[tags[i]] = tokens[pos[1]: tag_position[i+1][0]]
            else:
                okazaki[tags[i]] = tokens[pos[1]:]

            i += 1

        return okazaki

    def filter_in(self, raw = str()):
        if raw.count("|"):
            meta_data, data = raw.split("|",1)

        else:
            meta_data, data = None, raw

        return meta_data, data


    def filter_out(self, data = str(), meta_data = str()):
        if  meta_data != str():
            
            return meta_data + "|" + data
        
        else:
            return data

    

class Html_formatter(Formatter):
    def __init__(self):
        Formatter.__init__(self)

    def line_to_html(self, line = str(), tags = list()):
        
        return tags[0] + line + tags[1]

    def list_to_html(self, lines_list = list(), tags = list()):
        formatted = list()
        for line in lines_list:
            formatted.append(self.line_to_html(line, tags))
            
            
        return formatted
    
    def txt_to_html(self, txt = str(), tags = list(), line_separator = "\n"):
        lines_list = self.list_to_html(txt.split(line_separator), tags)
        txt = str()

        for line in lines_list:
            txt += (line + "\n")

        return txt

    def mask_analyze(raw = str(), mask_file = str()):
        return raw

    def converter_server(self, in_file = str(), out_file = str(), mask_file = str(), tags = list(), line_separator = "\n"):
        tm_otf = Text_manipulator()
        tm_otf.silent = True
        
        while True:
            try:
                line_new = self.txt_to_html(tm_otf.Read_as_input(in_file), tags, line_separator)
                tm_otf.Write_new(out_file, line_new)
                
            except KeyboardInterrupt:
                break
            
            except:
                raise
        

if __name__ == '__main__':
    argvs = sys.argv
    if len(argvs) != 1:
        f = Html_formatter()
        f.converter_server(in_file = argvs[1], out_file = argvs[2], tags = ["<h6>", str()], line_separator = "\n")
        
    else:
        print "usage: python " + __file__  + " [in_file] [out_file] [mask_file]"
