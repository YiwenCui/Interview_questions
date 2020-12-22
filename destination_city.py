def destCity(paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        ele_collection =""
        for list in paths:
            for idx, ele in enumerate(list):
                ele_collection+=ele
            if ele_collection.count(ele)==1 and idx==0:
                return ele_collection
                