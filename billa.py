git_commands = {
    "git init": (
        "Initialize a new Git repository. This command creates a new subdirectory named "
        "'.git' that contains all of your necessary repository files — a Git repository skeleton. "
        "After executing 'git init', you have an empty repository that you can begin to add content to.",
        "Example: git init my_repo"
    ),
    "git clone": (
        "Clone an existing repository into a new directory. This command copies an existing Git repository, "
        "including all of its history and branches, to your local machine. It is commonly used to obtain a "
        "local working copy of a remote repository.",
        "Example: git clone https://github.com/user/repo.git"
    ),
    "git add": (
        "Add file contents to the staging area. This command updates the index using the current content "
        "found in the working tree, preparing the content staged for the next commit. It doesn’t affect the "
        "repository in any way other than updating the index to prepare the content staged for the next commit.",
        "Example: git add README.md"
    ),
    "git commit": (
        "Record changes to the repository. This command takes the staged snapshot and commits it to the project "
        "history. Combined with a descriptive commit message, it serves as a milestone in the project timeline.",
        "Example: git commit -m \"Add initial README file\""
    ),
    "git status": (
        "Show the working tree status. This command displays paths that have differences between the index file "
        "and the current HEAD commit, paths that have differences between the working tree and the index file, "
        "and paths in the working tree that are not tracked by Git.",
        "Example: git status"
    ),
    "git push": (
        "Update remote refs along with associated objects. This command is used to upload local repository content "
        "to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo.",
        "Example: git push origin main"
    ),
    "git pull": (
        "Fetch from and integrate with another repository or a local branch. This command is a combination of two "
        "commands, 'git fetch' followed by 'git merge'. It updates your current branch with the latest changes from "
        "the remote repository.",
        "Example: git pull origin main"
    ),
    "git branch": (
        "List, create, or delete branches. This command allows you to create new branches, list existing branches, "
        "and delete branches that are no longer needed. Branching is essential for managing different lines of "
        "development in a project.",
        "Example: git branch feature/new-feature"
    ),
    "git checkout": (
        "Switch branches or restore working tree files. This command is used to switch between branches in a "
        "repository. It can also be used to restore files to a particular state, discarding changes in the working "
        "directory.",
        "Example: git checkout develop"
    ),
    "git merge": (
        "Join two or more development histories together. This command is used to integrate changes from different "
        "branches into a single branch, combining the sequences of commits into one unified history.",
        "Example: git merge feature/new-feature"
    ),
    "git rebase": (
        "Reapply commits on top of another base tip. This command moves or combines a sequence of commits to a new base "
        "commit, providing a linear project history by eliminating unnecessary merge commits.",
        "Example: git rebase main"
    ),
    "git remote": (
        "Manage set of tracked repositories. This command is used to create, view, and delete remote repositories that "
        "your local repository is connected to, enabling collaboration with others by sharing and accessing their work.",
        "Example: git remote add origin https://github.com/user/repo.git"
    ),
    "git fetch": (
        "Download objects and refs from another repository. This command retrieves updates from a remote repository without "
        "merging them into your local repository, allowing you to review changes before integrating them.",
        "Example: git fetch origin"
    ),
    "git log": (
        "Show commit logs. This command displays the history of commits for the repository, showing details such as the commit "
        "message, author, date, and commit SHA, which helps in tracking changes and understanding project evolution.",
        "Example: git log --oneline"
    ),
    "git diff": (
        "Show changes between commits, commit and working tree, etc. This command is used to view the differences between various "
        "states of your repository, such as changes between commits, branches, or the working directory and the staging area.",
        "Example: git diff HEAD~1"
    ),
    "git stash": (
        "Stash the changes in a dirty working directory away. This command temporarily shelves (or stashes) changes you've made to "
        "your working directory so you can work on something else, and then come back and re-apply them later on.",
        "Example: git stash save \"WIP: implementing feature X\""
    ),
    "git tag": (
        "Create, list, delete or verify a tag object signed with GPG. Tags are references that point to specific points in Git history, "
        "typically used to mark release points (e.g., v1.0, v2.0). This command allows you to manage these tags.",
        "Example: git tag -a v1.0 -m \"First release\""
    ),
    "git reset": (
        "Reset current HEAD to the specified state. This command moves the current branch to the specified commit, and optionally "
        "updates the staging area and the working directory to match, effectively undoing commits and changes.",
        "Example: git reset --hard HEAD~1"
    ),
    "git revert": (
        "Revert some existing commits. This command creates a new commit that undoes the changes introduced by a previous commit, "
        "without rewriting the project history, which is safer for shared repositories.",
        "Example: git revert abc1234"
    ),
    "git show": (
        "Show various types of objects. This command is used to display information about Git objects, such as the content of a commit, "
        "including the changes made and the commit message.",
        "Example: git show abc1234"
    ),
    # Add more Git commands and explanations as needed
}

def create_git_commands_file(filename="git_commands.txt"):
    with open(filename, "w") as file:
        file.write("Git Commands Reference\n")
        file.write("======================\n\n")
        for command, (explanation, example) in git_commands.items():
            file.write(f"{command}\n")
            file.write(f"{'-' * len(command)}\n")
            file.write(f"{explanation}\n")
            file.write(f"{example}\n\n")

if __name__ == "__main__":
    create_git_commands_file()
    print("git_commands.txt has been created with detailed Git commands and their explanations.")