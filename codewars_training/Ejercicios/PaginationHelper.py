


class PaginationHelper: 


    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
        
    
    # returns the number of items within the entire collection
    def item_count(self):
        self.number_items = len(self.collection)
        return self.number_items
    
    # returns the number of pages
    def page_count(self):
        self.number_pages = int(round(len(self.collection)/self.items_per_page,0))
        return self.number_pages
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        paginas = []
        pag = []
        #index = 2 / return 2 
        for indice,item in enumerate(self.collection):
            
            if indice%self.items_per_page==0 or indice == (len(self.collection)-1): 
               paginas.append(pag) 
               pag =[]
            else: 
                pag.append(item)
                print(pag)
        print(paginas)

        if len(paginas)>=page_index>0:
            return len(paginas[page_index])
        else:
            return -1 
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass




if __name__ =="__main__":

    helper = PaginationHelper(['a','b','c','d','e','f'], 4)

   # print(helper.item_count())
   # print(helper.page_count())
    print(helper.page_item_count(1))