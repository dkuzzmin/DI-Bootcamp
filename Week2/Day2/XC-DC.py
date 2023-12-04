import math
class Pagination():
    
    def __init__(self, items, pageSize = 10):
        self.items = items
        self.pageSize = pageSize
        self.currentPage = 1
        self.totalPages = math.ceil(len(self.items)/ self.pageSize)

    def getVisibleItems(self):
        # self.totalPages = int(len(self.items)/ self.pageSize)
        a_start = self.pageSize*(self.currentPage - 1)
        a_end = self.currentPage*self.pageSize
        # print(a_start)
        # print(a_end)
        if a_start > len(self.items)+1:
            a_start = len(self.items)
        if a_end + 1 > len(self.items):
            a_end = len(self.items)
        return self.items[a_start:a_end]
    
    def next_page(self):
        if self.currentPage >= self.totalPages:
            print("The end of pages")
        else:
            self.currentPage += 1
        return self

    def prev_page(self):
        if self.currentPage == 1:
            print("The beginning of pages")
        else:
            self.currentPage -= 1
        return self
    def first_page(self):
        self.currentPage = 1
        return self
    def last_page(self):
        self.currentPage = self.totalPages
        return self
    def goToPage(self, pageNum):
        self.currentPage = pageNum
        return self
        
        
        
# 1 a b c d 1 2 3 4
# 2 e f g h 5 6 7 8
# 3 i j k l - 9 10 11 12
# 4 m n o p
# 5 q r s t



alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())
p.next_page().next_page()
print(p.getVisibleItems())
p.next_page()
print(p.getVisibleItems())
p.next_page()
print(p.getVisibleItems())
p.first_page()
print(p.getVisibleItems())
p.next_page()
print(p.getVisibleItems())
p.next_page()
print(p.getVisibleItems())
p.next_page()
print(p.getVisibleItems())
p.next_page()
print(p.getVisibleItems())
p.prev_page()
print(p.getVisibleItems())
p.prev_page()
print(p.getVisibleItems())
p.prev_page()
print(p.getVisibleItems())
p.prev_page()
print(p.getVisibleItems())
p.last_page()
print(p.getVisibleItems())

p.prev_page()
print(p.getVisibleItems())
p.prev_page()
print(p.getVisibleItems())
p.prev_page()
print(p.getVisibleItems())

p.last_page()
print(p.getVisibleItems())
p.goToPage(5)
print(p.getVisibleItems())


