# CTCI 4.7
# Build Order

# My Solution
def build_order(projects, dependencies):
    adj_list = {}
    in_deg = {}
    no_edges = []
    result = []

    # Go thru projects and appropriately initilaize the adj list
    for project in projects:
        adj_list[project] = []
        in_deg[project] = 0

    # Go thru dependencies and construct the graph with the adj list
    for first, second in dependencies:
        adj_list[first].append(second)
        in_deg[second] += 1

    # Find all the nodes with no incoming edges
    for project in in_deg:
        if in_deg[project] == 0:
            no_edges.append(project)

    # Loop through all projects with no incoming edges
    while no_edges:
        node = no_edges.pop()

        # Loop through projects that the current node has an outgoing edge to
        for project in adj_list[node]:
            # Remove 1 from it's dependencies
            in_deg[project] -= 1
            # If the dependencies were fulfilled, add to no_edges
            if in_deg[project] == 0:
                no_edges.append(project)

        result.append(node)

    # If all the projects can be completed in a order
    if len(result) == len(projects):
        return result
    else:
        return None

#-------------------------------------------------------------------------------
#Testing

import unittest

class Test(unittest.TestCase):
  def test_build_order(self):
    projects = ["A", "B", "C", "D", "E", "F", "G"]
    dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
        ("A", "E"), ("B", "E"), ("D", "G")]
    print(build_order(projects, dependencies1))
    
    dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
    print(build_order(projects, dependencies2))
    
    dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
        ("B", "F"), ("C", "F"), ("G", "D")]
    print(build_order(projects, dependencies3))

if __name__ == "__main__":
  unittest.main()

