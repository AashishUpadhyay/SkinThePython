class SetCover:
    def __init__(self) -> None:
        pass

    def find_smallest_team(self, req_skills, people):
        # O(2^N) where N is len of people
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        
        people_skills_map = {}
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
                    if j in people_skills_map:
                        del people_skills_map[j]
                    ignore_peep_indices.add(j)
                    
            sk = 0
            for i_skill in i_skills:
                sk |= 1<<req_skills_index_map[i_skill]
            people_skills_map[i] = sk
       
        self.memo = {}
        self.N = len(req_skills)
        
        self.teamSize = len(people)
        self.rv = None
        for i in people_skills_map.keys():
            self.dfs(i, people_skills_map, 0, 0, 1)
        
        return self.convert_to_indices(self.rv, len(people))

    def dfs(self, index, people_skills_map, skillset, peopleset, people_count):
        if people_count > self.teamSize:
            return
        
        peopleset = (1<<index) | peopleset
        if peopleset in self.memo:
            return
        
        skillset = skillset | people_skills_map[index]
        if skillset == (1<<self.N)-1 and people_count < self.teamSize:
            self.teamSize = people_count
            self.rv = peopleset
        
        for i in people_skills_map.keys():
            if (1<<i) & peopleset:
                continue
                
            if skillset == (skillset | people_skills_map[i]):
                continue    
            
            self.dfs(i, people_skills_map, skillset, peopleset, people_count+1)
                
        self.memo[peopleset] = None        
    
    def convert_to_indices(self, peopleset, M):
        result = []

        for i in range(M):
            if (1<<i) & peopleset:
                result.append(i)
        return result

    def find_smallest_team_greedy_method(self, req_skills, people):
        # O(2^M) where M is len of req_skills
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        people_skills_map = {}
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
                    if j in people_skills_map:
                        del people_skills_map[j]
                    ignore_peep_indices.add(j)
                    
            sk = 0
            for i_skill in i_skills:
                sk |= 1<<req_skills_index_map[i_skill]
            people_skills_map[i] = sk


        skill_people_map = {}
        for psm_k in people_skills_map.keys():
            for psk in people[psm_k]:
                if req_skills_index_map[psk] not in skill_people_map:
                    skill_people_map[req_skills_index_map[psk]] = []
                skill_people_map[req_skills_index_map[psk]].append(psm_k)    

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
        N = len(people)
        req_skills_index_map = {rs:i for i, rs in enumerate(req_skills)}
        
        row_length = len(people)
        col_length = pow(2, M)
         
        dp = {} 
        people_skills = []
        for p_sks in people:
            sk = 0
            for p_sk in p_sks:
                sk |= (1<<req_skills_index_map[p_sk])
            people_skills.append(sk)    

        def key_in_dict(ri, cj):
            return ((ri-1) in dp and cj in dp[ri-1])

        for i, skills_with_person in enumerate(people_skills):
            dp[i] = {}
            for j in range(1, pow(2, M)):
                if skills_with_person & j == 0:
                    # no match
                    if key_in_dict(i, j):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = [(pow(2, N) - 1), N]     
                else:
                    remaining_skills = (skills_with_person ^ j) & j
                    if remaining_skills == 0:
                        people_set = 1<<i
                        dp[i][j] = [people_set, 1]
                    else:
                        people_set = (1<<i) | dp[i][remaining_skills][0]    
                        if key_in_dict(i, j) and ((dp[i][remaining_skills][1] + 1) <= dp[i-1][j][1]):
                            dp[i][j] = [people_set, dp[i][remaining_skills][1] + 1]
                        else:
                            if key_in_dict(i, j):
                                dp[i][j] = dp[i-1][j]
                            else:
                                dp[i][j] = [(pow(2, N) - 1), N] 


        return self.convert_to_indices(dp[row_length-1][col_length-1][0], row_length)