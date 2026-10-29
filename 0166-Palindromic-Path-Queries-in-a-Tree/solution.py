from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # Euler tour and initial root-to-node XOR masks.
        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                prefix[u] = (prefix[p] if u != 0 else 0) ^ (
                    1 << (ord(chars[u]) - ord('a'))
                )

                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting table for LCA.
        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick tree supporting range XOR updates
        # and point XOR queries.
        bit = [0] * (n + 2)

        def add(i, value):
            while i < len(bit):
                bit[i] ^= value
                i += i & -i

        def range_xor(left, right, value):
            add(left + 1, value)
            add(right + 2, value)

        def point_query(i):
            result = 0
            i += 1

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(new_char) - ord('a'))

                if old_mask != new_mask:
                    range_xor(
                        tin[u],
                        tout[u],
                        old_mask ^ new_mask
                    )
                    chars[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                mask_u = prefix[u] ^ point_query(tin[u])
                mask_v = prefix[v] ^ point_query(tin[v])
                ancestor_mask = 1 << (
                    ord(chars[ancestor]) - ord('a')
                )

                path_mask = mask_u ^ mask_v ^ ancestor_mask

                answer.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer
