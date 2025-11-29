class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_list = set()
        
        for email in emails:
            first, second = email.split("@")
            actual_email = ""
            
            local = first.split("+")[0].replace(".","")
            actual_email = local + "@" + second
        
            final_list.add(actual_email)
        return len(final_list)
            
                    
        