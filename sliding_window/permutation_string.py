class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_permutation(hashmap, hashmap_cur):
            return hashmap_cur == hashmap

        hashmap = {}
        for char in s1:
            hashmap[char] = hashmap.get(char, 0) + 1

        hashmap_cur = {}
        left, right = 0, 0

        while right < len(s2):
            if s2[right] in hashmap:
                hashmap_cur[s2[right]] = hashmap_cur.get(s2[right], 0) + 1
                while hashmap_cur[s2[right]] > hashmap[s2[right]]:
                    hashmap_cur[s2[left]] -= 1
                    left += 1
                if check_permutation(hashmap, hashmap_cur):
                    return True
            else:
                hashmap_cur.clear()
                left = right + 1

            right += 1

        return False
