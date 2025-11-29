class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_list = set()
        
        for email in emails:
            first, second = email.split("@")
            actual_email = ""
            
            for letter in first:
                if letter == ".":
                    continue
                elif letter == "+":
                    break
                else:
                    actual_email += letter
            actual_email += "@" + second
        
            final_list.add(actual_email)
        return len(final_list)
            
                    
        