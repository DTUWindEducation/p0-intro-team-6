1.	What is the difference between git and GitLab? 

Git is a distributed version control system, it allows , track changes, several users to work , working with different versions. It is a command line tool
Gitlab on the other hand is a web based platform that provides hosting services for git reposetories, this is how people can work remotly on the code, it can be stored and updated.

2.	What is the difference between GitLab, GitHub, and BitBucket?  

they are all repository hosting services, but they are different from each other.

gitlab
Open-source and self-hostable
Free tier includes unlimited private repositories and collaborators.

github
Popular for open-source projects due to its large community and ecosystem.
Strong focus on social coding and collaboration.

bitbucket
Part of Atlassian's suite of tools (integrates well with Jira and Trello).
Focuses on small teams and offers free private repositories for up to five users.

3.	Why would I ever want to use git, but not GitLab?  

 If you I am working on a personal project and do not need to share it with others, I can use Git locally without relying on a remote hosting service.
Private Hosting
Git allows you to work offline and synchronize later when connectivity is available.
Cost Considerations

4.	What are the steps to update the GitLab server with some changes I made on my computer? 
git add .
git add <file-name>
git commit -m "Your descriptive commit message"
git push origin <branch-name>