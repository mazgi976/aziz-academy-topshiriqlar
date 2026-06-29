import json

class Report:
    def __init__(self, t, l, kind): self.t, self.l, self.k = t, l, kind
    def render(self):
        if self.k == "TXT":
            print(f"TITLE={self.t}", *self.l, sep="\n")
        else:
            print(json.dumps({"title": self.t, "lines": len(self.l)}))
            
try:
    k, t, n = input().strip(), input().strip(), int(input())
    lines = [input().strip() for _ in range(n)]
    if not t or n < 0 or any(not l for l in lines) or k not in ["TXT", "JSON"]: raise Exception
    Report(t, lines, k).render()
except: print("BAD")