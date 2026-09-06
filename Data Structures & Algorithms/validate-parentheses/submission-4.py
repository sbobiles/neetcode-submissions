class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

                
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)

            if char == ')':
                if len(stack) != 0:
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            
            if char == '{':
                stack.append(char)

            if char == '}':
                if len(stack) != 0:
                    if stack[-1] != '{':
                        return False 
                    else:
                        stack.pop()
                else:
                    return False

            if char == '[':
                stack.append(char)
            
            if char == ']':
                if len(stack) != 0:
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True

        return False 
            
        