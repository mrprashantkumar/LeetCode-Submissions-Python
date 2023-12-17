from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.details = defaultdict(SortedList)
        self.getcuisine = defaultdict()

        for x, y, z in zip(foods, cuisines, ratings):
            self.getcuisine[x] = (y, z)
            self.details[y].add((-z, x))   
        

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.getcuisine[food]
        self.getcuisine[food] = (c, newRating)
        self.details[c].remove((-r, food))
        self.details[c].add((-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        return self.details[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)