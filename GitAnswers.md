5. What is a branch and why would I use one?
A branch in Git is an independent line of development within a repository. It allows developers to work on different features, bug fixes, or experiments without affecting the main project.
Why use branches?
Feature Development: Implement new features without disrupting the main codebase.
Bug Fixes: Fix issues separately before merging into the stable version.
Experimentation: Test changes without impacting the main branch.
Collaboration: Multiple developers can work on separate branches and merge changes when ready.
6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
A --- B --- C   (main)
        \
         D   (feature-branch)
A: First commit
B: Second commit
C: Third commit 
The three of them on main
D: A commit on feature-branch, which diverges from B with a single commit
(The image was generated using DALL·E, an AI-powered image generation tool.)
7. Give an example of a set of git commands that would result in a merge conflict.
# Initialize a Git repository
git init my_repo
cd my_repo
echo "Hello, World!" > file.txt
git add file.txt
git commit -m "Initial commit"
# Create a new branch and modify file.txt
git checkout -b branch1
echo "This is branch1" > file.txt  # Overwriting the file
git commit -am "Update from branch1"
# Switch back to main and modify the same line
git checkout main
echo "This is main" > file.txt  # Overwriting the same line
git commit -am "Update from main"
# Merge branch1 into main (this will cause a conflict)
git merge branch1
Since both main and branch1 modified the same line in file.txt, Git will detect a conflict and ask you to resolve it manually.
8. Is Git suitable for LaTeX documents?
Yes, Git is well-suited for LaTeX projects since .tex files are plain text, allowing Git to track changes efficiently.