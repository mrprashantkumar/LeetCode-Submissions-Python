class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m=len(req_skills)
        n=len(people)
        skill_index={v:i for i,v in enumerate(req_skills)}
        cand=[]
        for skills in people:
            val=0
            for skill in skills:
                val |=1<<skill_index[skill]

            cand.append(val)

        @cache
        def fn(i,mask):
            if mask==0:
                return []

            if i==n:
                return [0]*100

            if not (mask & cand[i]):
                return fn(i+1,mask)

            return min(fn(i+1,mask),[i]+fn(i+1,mask &~cand[i]),key=len)

        return fn(0,(1<<m)-1)