class Solution:

    def encode(self, strs: List[str]) -> str:
        salt = 12345
        char_separator = '.'
        word_separator = ','

        print('input', strs)

        output = []

        for s in strs:
            for c in s:
                output.append(str(ord(c)))
                output.append(char_separator)
            output.append(word_separator)

        res = ''.join(output)
        print('res',res)
        return res

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []

        salt = 12345
        char_separator = '.'
        word_separator = ','

        data = s[:-1].split(word_separator)
        output = []

        print('data',data)

        for w in data:
            characters = w[:-1].split(char_separator)
            word = []
            print('characters',characters)
            for c in characters:
                if c == "":
                    word.append("")
                    continue
                extract = chr(int(c))
                word.append(extract)
            # print('w',word)
            text = ''.join(word)
            output.append(text)
            
            # print(output)
        
        return output
         

        

