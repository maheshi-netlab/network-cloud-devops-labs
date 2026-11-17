# Git Merge Conflict Resolution

## Scenario
Two engineers independently modified the same firewall configuration.

## Engineer A
- FIREWALL_POLICY=STRICT
- ALLOW_HTTP=false
- ALLOW_HTTPS=true

## Engineer B
- FIREWALL_POLICY=PERMISSIVE
- ALLOW_HTTP=true
- LOG_LEVEL=DEBUG

## Conflict Resolution
- Selected STRICT firewall policy.
- Kept HTTPS enabled.
- Kept HTTP disabled.
- Retained DEBUG logging.

## Git Commands Practised
- git switch
- git branch
- git diff
- git merge
- git status
- git add
- git commit
- git push

## Final Result
Both engineer branches were merged locally.
The conflict was resolved manually and the merge commit was pushed to GitHub.
