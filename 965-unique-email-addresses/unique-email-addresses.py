class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len({
            local.split('+')[0].replace('.', '') + '@' + domain 
            for email in emails 
            for local, domain in [email.split('@')]
        })
            
                    
        