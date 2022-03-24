class DisjoinSet:
    def __init__(self) -> None:
        self.groups = {}
        self.item_groups = {}
        self.group_weights = {}

    def union(self, item1, item2):
        grp1 = self.find(item1)
        grp2 = self.find(item2)

        if grp1 == None and grp2 == None:
            grp_id = item1
            self.groups[grp_id] = set([item1, item2])
            self.group_weights[grp_id] = len(self.groups[grp_id])
            self.item_groups[item1] = grp_id
            self.item_groups[item2] = grp_id
        elif grp1 != None and grp2 != None:
            try:
                if grp1 == grp2:
                    return False

                if self.group_weights[grp1] < self.group_weights[grp2]:
                    grp1, grp2 = grp2, grp1

                for i in self.groups[grp2]:
                    self.groups[grp1].add(i)
                    self.item_groups[i] = grp1

                self.group_weights[grp1] = len(self.groups[grp1])
                del self.groups[grp2]
                del self.group_weights[grp2]
            except KeyError:
                raise Exception

        elif grp1 == None:
            self.groups[grp2].add(item1)
            self.group_weights[grp2] = len(self.groups[grp2])
            self.item_groups[item1] = grp2
        else:
            self.groups[grp1].add(item2)
            self.group_weights[grp1] = len(self.groups[grp1])
            self.item_groups[item2] = grp1

        return True

    def find(self, item):
        if item not in self.item_groups:
            return None

        return self.item_groups[item]
