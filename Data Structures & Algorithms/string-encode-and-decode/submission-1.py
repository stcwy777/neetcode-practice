class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'ΩΩ'
        else:
            return 'Ω'.join(strs)

    def decode(self, s: str) -> List[str]:

        if s == 'ΩΩ':
            return []
        else:
            return s.split('Ω')
