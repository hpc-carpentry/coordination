# March 18, 2021 HPC Carpentry Coordination Meeting

## Time and Venue

We have historically held sessions at 1200 UTC and 2200 UTC, although these
have been sparsely attended. Volunteers willing to host additional sessions
should reach out on the [Slack](https://swcarpentry.slack.com#hpc-carpentry) or
the [mailing list ](https://carpentries.topicbox.com/groups/discuss-hpc) to
notify potential participants.

:::danger **Daylight Saving Time**

- US time zones change to DST on Sunday, March 14, 2021.

- European time changes to "Summer Time" on Sunday, March 28, 2021.

For example, in the US Eastern time zone, the March Coordination Meetings are
8:00am EDT and 6:00pm EDT, respectively. Use the conversion links below to find
your local time. :::

- Time conversion for
  [12:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination%2C+1200+UTC&iso=20210318T12&p1=1440)
- Time conversion for
  [22:00 UTC](https://www.timeanddate.com/worldclock/fixedtime.html?msg=HPC+Carpentry+Coordination+2200+UTC&iso=20210318T22&p1=%3A)

Both meetings will use Google Meet (redacted URL), updated Jan. 21, 2021 with a
new URL.

## Agenda

See the
[previous coordination CodiMD](https://codimd.carpentries.org/zgd6BdqmTiWCArrVbTzVkQ?both).
See also the
[process proposal](https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng).

### State of the Sites

- There are currently multiple issues with the "coordination" tag on the
  [hpc-intro](https://github.com/carpentries-incubator/hpc-intro/issues) repo.
  Some kind of plan of action would be useful.
  - Possibly revive the use of GitHub Projects as a management tool?
- Status of the graphics files for the new look and feel? (Annajiat Alim Rasel
  and Alan O'Cais)

### Governance

- The
  [coordination repo issue](https://github.com/carpentries-incubator/hpc-intro/issues)
  to specify the process for a steering committee has several votes, and meets
  our criteria for adoption (more than half as many :+1: votes as the number of
  participants in the prior logo proposal). Proceed with nominations in a new
  issue suggesting the existing
  [plan](https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng?view)?
- Review the
  [Carpentries Handbook on lesson development](https://docs.carpentries.org/topic_folders/governance/lesson-program-policy.html#lesson-program-incubation-roadmap)
  and identify some milestones for a path forward for the lessons? (Possibly
  this is a task for the new steering committee, once it's established.)
- Run our governance ideas and problems past Carpentries folks, especially Kari
  Jordan.

### Other Business

#### SSH vs Personal Access Tokens for GitHub & cluster logins

Active discussion on git-novice; relevant for us.

- Raised by Benson on Slack: https://app.slack.com/client/T03LE485Y/CEXAZR52T
  - https://arc-lessons.github.io/security/00_schedule.html
  - https://github.com/hpc-carpentry/coordination/issues/18
  - https://github.com/swcarpentry/git-novice/pull/779
  - https://github.com/swcarpentry/git-novice/issues/778
- [PR on hpc-shell](https://github.com/hpc-carpentry/hpc-shell/pull/37)

#### Committing on "main" and [branching workflows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

A couple of recent pull requests had features/fixes committed directly to the
default branch. This is not sustainable, for a project of this complexity.

The Carpentries lessons don't teach branching workflows, but with many people
editing the same files in very different ways, it is a necessity. We should
schedule an "advanced git" lesson to foster discussion and adoption of the
practice.

- CodeRefinery has a lesson on
  [git branch design](https://coderefinery.github.io/git-branch-design/) that
  ought to help.

---

### 1200 UTC Session

Attending

- Andrew Reid, NIST
- Annajiat Alim Rasel, Brac University
- Trevor Keller (he/they), NIST CTCMS
- Alan O'Cais (he/they), JSC
- Benson Muite,
- Toby Hodges (_complicating things by commenting on the notes during the
  meeting, without actually attending the meeting_)

#### State of the Site

##### Sweeping Changes

Mike Renfro made some good comments (esp.
[hpc-intro/297](https://github.com/carpentries-incubator/hpc-intro/issues/297))
that might touch every file:

- Asking people not to make contributions is an unnecessary barrier, and in the
  event of merge conflicts. Git provides tools to deal with conflicts. It might
  be useful to break the current set into more atomic sub-tasks, but this is
  not essential.
- This might depend on individual contributors' git expertise. We may want to
  level this up in our community, e.g. by having experts back-seat-drive for
  not-as-expert contributors.
  - See below about branching workflows.

##### GitHub Projects

Little/no interest in github projects as a way forward.

##### Website

- Logos: [It's done!](http://www.hpc-carpentry.org)
- Content: if there's anything you want migrated from the "old" site, file an
  issue or PR.

Alan started an [hpccarpentry](https://twitter.com/hpccarpentry) Twitter
account, but, does not use Twitter.

Alan also shared access to the HPC Carpentry twitter account with some
attendees.

#### Governance

##### Process for Decisions

- General agreement that there were sufficient upvotes, and insufficient
  objections, to adopt the democratic process from our
  [plan](https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng?view).
- Next step is to create a new issue soliciting nominations for a
  [steering committee](https://codimd.carpentries.org/3VbpZ4C5T5eLD9V_0ZJGng?view)
- Duties and responsibilities of the steering committee remain a bit vague, but
  the overall purpose is to keep things on-track for developing the lessons
  into Carpentries lessons, and preventing side-tracks into rabbit-holes.
  - [name=toby]: I suspect we will want a "Core Team liaison" to this Steering
    Committee when it is established, who would attend their meetings/provide
    updates and input from The Carpentries side. That will probably be me,
    though I can't guarantee that I will be able to join the calls e.g. if they
    happen in the middle of my night.
    - [name=Trevor]: We're happy to schedule around that!

##### How well do the lessons mesh with the Curriculum Development Handbook?

- Andrew intends to review and identify some milestones in curriculum
  development for the next Coord Meeting
- Trevor will join this
- Annajiat would like to join as well

#### New Business

##### SSH vs Personal Access Tokens for github.

- GitHub is deprecating passwords, so we need to think about how to get
  learners on-board with the new workflow. This is active at other levels, e.g.
  Carpentries is working on this, deciding whether to prioritize SSH or tokens.
  Prioritizing SSH is a no-brainer for HPC, but this is maybe not what
  Carpentries wants to do.
- SSH is more widely used and general (GitHub, [GitLab](https://gitlab.com),
  [Gitee](https://gitee.com), [Gitea](https://gitea.io)), whereas tokens are
  github-specific.
- HPC lessons don't actually use git in the learning workflow, but we do have a
  requirement to connect to remote systems.
  - There is an existing
    [open issue](https://github.com/carpentries-incubator/hpc-intro/issues/164)
    on SSH key hygiene on HPC Intro.
  - Question about scope -- HPC Intro seems natural for the scope, but there is
    a danger of burning up a lot of time on non-HPC-specific issues. Possibly a
    separate introductory lesson could elaborate on SSH best-practices with
    less of a time constraint. (HPC-shell?)
  - HPC Intro scope is extra-natural because the key mechanics naturally lie
    between "here's your laptop" and "here's the cluster", which is integral to
    the HPC Intro flow.
  - Re-opens the issue of whether a shell lesson should be a prerequisite for
    HPC Intro.
    - [name=toby]: "danger of burning up a lot of time on
      non-~~HPC~~Git-specific issues" is the exact reason some are reluctant to
      address SSH in the Git lesson too! I am beginning to think this would be
      best addressed in SWC Shell, where it could serve as good prep for remote
      access generally, as well as the SWC Git lesson and (one day!) HPC
      Carpentry lessons. [name=andrew]: :+1:
  - Protecting the shared resources we're teaching about is sufficiently
    important that the time investment in delineating best practices is
    worthwhile. Having learners construct an `~/.ssh/config` file is useful in
    capturing the info in a recoverable/discoverable way, vs. just telling
    learners what command-line flags to use.
    - [name=toby]: :+1: I suspect that, where GitHub is leading, others will
      follow, and password access will start to be phased out on other
      platforms (version control and otherwise). So SSH is likely to become
      more universally relevant/worth spending time on.
- Learners may (should!) become contributors, and making this easier is useful,
  though it's possible to contribute solely through the github website.
- Maybe HPC-shell should be considered as introduction to UNIX Shell for HPC,
  with all remote cluster material done in HPC Intro

##### Branching Workflows in Git

- Failing to branch a fork of the hpc-intro repo creates divergent forks, and
  makes further development more complex and messy. Contributors should use a
  branching workflow. Carpentries git lesson doesn't quite get to that point,
  but the Code Refinery lessons do this. (Links above in the agenda.)
- Someone [name=Trevor] should host a tutorial on branching workflows for our
  community. Maybe in one of the co-working slots?
  - This session could be recorded and made available afterwards.
- Counterpoint: Not all changes rise to this level of complexity, having a low
  barrier to contributions for easy fixes would encourage contributions. Use
  tags to identify "easy" vs "hard" issues? Also, the branching workflow is a
  divergence from the Carpentries git lesson.
- Counter-counterpoint: The goal of the Carpentries git lesson is to capture
  changes to largely non-shared, individual code bases, and is perhaps not
  representative of the level of shared contributions implied in
  lesson-development.
  - Question: What does the GitHub WebUI do by default? Forks but doesn't
    branch on the fork, we think.
- [name=Trevor] will teach the
  [Git branching workflow lesson from Code Refinery](https://coderefinery.github.io/git-branch-design/)
  in next co-working hours. Is this something that should be in HPC Carpentry
  for an introduction to collaborative software development?

---

### 2200 UTC Session

Attending

- Andrew Reid, NIST
- Jon Guyer, NIST
- Mike Renfro, TN Tech
- Trevor Keller, NIST
- Callum Walley, NeSI
- Annajiat Alim Rasel, Brac University

##### Branching Workflows in Git

- Mike flogs his instructor checkout notes from
  https://swcarpentry.slack.com/archives/C08BVNU00/p1590413018058200?thread_ts=1590374027.053600&cid=C08BVNU00
  that technically would meet the requirements for branching and submitting a
  proper PR:

> 1. Create a fork of (insert repository here) into your GitHub account.
> 2. In your fork of the repository, find the file you want to edit, click on
>    its link so you see its Markdown source, and click the "Edit this file"
>    button (pencil icon) beside the "History" button.
> 3. Make your changes in the editor window and scroll down to the bottom of
>    the page.
> 4. At the bottom of the page, enter: a one-line description of the changes,
>    an optional extended description of the changes, and select the button
>    "Create a new branch for this commit and start a pull request." Give the
>    new branch a descriptive name name like 'fix-(describe fix here)' .
> 5. Finally, click the "Propose file change" button.
> 6. On the "Open a pull request" page that appears, delete all the text in the
>    box, and write a few sentences, then click the "Create pull request"
>    button.

- Motivation: Some recent PRs have had changes in the "gh-pages" of the branch,
  which has a high risk of making future commits more complicated. The
  best-practice workflow is create a branch in the forked repo, and generate
  the pull request from the branch.

- The argument about this being a barrier to contributors is unconvincing, in
  that the Github WebUI automatically does this. (See notes from Mike Renfro
  above.) Consensus is that we should encourage branching workflows.

  - Not automatic, but on the web, creating a branch just means clicking the
    button and typing a name.

- [name=Trevor] re-iterates his willingness to do a branching workflow lesson
  as part of (or instead of) the next co-working.

#### State of the Site

##### Pending coordination commits

- Besides hitting many files, the "coordination" tag was motivated by Mike's
  desire not to necessarily inflict his style opions on the community without
  further discussion. In addition to the 1200UTC discussion, this suggests we
  should not allow these pending issues to hold up other contributions.

#### Governance

- Acknowledging adoption of the two proposals from the agenda.
- Toby H. may be expected to liaise with us from the Carpentries, subject to
  availability/scheduling.
- Aside (not on the agenda): Q about whether our repos are open to new
  contributors. The "hpc-intro" lesson is in the Carpentries incubator, which
  makes it visible to recent instructor-trainees, so that one is visible. The
  Carpentries has encouraged us in the past to put more repos in the incubator,
  we could do that.
- On steps to getting into the carpentries, Andrew R. has taken the action item
  to review the lesson-development guide and try to identify milestones.
  Consensus here is that this shouldn't be a one-person activity. Once some
  milestones are ID'd, they can be brought up for discussion by the
  coordination team. Carpentries-aware colleagues could also possibly give
  feedback.

#### Other Business

##### SSH vs. Personal Access Tokens

- Github is phasing out password-based access.
- Tension between github-specific personal-access-token workflow, and more
  generic (and HPC-friendly) SSH key scheme.

- Feedback from this group

  - Guyer: Favoring SSH makes sense for this community in particular. There is
    a precedent for leaving out details of some tools, e.g. the intro lessons
    don't go into detail on the nano editor. Multiple engagement options risks
    losing focus.
  - Renfro: The minimal-effort SSH is easy to do, and clear, and reasonably
    secure, though not optimal. Supplemental-and-the-end content could cover
    better practice.
  - Albert Savary: Their cluster uses two-factor, SSH does not enter into it.
  - Keller: Out of scope for Carpentries upstream, unfair to rely on them to
    provide this instruction. It's up to us to figure out where to put this
    content. Maybe an optional module for the agent functionality?
  - Guyer: Pedagogical value in doing it the simple but laborious way, and
    releive the resulting frusttration with the advanced capabilities later on,
    which will be well-motivated, and won't just be a recipe to get through an
    unfamiliar-tool barrier.
  - We just don't know if we actually have a time constraint that complicates
    adding this content to the hpc-intro lesson.

- Consensus: Starting with a basic version is consistent with the Carpentries
  scheme, it allows for maintaining focus and do emphasis through repetition
  later on.
- [name=Benson] and [name=Annajiat] have been running mix-and-match HPC
  workshops. They _start_ with HPC Shell, then teach HPC Intro, treating the
  overlap as review.
  ([Link](https://annajiat.github.io/2021-02-14-bracu-online/))
  - Instant follow-up, a "feedback" tag now exists in the hpc-intro lesson,
    intended for PRs and issues arising from experience road-testing the
    lesson.
