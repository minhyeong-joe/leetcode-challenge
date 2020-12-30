from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        searchLists = list()
        # lexigraphical sort
        products.sort()
        typed = ""
        for ch in searchWord:
            typed += ch
            searchLists.append(
                [p for p in products if p.startswith(typed)][:3])
        return searchLists


sol = Solution()
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(sol.suggestedProducts(products, searchWord))

products = ["bags", "baggage", "banner", "box", "cloths"]
searchWord = "bags"
print(sol.suggestedProducts(products, searchWord))

products = ["havana"]
searchWord = "tatiana"
print(sol.suggestedProducts(products, searchWord))
