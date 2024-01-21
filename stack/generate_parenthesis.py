class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def generate(partial,left,right):
            if len(partial)==2*n:# if length of the the partial is euqal to desired length t
                res.append(partial)#add the partial to the result list
            if left<n:# if number of open parenthesis is less than n 
                generate(partial+'(',left+1,right)#then add a open parenthesis
            if right<left:#if number of close parenthesis is less than open 
                generate(partial+')',left,right+1)#then add close parenthesis
        generate('',0,0)
        return res





        