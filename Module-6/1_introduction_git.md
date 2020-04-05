
![](https://www.python.org/static/img/python-logo.png) ![](img/vertical-line.png) ![](img/Git-Icon-1788C.png)
 
### GIT | An Introduction to Github

- Git is a free and open source distributed version control system designed to handle everything from small to very 
  large projects with speed and efficiency.

- Git allows a team of people to work together

- Git relies on the basis of distributed development

- Characteristics of Git

    - Distributed development
    - Strong support for non-linear development | Branches in Git are very lightweight.
    - Efficient handling of large projects
    - Data Assurance

- How GIT Works?
    - A Git repository is a key-value object store where all objects are indexed by their SHA-1 hash value.
    - All commits, files, tags and filesystem tree nodes are different types of objects living in this repository.
    - A Git repository is a large hash table with no provision made for hash collisions.
    - Git specifically works by taking “snapshots” of files

- GitHub Account
    - Go to [github.com](https://github.com/) and 
      enter the required user credentials asked on the site and then click on SignUp for GitHub button.
    - Creating a new Repository.
      <br/>Or<br/>
    - Find the GitHub repository [Python-Learning](https://github.com/ptoraskar/) with which you'd like to work.
        
- The “fork and branch” workflow looks something like this:
    - Fork a GitHub repository.
        - Make sure you’re logged into GitHub with your account.
        - Find the GitHub repository with which you’d like to work.
            ```html
              https://github.com/ptoraskar/Python-Learning.git
            ```
        - Click the Fork button on the upper right-hand side of the repository’s page.
   
    - Clone the forked repository to your local system.
        ```bash
        git clone https://github.com/ptoraskar/Python-Learning.git
        ```
    - Add a Git remote for the original repository.
        ```bash
        git remote add upstream https://github.com/<user-name>/Python-Learning.git
        ```
    
    - Create a feature branch in which to place your changes.
    - Make your changes to the new branch.    
        - Create and checkout a feature branch.
            ```bash
              git checkout -b <new branch name>
            ```
    - Commit the changes to the branch.
        - Make changes to the files.
        - Commit new changes
            ```bash
              git commit -m "Commit Message"
            ```
    - Push the branch to GitHub.
        - Commit your changes to the branch.
             ```bash
             git push origin new-feature 
             ```

    - Open a pull request from the new branch to the original repo.
        - If the maintainers accept your changes and merge them into the main repository, then there is a little bit of clean-up for you to do. 
        - First, you should update your local clone by using git pull upstream master. 
        - This pulls the changes from the original repository’s (indicated by upstream) master branch (indicated by master in that command) to your local cloned repository. 
        - One of the commits in the commit history will be the commit that merged your feature branch, so after you git pull your local repository’s master branch will have your feature branch’s changes committed. 
        - This means you can delete the feature branch (because the changes are already in the master branch):
        
        ```bash
          git branch -d <branch name>
        ```
        - Then you can update the master branch in your forked repository:
        ```bash
          git push origin master
        ```
        - And push the deletion of the feature branch to your GitHub repository <br /> 
        (update: an earlier version of this article listed git push -d below):

        ```bash
          git push --delete origin <branch name>
        ```

    - Keeping Your Fork in Sync
    
        ```bash
          git pull upstream master
          git push origin master
        ```

#   
[Back...](https://github.com/ptoraskar/Python-Learning/blob/master/README.md) | [Next...](/Module-1/2_overview_to_python.md)