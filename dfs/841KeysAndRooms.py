class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        rooms_stack = [0]
        while rooms_stack and len(visited) < len(rooms):
            room = rooms_stack.pop()
            if room not in visited:
                visited.add(room)
            for neighbor in rooms[room]:
                if neighbor not in visited:
                    rooms_stack.append(neighbor)
                
        return len(visited) == len(rooms)
        
        
    
        