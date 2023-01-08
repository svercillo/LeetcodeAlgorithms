import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort(key=lambda k: k[0])
        heap = []
        for start, end in intervals:

            if len(heap) == 0:
                heap.append(end)
            else:
                most_free_slot = heapq.heappop(heap)
                if most_free_slot <= start:
                    most_free_slot = end
                else:
                    heapq.heappush(heap, end)

                heapq.heappush(heap, most_free_slot)

        return len(heap)
