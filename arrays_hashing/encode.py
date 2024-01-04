class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return strs
        final_str = ""
        for string in strs:
            final_str += string + "/"
        return final_str[:-1]  # Remove the trailing "/"


    def decode(self, s: str) -> List[str]:
        # Split the input string using "/" as the delimiter
        if s==[]:
            return s
        return s.split("/")

