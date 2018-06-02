# coding=utf-8

# 2018-06-02 00:59
# 2018-06-02 02:06

import collections
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        em_to_acc = dict()
        em_graph = collections.defaultdict(set)
        
        for a in accounts:
            acc = a[0]
            for em in a[1:]:
                em_to_acc[em] = acc
                em_graph[a[1]].add(em)
                em_graph[em].add(a[1])
                
        seen = set()
        mail_union = []
        for em in em_graph.keys():
            if em not in seen:
                union_set = []
                stack = [em]
                while len(stack) != 0:
                    m = stack.pop()
                    union_set.append(m)
                    seen.add(m)
                    for tm in em_graph[m]:
                        if tm not in seen:
                            stack.append(tm)
                            seen.add(tm)
                mail_union.append(union_set)
                
        ret = []
        for ml in mail_union:
            acc = [em_to_acc[ml[0]]]
            sorted_mails = sorted(ml)
            acc.extend(sorted_mails)
            ret.append(acc)
            
        return ret
    
    
# 2018-06-02 02:21 Disjoint Set Union

import collections
class Solution(object):
    class DSU(object):
        def __init__(self, size):
            self.parent = range(0, size)
            
        def find(self, x):
            while x != self.parent[x]:
                x = self.parent[x]
            return x
        
        def union(self, x, y):
            self.parent[self.find(y)] = self.find(x)
        
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dict_m_to_id = dict()
        dict_m_to_acc = dict()
        
        dsu = Solution.DSU(10000)
        
        count = 0
        for acc in accounts:
            a = acc[0]
            for m in acc[1:]:
                if m not in dict_m_to_id:
                    dict_m_to_id[m] = count
                    dict_m_to_acc[m] = a
                    count += 1
                dsu.union(dict_m_to_id[acc[1]], dict_m_to_id[m])
            
        mail_union = collections.defaultdict(set)
        for m in dict_m_to_id.keys():
            mail_union[dsu.find(dict_m_to_id[m])].add(m)
            
        return [[dict_m_to_acc[list(m)[0]]] + sorted(m) for m in mail_union.values()]
                
            

if __name__ == "__main__":
    s = Solution()
    
    accounts = accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    # [['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['Mary', 'mary@mail.com']]
    print s.accountsMerge(accounts)         
    
    accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    # [['Gabe', 'Ethan0@m.co', 'Ethan4@m.co', 'Ethan5@m.co', 'Fern0@m.co', 'Fern1@m.co', 'Fern5@m.co', 'Gabe0@m.co', 'Gabe1@m.co', 'Gabe3@m.co', 'Hanzo0@m.co', 'Hanzo1@m.co', 'Hanzo3@m.co', 'Kevin0@m.co', 'Kevin3@m.co', 'Kevin5@m.co']]
    print s.accountsMerge(accounts)
    
    
                
    