class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = Counter()

        for sites in cpdomains:
            freq, domain = sites.split()
            freq = int(freq)
            d[domain] += freq

            for i, x in enumerate(domain):
                if x == '.':
                    d[domain[i+1:]] += freq
        
        ans = []
        for k, v in d.items():
            ans.append(str(v) + " " + k)
        return ans