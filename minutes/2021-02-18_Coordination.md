# February 18, 2021 HPC Carpentry Coordination Meeting

## Time and Venue

We have historically held sessions at 1200 UTC and 2200 UTC, although these have been sparsely attended. Volunteers willing to host additional sessions should reach out on the [Slack](https://swcarpentry.slack.com#hpc-carpentry) or the [mailing list ](https://carpentries.topicbox.com/groups/discuss-hpc) to notify potential participants.

- Time conversion for [12:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination%2C+1200+UTC&iso=20210218T12&p1=1440)
- Time conversion for [22:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination+2200+UTC&iso=20210218T22&p1=%3A)

Both meetings will use [Google Meet -URL redacted-], updated Jan. 21 with a new URL. 

## Agenda

See the [previous coordination CodiMD](https://codimd.carpentries.org/j7wbzKFhRpKB8xgJKbyorg), as well as the [coordination issue](https://github.com/hpc-carpentry/coordination/issues/27) for prior discussion.

### State of the Sites

- Coordinate a giant commit to fix the markdown line limits to clean up the diffs.
    - Consider adding [semantic linebreaks](https://rhodesmill.org/brandon/2012/one-sentence-per-line/) as well.
    - suggestion to use a linter
    - check on status of this upstream
- Status of the graphics files for the new look and feel? (Annajiat Alim Rasel and Alan O'Cais)
- Status of the parallel-novice repo? (Peter Steinbach)

### Governance 

- New, improved, less-rigid Martha's Rule for accepting proposals
- [Plan](https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng?view) for electing a steering committee to set executive priorities (Andrew Reid and Trevor Keller)
- Run our governance ideas and problems past Carpentries folks, especially Kari Jordan.

### New Business

- Collaboration opportunity with the Linux Clusters Institute?

---

## 1200 UTC Session

Attending:
- Andrew Reid 
- Benson Muite
- Alan O'Cais
- Mike Renfro
- Annajiat Alim Rasel
- Trevor Keller


### State of the Site

#### Giant commit for line lengths.

 - Rationale is to clean up the diff outputs, GitHub diffs wrap at 80 chars.
 - Good idea!
 - Changes to the lesson checker to enforce this? 
     - Yes. Divergence from upstream is minimal, change is not difficult.
     - `lesson_check.py` is a mess anyway
 - Actual process: "Manually" w/ Emacs, Trevor volunteers to do this.
 - Review PR #296, merge when ready, then do this.
 - Minimal interactions with PR #157, which also seems inactive, don't wait for that one.

- Subsidiary Q: Do this on all the repos?
     - Yes for repos with no PRs.
     - More complicated for hpc-python:
       focus on clearing PRs first, then wrap files
           
#### State of the graphics files

 - Want SVGs for ease of integration with the existing site.
    - Auto conversion from PNG is functional but unattractive.
    - AAR will ask for higher-def PNGs, and also for SVGs.
          - Recommendation: Implement what we have, and re-implement if/when we get improved images.

#### State of the parallel-novice repo?

 - Transferred to hpc-carpentry! 
 - [Issue #27](https://github.com/hpc-carpentry/coordination/issues/27) is still open because a maintainers list is not yet set up.
 - Volunteers to maintain? Contact Peter, job is mostly to review PRs.
 - "Bonus" content (Python MPi example) overlaps with hpc-intro
     - Danger of divergence?
     - Duplication of effort?
     - May come back to his after a few people have taught the workshop. Bonus content could be removed or hpc intro updated
 - Issue to volunteer: https://github.com/hpc-carpentry/hpc-parallel-novice/issues/4 

### Governance

 - Modified Martha's Rules is [Issue #28](https://github.com/hpc-carpentry/coordination/issues/28) on the coordination repo.
       - Primary modification is to use GitHub issues on the coordination repo for voting on proposals.
       - Some discussion about the importance of the "zero" response, we will use :eyes: for this.
        
 - [Plan](https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng?view) for elections
        - Same scheme for issues as for elections to the steering committee.
        - Need half a quorum +1 to pass
        - Concern: Could a pushy, well-connected proposer push something through?
            - Yes, the mechanism does not prevent this.
            - People have to actually implement the proposal, community does this.
            - Steering committee can assess oddities.
            - Begin with a presumption of good faith.
            - Steering committee members have technical means to remedy bad actions.
            - Goal is to reach consensus.
        - Should a steering committee member vote be required?
            - No, too complicated & undemocratic.
        - Participation requirement? 
            - May be important if community becomes larger.
            - Contributions are hard to define -- Issue? PR?
            - Presently, barriers to engagement are a bad idea.
            - Organization is porous
            - May want to consider slight variation on participation requirements when voting for steering commitee members as opposed to issues
                
 - Interaction with Carpentries?
        - Possibly higher-level solutions to the vocal-minority problem.
               
### Linux Clusters Institute

R. Knepper did not attend the 1200 session.

### New coordination business

 - hpc-carpentry.github.io moved to hpc-carpentry.old-site
 - Frees up name space to complete the web site migration
 - AO will fix the images and propose archiving the old one.
                

---

## 2200 UTC Session

Attending: 
- Andrew Reid
- Trevor Keller (he/they)
- Annajiat Alim Rasel (he, him, his)
- Richard Knepper (from the Linux Cluster Institute)
- Evgenij Belikov
- Wirawan Purwanto
- Mike Renfro


### Linux Cluster Institute

LCI is a non-profit out of UI Urbana-Champaign. Goal: training of admin of HPC clusters (cluster operators); develop community, network, propagate common standards 7 best practices for getting things done.

Live instruction: last year, 3 workshops. Migrating to virtual instruction. What's useful, what formats, exercises? & soliciting instructors from the wider community.

Want to find out: what people are looking in the community.

Upside of live event: Having people sitting side-by-side in person, having lunch, etc., is a major benefit of in-person instruction. How to foster that collaboration virtually? Co-working time during workshops, set aside time to call out community effort.


Introductory level: targeting those who were part of enterprise IT who haven't engaged with HPC/research computing. Covering concepts of MPI, parallel programming, understanding how application is running on HPC. Managing users (social & technical senses), advanced networking, schedulers, troubleshooting.

Last year; planning advanced topics: storage, advanced networking topics.

#### Engagement with HPC Carpentry community

Andrew: What we don't know: what space of cluster configs that we want to be in. Snippets in our lessons allow for customization. Some heterogeneity, e.g. some clusters *not* using modules. Not everyone is running SLURM. Tension between focus vs breadth. 

Richard: Content is tailored in certain direction, but other scenarios--need adapting.
One thing we are adopting: OpenHPC idioms for configuration. But not every site is following the same way. Local variabilities. We are looking into standardizing. We try to generalize to a limited continuum; if we try to target everyone: lose focus.

For HPC carpentry lesson: we need to find somewhere to do the lesson. E.g. some cluster may be highly oversubscribed--not possible to do it there. ComputeCanada has a set up using TerraForm, "cloud-native" set up, HPC infrastructure-as-a-code.

Richard: We can't give toy HPC for exercises. We've been fortunate getting resources. Now, looking into engaging with Azure.
In XSEDE project, my team works creating virtual cluster set up on OpenStack cloud. Elastic cluster--may be useful for your case. Using Ansible to set up everything. Spins up the cluster when job comes in the scheduler, spins down the compute node when not needed. Prerequisite: Needs OpenStack.

Mike: If basic 2 VM + network partition: can use [XCBC](https://github.com/XSEDE/CRI_XCBC) also. Once CentOS installed on fresh VM--that is done.

Andrew: Also looking to Carpentries for resources. But we don't want to bug them too much on this. They have some AWS resources donated. Not obvious if that can be scaled up.

Richard: Getting clarified on HPC carpentry & software carpentry. Same principle: for getting people to use HPC who were working on laptops.

Evgenij: Intermediate point between "users" and "operators": e.g. users who want to install custom software. Is there a lesson already written in Carpentry style?

Andrew: Carpentries have made major shift last year to convert to online instruction. Not trivial due to highly hands-on contents of Carpentries lesson. Very "in person" centric. Some resources published:

* https://docs.carpentries.org/topic_folders/hosts_instructors/resources_for_online_workshops.html
* https://carpentries.org/blog/2020/03/tips-for-teaching-online/

Richard: That is what we are trying to explore also. E.g. having someone there with you to collaborate, help you along is quite critical for the success of the workshop, ensuring that you are making progress. Our struggle: How to provide such kind of support in the online format?


### State of the Sites

 - Plan to do line breaks change
 - Suspend other PRs while doing that change
     - Probably only a day or two.

 - Semantics line breaks:
    - break at the end of every sentence
    - potentially also at commas and breaks in concepts
    - issue [#282](https://github.com/carpentries-incubator/hpc-intro/issues/282#issuecomment-778650807) in carpentries-incubator/hpc-intro
    - con of semantic line breaks: harder for humans to read
    - fold (https://linux.die.net/man/1/fold) is the CLI tool for wrapping text.

  - We are all in favor of the 79-character change
  - Mixed enthusiasm for the semantic line breaks. It would make it easier to spot the differences in GitHub's `diff` mode, where now, with re-wrapping after edits, it can be hard to tell.


### On hpc-parallel-novice lesson

Moved to hpc-carpentry.

General desire to set up maintenance team (done by Peter).
Volunteer here if interested: https://github.com/hpc-carpentry/hpc-parallel-novice/issues/4

### On Governance

Martha's Rules proposal: https://github.com/hpc-carpentry/coordination/issues/28 .

Democracy proposal: https://github.com/hpc-carpentry/coordination/issues/36
(was CodiMD: https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng?view)

* Concern: Preventing toxic community dynamics on Github, e.g. hijacking mechanism for some vocal, negative, but minority part.
* For a small group, almost anything works; might as well give this process a try, and update as we grow.
* Everything's fine, until there's a fight.

---

Looking for old notes? Check our [minutes](https://github.com/hpc-carpentry/coordination/tree/main/minutes)!

#### Disclaimers

General questions or feedback? Contact [team@carpentries.org](mailto:team@carpentries.org).

Inline HTML with `fa` tags refer to [Font Awesome](https://fontawesome.com/icons?d=gallery).

:::info
This document is synchronized as you type, so that everyone viewing this page sees the same text. This allows you to collaborate seamlessly on documents.

**Use of this service is restricted to members of The Carpentries community**; this is not for general purpose use (for that, try etherpad.wikimedia.org).

Users are expected to follow our **[Code of Conduct][conduct]**.

All content is publicly available under the [Creative Commons Attribution License][license].
:::

:::danger
**This server is not backed up!** 
The Carpentries is not responsible for any data loss. 
If you want to save the content of this document, please download it (Menu > Download).
:::

<!--References-->

[conduct]: https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html
[invite]: https://swc-slack-invite.herokuapp.com/
[license]: https://creativecommons.org/licenses/by/4.0/
[slack]: https://swcarpentry.slack.com
