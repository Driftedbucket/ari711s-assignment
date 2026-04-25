import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time

class Telecom_CSP_Solver:
    def __init__(self, mountains):
        self.mountains = set(mountains)
        self.n_towers = 8
        self.grid_size = 10
    
        self.initial_domain = [
            (r, c)
            for r in range(self.grid_size)
            for c in range(self.grid_size)
            if (r, c) not in self.mountains
        ]
        self.nodes_explored = 0

    def is_consistent(self, assignment, cell):
        row, col = cell
        for placed_cell in assignment.values():
            pr, pc = placed_cell
            
            if pr == row or pc == col:
                return False
            if abs(pr - row) <= 1 and abs(pc - col) <= 1:
                return False
        return True

    def get_legal_values(self, tower, assignment, domains):
        
        return [
            cell for cell in domains[tower]
            if self.is_consistent(assignment, cell)
        ]

    def select_unassigned_variable(self, assignment, domains):

        unassigned = [t for t in range(self.n_towers) if t not in assignment]
        return min(unassigned, key=lambda t: len(self.get_legal_values(t, assignment, domains)))

    def forward_check(self, assignment, domains, tower, cell):
        
        new_domains = {t: list(d) for t, d in domains.items()}
        row, col = cell

        for other in range(self.n_towers):
            if other in assignment:
                continue
            pruned = []
            for candidate in new_domains[other]:
                cr, cc = candidate

                if (cr == row or cc == col or
                        (abs(cr - row) <= 1 and abs(cc - col) <= 1)):
                    pruned.append(candidate)
            for p in pruned:
                new_domains[other].remove(p)
            if len(new_domains[other]) == 0:
                return None 
        return new_domains

    def backtrack(self, assignment, domains):

        if len(assignment) == self.n_towers:
            return assignment

        self.nodes_explored += 1
        tower = self.select_unassigned_variable(assignment, domains)
        legal = self.get_legal_values(tower, assignment, domains)

        for cell in legal:
            assignment[tower] = cell
            new_domains = self.forward_check(assignment, domains, tower, cell)

            if new_domains is not None:
                result = self.backtrack(assignment, new_domains)
                if result is not None:
                    return result

            del assignment[tower]

        return None 

    def solve(self):
        self.nodes_explored = 0
        domains = {t: list(self.initial_domain) for t in range(self.n_towers)}
        start = time.time()
        solution = self.backtrack({}, domains)
        elapsed = time.time() - start
        return solution, elapsed

    def plot(self, solution, level_name, ax):
        ax.set_xlim(0, self.grid_size)
        ax.set_ylim(0, self.grid_size)
        ax.set_aspect('equal')

        
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                
                display_r = self.grid_size - 1 - r
                if (r, c) in self.mountains:
                    color = '#8B6347'
                else:
                    color = '#F0F4F8'
                rect = mpatches.FancyBboxPatch(
                    (c, display_r), 1, 1,
                    boxstyle="square,pad=0",
                    facecolor=color,
                    edgecolor='#AABBCC',
                    linewidth=0.5
                )
                ax.add_patch(rect)

                if (r, c) in self.mountains:
                    ax.text(c + 0.5, display_r + 0.5, 'M',
                            ha='center', va='center',
                            fontsize=8, fontweight='bold',
                            color='white')

        if solution:
            placed_cells = list(solution.values())
            for idx, (r, c) in enumerate(placed_cells):
                display_r = self.grid_size - 1 - r
                rect = mpatches.FancyBboxPatch(
                    (c + 0.05, display_r + 0.05), 0.9, 0.9,
                    boxstyle="round,pad=0.05",
                    facecolor='#1565C0',
                    edgecolor='#0D47A1',
                    linewidth=1.5
                )
                ax.add_patch(rect)
                ax.text(c + 0.5, display_r + 0.5, f'T{idx+1}',
                        ha='center', va='center',
                        fontsize=7.5, fontweight='bold',
                        color='white')

        for i in range(self.grid_size + 1):
            ax.axhline(i, color='#90A4AE', linewidth=0.5)
            ax.axvline(i, color='#90A4AE', linewidth=0.5)

        ax.set_xticks([c + 0.5 for c in range(self.grid_size)])
        ax.set_xticklabels(range(self.grid_size), fontsize=8)
        ax.set_yticks([r + 0.5 for r in range(self.grid_size)])
        ax.set_yticklabels(reversed(range(self.grid_size)), fontsize=8)
        ax.set_title(level_name, fontsize=12, fontweight='bold', pad=10)


levels = [
    {
        "name": "Level 1: Coastal Region (Easy)",
        "mountains": [(0, 0), (1, 1), (9, 9)],
    },
    {
        "name": "Level 2: Highlands Region (Medium)",
        "mountains": [(2,2),(2,3),(3,2),(3,3),(7,8),(8,7),(8,8)],
    },
    {
        "name": "Level 3: Brandberg Region (Hard)",
        "mountains": [(0,5),(1,5),(2,5),(3,5),(4,5),(5,0),(5,1),(5,2),(5,3),(5,4)],
    },
]

fig, axes = plt.subplots(1, 3, figsize=(20, 7.5))
fig.suptitle("MTC 5G Signal Booster Placement — CSP Solver",
             fontsize=16, fontweight='bold', y=1.01)

for ax, level in zip(axes, levels):
    solver = Telecom_CSP_Solver(level["mountains"])
    solution, elapsed = solver.solve()

    status = "✓ Solved" if solution else "✗ No Solution"
    print(f"\n{level['name']}")
    print(f"  Status        : {status}")
    print(f"  Nodes explored: {solver.nodes_explored}")
    print(f"  Time          : {elapsed:.4f}s")

    if solution:
        print("  Placements    :")
        for t, cell in sorted(solution.items()):
            print(f"    T{t+1} → {cell}")

    solver.plot(solution, level["name"], ax)

    info = f"{status} | Nodes: {solver.nodes_explored} | {elapsed:.3f}s"
    ax.set_xlabel(info, fontsize=8, color='#37474F')


tower_patch = mpatches.Patch(color='#1565C0', label='Tower (T)')
mountain_patch = mpatches.Patch(color='#8B6347', label='Mountain (M)')
free_patch = mpatches.Patch(color='#F0F4F8', label='Free Cell', edgecolor='#AABBCC')
fig.legend(handles=[tower_patch, mountain_patch, free_patch],
           loc='lower center', ncol=3, fontsize=10,
           bbox_to_anchor=(0.5, -0.04))

plt.tight_layout()
output_path = 'mtc_csp_solution.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"\nPlot saved to {output_path}")
plt.show()