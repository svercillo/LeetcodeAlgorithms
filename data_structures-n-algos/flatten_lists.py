class Vector2D:

    pointer_stack = []

    def __init__(self, vec):
        self.vec = vec

        def dfs(arr):
            i = len(arr) - 1
            while i >= 0:

                ele = arr[i]

                if type(ele) == list:
                    if len(ele) == 0:
                        arr.pop(i)
                    else:
                        dfs(ele)

                i -= 1

        dfs(self.vec)
        obj = vec
        while type(obj) == list and len(obj) > 0:
            self.pointer_stack.append(0)
            obj = obj[0]
            if type(obj) == list and len(obj) == 0:
                self.next()

        if obj == []:
            self.poiter_stack = []

        # print(self.pointer_stack)

    def next(self) -> int:

        obj = self.vec

        # print(self.pointer_stack, obj)

        list_objs = []
        for _, pointer in enumerate(self.pointer_stack):
            # print("AAA", obj, pointer)
            list_objs.append(obj)
            obj = obj[pointer]

        ind = len(self.pointer_stack) - 1
        print("P ", self.pointer_stack)
        while ind >= 0:

            self.pointer_stack[ind] += 1
            # print(self.pointer_stack, list_objs[ind])

            if self.pointer_stack[ind] >= len(list_objs[ind]):
                self.pointer_stack.pop(ind)
            else:
                break

            ind -= 1  # gaurenteed to never be negative

        res = obj

        obj = self.vec

        for _, pointer in enumerate(self.pointer_stack):
            list_objs.append(obj)
            obj = obj[pointer]

        if self.pointer_stack != []:
            while type(obj) == list and len(obj) > 0:
                self.pointer_stack.append(0)
                obj = obj[0]

        return res

    def hasNext(self):
        print(self.pointer_stack)

        obj = self.vec

        list_objs = []
        for _, pointer in enumerate(self.pointer_stack):
            if pointer >= len(obj):
                return False
            list_objs.append(obj)
            obj = obj[pointer]

        # print(self.vec, obj)
        return (obj != self.vec) and obj != []


vector2d = Vector2D([[1, 2], [3], [4]])
vector2d = Vector2D([[], [], [-1]])

print("VALUE: ", vector2d.next())
# print("VALUE: ", vector2d.next())
# print("\n\n")
# print("VALUE: ", vector2d.next())
# print("\n\n")
print("HAS NEXT: ", vector2d.hasNext())
# print("\n\n")
# print("HAS NEXT: ", vector2d.hasNext())
# print("\n\n")
# print("VALUE: ", vector2d.next())
# print("\n\n")
# print("HAS NEXT: ", vector2d.hasNext())
