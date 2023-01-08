class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):

        supplies = set(supplies)

        req = {}

        for i, rec in enumerate(recipes):
            req[rec] = set(ingredients[i])

        res = set()

        updated = False
        while True:
            to_delete = []
            for rec in req:
                valid = True
                for ing in req[rec]:
                    if ing not in supplies:
                        valid = False
                        break

                if valid:
                    updated = True
                    res.add(rec)
                    to_delete.append(rec)
                    supplies.add(rec)

            for rec in to_delete:
                req.pop(rec)

            if not updated:
                break

            updated = False

        return list(res)


res = Solution().findAllRecipes(
    recipes=["bread"],
    ingredients=[["yeast", "flour"]],
    supplies=["yeast", "flour", "corn"],
)


print(res)
