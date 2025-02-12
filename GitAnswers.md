
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
 
9. No, because Git doesn't work well with binary files, such as pdf or png. Knowing that, powerpoints and words documents inculde a lot of images that are considered binary files.

10. I could have an error if someone else pushed another version to git. So I will have to try to pull before pushing a new version of the code

11. If I have another version, Git will first try to merge on my local repo the version from the remote and then If the are merging error, I have to manually resolve them.

12. When branching, you create a new version on the repo that everyone is working on. It means that if someone pull the repo itself, they will see the new branch. As for forking, you copy the whole project on your own github. It means that if you modify anything on your own fork, the people that fist created the project and are at the basis of you frok won't see any changes. 
