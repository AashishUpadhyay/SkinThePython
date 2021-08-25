class SetCover:
    def __init__(self) -> None:
        pass

    def find_smallest_team(self, req_skills, people):
        # O(2^N) where N is len of people
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        
        peopleSkillsMap = []
        ignore_peep_indices = set()
        for i, i_skills in enumerate(people): 
            if len(i_skills) == 0 or i in ignore_peep_indices:
                continue
            i_skill_set = set(i_skills)
            for j, j_skills in enumerate(people):
                if i == j:
                    continue
                j_skill_set = set(j_skills)
                if j_skill_set.issubset(i_skill_set):
                    ignore_peep_indices.add(j)
                    
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

    def find_smallest_team_greedy_method(self, req_skills, people):
        # O(2^N) where M is len of req_skills
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        people_skills_map = {}
        skill_people_map = {}
        ignore_peep_indices = set()
        for i, i_skills in enumerate(people): 
            if len(i_skills) == 0 or i in ignore_peep_indices:
                continue
            i_skill_set = set(i_skills)
            for j, j_skills in enumerate(people):
                if i == j:
                    continue
                j_skill_set = set(j_skills)
                if j_skill_set.issubset(i_skill_set):
                    ignore_peep_indices.add(j)
                    
            sk = 0
            for i_skill in i_skills:
                sk |= 1<<req_skills_index_map[i_skill]
                if i_skill not in skill_people_map:
                    skill_people_map[req_skills_index_map[i_skill]] = []
                skill_people_map[req_skills_index_map[i_skill]].append(i)
            people_skills_map[i] = sk

        self.teamSize = len(people)
        self.M = len(req_skills)
        self.rv = None

        self.dfs_greedy_method(0, req_skills_index_map, people_skills_map, skill_people_map, 0, 0, 0)
        return self.convert_to_indices(self.rv, len(people))

    def dfs_greedy_method(self, req_skill, req_skills_index_map, people_skills_map, skill_people_map, skillset, peopleset, people_count):

        if skillset == (pow(2, self.M) - 1) and self.teamSize > people_count:
            self.teamSize = people_count
            self.rv = peopleset
            return

        if people_count > self.teamSize or req_skill > (self.M - 1):
            return    

        if skillset & (1<<req_skill):
            self.dfs_greedy_method(req_skill + 1, req_skills_index_map, people_skills_map, skill_people_map, skillset, peopleset, people_count)      

        for peep in skill_people_map[req_skill]:
            if (1<<peep) & peopleset:
                continue

            new_skillset = skillset | people_skills_map[peep]
            new_peopleset = peopleset | (1<<peep)

            self.dfs_greedy_method(req_skill + 1, req_skills_index_map, people_skills_map, skill_people_map, new_skillset, new_peopleset, people_count+1)

    def find_smallest_team_dp(self, req_skills, people):
        M = len(req_skills)
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        
        row_length = len(people)
        col_length = pow(2, M)

        dp = [[-1 for _ in range(col_length)] for _ in range(row_length)]

        for i, peep_skills in enumerate(people):
            for j in range(1, pow(2, M)):
                has_skill = False
                rem_skills = j
                for psk in peep_skills:
                    if (1<<req_skills_index_map[psk]) > j:
                        rem_skills -=  (1<<req_skills_index_map[psk])
                        has_skill = True

                dp[i][j] = (1<<i) if has_skill else 0 | dp[i-1][rem_skills]

        return self.convert_to_indices(dp[row_length-1][col_length-1], row_length)