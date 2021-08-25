class SetCover:
    def __init__(self) -> None:
        pass

    def find_smallest_team(self, req_skills, people):
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        
        peopleSkillsMap = []
        ignore_indices = set()
        for i, i_skills in enumerate(people): 
            if len(i_skills) == 0 or i in ignore_indices:
                continue
            i_skill_set = set(i_skills)
            for j, j_skills in enumerate(people):
                if i == j:
                    continue
                j_skill_set = set(j_skills)
                if j_skill_set.issubset(i_skill_set):
                    ignore_indices.add(j)
                    
            sk = 0
            for i_skill in i_skills:
                sk |= 1<<req_skills_index_map[i_skill]
            peopleSkillsMap.append([sk, i, len(i_skills)]) 
       
        self.memo = {}
        self.N = len(req_skills)
        
        self.teamSize = len(people)
        self.rv = None
        for i in range(len(peopleSkillsMap)):
            self.dfs(i, peopleSkillsMap, 0, 0, 1)
        
        return self.convert_to_indices(self.rv, len(people))

    def dfs(self, index, peopleSkillsMap, skillset, peopleset, people_count):
        if people_count > self.teamSize:
            return
        
        peopleset = (1<<peopleSkillsMap[index][1]) | peopleset
        if peopleset in self.memo:
            return
        
        skillset = skillset | peopleSkillsMap[index][0]
        if skillset == (1<<self.N)-1 and people_count < self.teamSize:
            self.teamSize = people_count
            self.rv = peopleset
        
        for i in range(len(peopleSkillsMap)):
            if (1<<peopleSkillsMap[i][1]) & peopleset:
                continue
                
            if skillset == (skillset | peopleSkillsMap[i][0]):
                continue    
            
            self.dfs(i, peopleSkillsMap, skillset, peopleset, people_count+1)
                
        self.memo[peopleset] = None        
    
    def convert_to_indices(self, peopleset, M):   
        result = []

        for i in range(M):
            if (1<<i) & peopleset:
                result.append(i)
        return result